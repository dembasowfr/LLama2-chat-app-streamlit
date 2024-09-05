import streamlit as st
import replicate
import os

from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()  

REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN");

## Check if the .env files are correctly loaded
print("REPLICATE_API_TOKEN", REPLICATE_API_TOKEN)