import streamlit as st
# import mysql.connector
import os
import json
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import base64
from streamlit_chat import message
from spire.doc import *
from spire.doc.common import *


load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def initialize_session_state_chat():
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Hello, Medic Here! Ask me anything about 🤗"]

    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey! 👋"]

def get_pdf_text(pdf_docs):

    # Create a Document object
    doc = Document()

    # Load a Word file
    doc.LoadFromFile(r"C:\Users\soham\Desktop\Spunky\genai\Exagram Enhanced\exagramv2\medic_disease (1).docx")

    # Get text from the entire document
    text = doc.GetText()

    # Print result
    # for pdf in pdf_docs:
    #     pdf_reader= PdfReader(pdf)
    #     for page in pdf_reader.pages:
    #         text+= page.extract_text()
    return  text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    # prompt_template = """
    # consider context as syllabus and answer question asked on given syllabus, if the answer is not in
    # provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    # Context:\n {context}?\n
    # Question: \n{question}\n

    # Answer:
    # """
    prompt_template = """
    consider yourself as medical chatbot and use context as information of all diseases to answer question of user, ask follow up question if neccesary, if the answer is not in
    provided context try to give closest answer to question\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro",
                            temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input_chain(user_question,history):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain.invoke(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)
    history.append((user_question, response["output_text"]))

    return response["output_text"]



# Streamlit app
def main():
    st.set_page_config('Medic')
   
    st.title("Medic 🌐")

    initialize_session_state_chat()

    st.title("Document Processing")
    raw_text = get_pdf_text("ko")
    text_chunks = get_text_chunks(raw_text)
    get_vector_store(text_chunks)  
    st.success("Done")

    reply_container = st.container()
    container = st.container()

    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input("Question:", placeholder="Questions About Syllabus :", key='input')
            submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input:
            with st.spinner('Generating response...'):
                output = user_input_chain(user_input, st.session_state['history'])

            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)

        if st.button("clear"):
            st.session_state['history'].clear()

    if st.session_state['generated']:
            with reply_container:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="thumbs")
                    message(st.session_state["generated"][i], key=str(i), avatar_style="fun-emoji")



if __name__ == "__main__":
    main()