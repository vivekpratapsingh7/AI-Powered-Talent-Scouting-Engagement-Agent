import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(dotenv_path=r"backend2\.env")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not set")

client = Groq(api_key=api_key)

MODEL_NAME = "llama-3.3-70b-versatile"