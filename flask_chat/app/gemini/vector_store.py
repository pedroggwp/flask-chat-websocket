import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from app.gemini.modelo import model
from langchain.chains import RetrievalQA

load_dotenv()

PASTA_DOCS = os.path.join(os.path.dirname(__file__), "docs")

def carregar_documentos(pasta):
    docs = []
    for nome in os.listdir(pasta):
        if nome.endswith(".txt"):
            caminho = os.path.join(pasta, nome)
            loader = TextLoader(caminho, encoding="utf-8")
            docs.extend(loader.load())
    return docs

def criar_chain_rag():
    documentos = carregar_documentos(PASTA_DOCS)
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs_divididos = splitter.split_documents(documentos)

    embeddings = GoogleGenerativeAIEmbeddings(
        google_api_key=os.getenv("GEMINI_API_KEY"),
        model="models/embedding-001"
    )

    db = FAISS.from_documents(docs_divididos, embeddings)

    return RetrievalQA.from_chain_type(
        llm=model,
        retriever=db.as_retriever(),
        return_source_documents=True
    )

rag_chain = criar_chain_rag()