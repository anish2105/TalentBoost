import torch
import os
from langchain import PromptTemplate, LLMChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS, Chroma
from langchain.chains import RetrievalQA
# embeddings = HuggingFaceEmbeddings(model_name="intfloat/e5-large-v2")

os.environ["OPENAI_API_KEY"] = "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"
embeddings = OpenAIEmbeddings()

from langchain.document_loaders.base import Document
from langchain.text_splitter import CharacterTextSplitter
import pdfplumber

def pdf_loader(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        pages = pdf.pages

        documents = []
        for page in pages:
            text = page.extract_text()
            documents.append(Document(page_content=text))

    return documents

documents = pdf_loader("resumes\Anish Resume.pdf")

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200
    )

docs = text_splitter.split_documents(documents)
db = FAISS.from_documents(docs, embeddings)
llm = OpenAI(model_name='gpt-3.5-turbo' , temperature = 0) #temperature is set to 0 so that it doesn't give randomised answers.

qa = RetrievalQA.from_chain_type(llm=llm,
                                 chain_type="stuff",
                                 retriever=db.as_retriever(k=2),
                                 return_source_documents=True,
                                 verbose=True)

# query = "job description is Blockchain and web dev intern, is the resume good enough, if yes print yes else suggest any changes to the candidate on the basis of required skills , experience or projects.Also start the answer with 'Based on the resume..'"
# result = qa(query)
# print(result['result'])


##############################################################################################################
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set the path for the resumes folder
UPLOAD_FOLDER = 'resumes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)




