# import the necessary langchain dependencies
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Use streamlit for UI development
import streamlit as stl

# Use watsonx interface
 
from watsonxlangchain import LangChainInterface 


# Setup the app

stl.title("Chat with watsonx")

# Build a prompt input template to display the prompts

prompt = stl.chat_input('Pass Your Prompt Here')


# If the user hits enter, then:
if prompt:
    # Display the prompt in the chat box
    stl.chat_message('user').markdown(prompt)