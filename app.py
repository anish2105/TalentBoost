import os
from flask import Flask, render_template, request, redirect, url_for,session
import pdfplumber
from langchain.document_loaders.base import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import yagmail
import Levenshtein

os.environ["OPENAI_API_KEY"] = "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"

app = Flask(__name__)
app.secret_key = "1234"

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
    message = "Dear Candidate,\n\nCongratulations! You have successfully cleared the resume screening test for the position. You are now invited to the first-round interview.\n\nPlease log in to our website using the provided password below:\n\nPassword: YourPassword123\n\nLink: http://ec2-13-127-117-112.ap-south-1.compute.amazonaws.com:8080/next-round\n\nWe look forward to seeing you for the interview.\n\nBest regards,\n404Found"

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

def send_hr_email(our_mail , candidate_email):
    from_email = "404found3@gmail.com"  # Your email address
    password = "nnrpejvnjwdffdwl"     # Your email password or app password
    subject = "Candidate has been selected"
    message = f"{candidate_email} has been selected"

    try:
        yag = yagmail.SMTP(from_email, password)
        yag.send(our_mail, subject, message)
        print("HR email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
        
def send_notselection_email(candidate_email):
    from_email = "404found3@gmail.com"  # Your email address
    password = "nnrpejvnjwdffdwl"     # Your email password or app password
    subject = " Update Regarding Your Interview"
    message = "We hope this message finds you well. Thank you for your interest. We appreciate the time and effort you invested in the interview process.\n\nAfter careful consideration, we regret to inform you that you have not been selected to move forward to the next stage of the selection process. While your qualifications are impressive, we have chosen to proceed with other candidates who closely match the specific requirements for the role.\n\nWe want to express our gratitude for your interest in joining [Company Name]. Your application and interview were valued, and we encourage you to consider future opportunities with us.\n\nWe wish you the best in your continued job search and professional endeavors. If you have any questions or would like feedback on your interview, please feel free to reach out to us.\n\nThank you again for considering our company. We appreciate your understanding and wish you success in your future endeavors.\n\nBest regards,\n404Found"

    try:
        yag = yagmail.SMTP(from_email, password)
        yag.send(candidate_email, subject, message)
        print("Not selected email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
        
def send_selection_email(candidate_email):
    from_email = "404found3@gmail.com"  # Your email address
    password = "nnrpejvnjwdffdwl"     # Your email password or app password
    subject = "Invitation to Final Round Face-to-Face Interview"
    message = "Congratulations! We are pleased to inform you that you have successfully cleared the first-round interview test for the position. Your performance and qualifications have impressed us.\n\nWe would like to proceed to the next stage of the selection process by inviting you to a final round of face-to-face interview. Our team is excited to learn more about you and discuss your potential contributions to our organization.\n\nExpect to hear from our team soon to coordinate the details of the upcoming interview. We are eager to meet you in person and explore the possibility of you joining our team.\n\nThank you for your interest in our company, and once again, congratulations on your achievement.\n\nBest regards,\n404Found"

    try:
        yag = yagmail.SMTP(from_email, password)
        yag.send(candidate_email, subject, message)
        print("Congratulations email sent successfully!")
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
        if entered_password == '1234':
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
                Based on the resume, generate a mix of interview questions related to the candidate's projects, domain skills, and general skills. Provide answers for the questions. Ensure that the questions generated do not include the phrases 'Domain-related question' and 'Project-related question and also they are easy to attend , keep only 6 question , start each question by adding the word 'Question:'"""
                result = qa(query)
                ques = result['result']
                input_string = ques
                
                query_email = "candidate's email?"
                result_email = qa(query_email)
                ans_email = result_email['result']
                
                # Split the input string into a list of lines
                lines = input_string.split('\n')

                # Initialize arrays to store questions and expected answers
                question_array = []
                expected_answer_array = []

                # Iterate through the lines to extract questions and expected answers
                for line in lines:
                    line = line.strip()
                    if line.startswith("Question"):
                        question_array.append(line[len("Question"):].strip())  
                    elif line.startswith("Answer:"):
                        expected_answer_array.append(line[len("Answer"):].strip())

                print(expected_answer_array)
                session['expected_answer_array'] = expected_answer_array
                session['ans_email'] = ans_email
                # Pass the question_array and expected_answer_array to the template
                return render_template('question.html', question_array=question_array, expected_answer_array=expected_answer_array, cv_filename=cv_filename)
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

@app.route('/submit', methods=['POST'])
def submit():
    user_answer_array = []
    expected_answer_array = session.get('expected_answer_array', [])
    ans_email = session.get('ans_email','')
    print(ans_email)
    print(expected_answer_array)
    # Loop through the form fields and retrieve user answers
    for i in range(1, 7):  
        user_answer = request.form.get(f'answer{i}')
        user_answer_array.append(user_answer)

    correct_count = 0
    threshold = 0.7  # Adjust as needed

    for user_answer, expected_answer in zip(user_answer_array, expected_answer_array):
        levenshtein_distance = Levenshtein.distance(user_answer.lower(), expected_answer.lower())
        max_length = max(len(user_answer), len(expected_answer))
        similarity_ratio = 1 - (levenshtein_distance / max_length)

        if similarity_ratio >= threshold:
            correct_count += 1

    accuracy = correct_count / len(user_answer_array) * 100
    print(accuracy)
    if accuracy>65:
        send_selection_email(ans_email)
        send_hr_email('404found3@gmail.com',ans_email)
    else:
        send_notselection_email(ans_email)
    # Render the evaluate.html template and pass the accuracy
    return render_template('evaluate.html', accuracy=accuracy)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
