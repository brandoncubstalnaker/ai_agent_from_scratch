import os
from dotenv import load_dotenv

# Load environment variables from .env file 

load_dotenv()

def get_api_key(key_name="GEMINI_API_KEY"):
    api_key = os.getenv(key_name)
    if not api_key:
        raise ValueError(f"Missing API key: {key_name}")
    return api_key	

