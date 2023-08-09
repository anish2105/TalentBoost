import os
from flask import Flask, render_template, request, redirect, url_for
import pdfplumber
from langchain.document_loaders.base import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import yagmail

os.environ["OPENAI_API_KEY"] = "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"

app = Flask(__name__)

# Set the path for the resumes folder
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Initialize the embeddings, db, and llm objects outside the route
embeddings = OpenAIEmbeddings()
db = None
llm = None

def pdf_loader(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        pages = pdf.pages
        documents = []
        for page in pages:
            text = page.extract_text()
            documents.append(Document(page_content=text))
    return documents

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200
)

def send_congratulatory_email(candidate_email):
    from_email = "404found3@gmail.com"  # Your email address
    password = "nnrpejvnjwdffdwl"     # Your email password or app password
    subject = "Congratulations on Clearing the Resume Screening Test"
    message = "Dear Candidate,\n\nCongratulations! You have successfully cleared the resume screening test for the position. You are now invited to the first-round interview.\n\nPlease log in to our website using the provided password below:\n\nPassword: YourPassword123\n\nLink: http://127.0.0.1:5000/next-round\n\nWe look forward to seeing you for the interview.\n\nBest regards,\n404Found"

    try:
        yag = yagmail.SMTP(from_email, password)
        yag.send(candidate_email, subject, message)
        print("Congratulations email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
        
def send_notselected_email(candidate_email):
    from_email = "404found3@gmail.com"  # Your email address
    password = "nnrpejvnjwdffdwl"     # Your email password or app password
    subject = "Thank you for your interest in 404Found"
    message = "Dear Candidate,\n\nThank you for your interest in the position at 404Found. We appreciate you taking the time to complete our resume screening test.\n\nWe have carefully reviewed your application and qualifications, and we regret to inform you that you were not selected for the position at this time.\n\nWe were impressed with your skills and experience, but we ultimately decided to move forward with other candidates who had a more specific match with the requirements of the position.\n\nWe wish you the best of luck in your job search, and we encourage you to apply for any future openings that we may have that are a good fit for your skills and experience.\n\nSincerely,\n404Found"

    try:
        yag = yagmail.SMTP(from_email, password)
        yag.send(candidate_email, subject, message)
        print("Not selected email sent!")
    except Exception as e:
        print("Error sending email:", e)


@app.route('/', methods=['GET', 'POST'])
def index():
    global db, llm  # Access the global db and llm objects to avoid duplication

    if request.method == 'POST':
        job_title = request.form.get('job-title')
        cv_file = request.files.get('cv')
        
        if job_title and cv_file:
            global db, llm
            db = None
            llm = None
            cv_filename = cv_file.filename
            cv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))
            
            documents = pdf_loader(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))
            
            if db is None:
                docs = text_splitter.split_documents(documents)
                db = FAISS.from_documents(docs, embeddings)

            if llm is None:
                llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0)

            qa = RetrievalQA.from_chain_type(llm=llm,
                                             chain_type="stuff",
                                             retriever=db.as_retriever(k=2),
                                             return_source_documents=True,
                                             verbose=True)

            query_name = "candidate's name?"
            result_name = qa(query_name)
            ans_name = result_name['result']

            query_email = "candidate's email?"
            result_email = qa(query_email)
            ans_email = result_email['result']

            query_summary = "candidates resume summary , Give a short answer"
            result_summary = qa(query_summary)
            ans_summary = result_summary['result']

            query_sug = f"job description is {job_title}, is the resume good enough, if yes print yes else suggest any changes to the candidate on the basis of required skills , experience or projects.Also start the answer with 'Based on the resume..' , Give a short answer"
            result_sug = qa(query_sug)
            ans_sug = result_sug['result']
            
            query = f"job description is {job_title} , is he a good fit, answer between this 5 choices , [1,2,3,4,5] , where 1 is the worst option and 5 being the best option, just answer in oprion only"
            result = qa(query)
            em = result['result']
            if em > '3':
                send_congratulatory_email(ans_email)
            else:
                send_notselected_email(ans_email)
            
            return render_template('cvscreening.html', job_title=job_title, cv_filename=cv_filename, ans_name = ans_name,ans_email = ans_email, ans_summary = ans_summary , ans_sug = ans_sug )

    return render_template('index.html')

@app.route('/next-round', methods=['GET', 'POST'])
def next_round():
    if request.method == 'POST':
        entered_password = request.form.get('password')
        if entered_password == 'YourPassword123':
            cv_file = request.files.get('cv')

            if cv_file:
                db = None
                llm = None
                cv_filename = cv_file.filename
                cv_file.save(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))

                documents = pdf_loader(os.path.join(app.config['UPLOAD_FOLDER'], cv_filename))

                if db is None:
                    docs = text_splitter.split_documents(documents)
                    db = FAISS.from_documents(docs, embeddings)

                if llm is None:
                    llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0)

                qa = RetrievalQA.from_chain_type(llm=llm,
                                                 chain_type="stuff",
                                                 retriever=db.as_retriever(k=2),
                                                 return_source_documents=True,
                                                 verbose=True)

                # Generate the list of questions using the OpenAI API
                query = """
                can you ask 5 questions for this candidates interview based on this resume , machine learning role and his skills , make the questions such that it can be answered in one line"""
                result = qa(query)
                ans = result['result']
                input_string = ans

                # Split the input string into a list of questions
                questions_list = input_string.split('\n')

                # Remove the '\n' characters from each question
                questions_list = [question.strip() for question in questions_list if question.strip()]

                # Pass the questions_list and cv_filename to the template
                return render_template('question.html', questions_list=questions_list, cv_filename=cv_filename)
            else:
                return render_template('next_round.html', error_message='Please upload a resume.')
        else:
            return render_template('next_round.html', error_message='Incorrect password. Please try again.')

    return render_template('next_round.html')


@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/evaluate')
def evaluate():
    return render_template('evaluate.html')

@app.route('/go-back')
def go_back():
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
