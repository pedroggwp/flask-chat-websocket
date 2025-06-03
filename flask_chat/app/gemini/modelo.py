from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Instancia o modelo
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.5,
    google_api_key=api_key
)
