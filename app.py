import os
import sys
from dotenv import load_dotenv

load_dotenv()

def get_API_KEY():
    api_key = os.getenv("API_KEY")
    
    return api_key