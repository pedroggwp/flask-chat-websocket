# Chat com Websocket + Flask - Laboratório Didático de IA

[![Flask](https://img.shields.io/badge/Flask-2.3.2-%23000.svg?logo=flask)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-API-yellow)](https://ai.google.dev/)

Aplicação Flask como laboratório didático para exploração de conceitos de IA e IoT, com integração do Google Gemini para respostas automáticas e comunicação em tempo real via WebSockets.

![Diagrama de Arquitetura](link-para-imagem-ou-gif-demonstrativo.png) <!-- Adicione posteriormente -->

## ✨ Recursos Principais

- **Chat em tempo real** entre usuário e atendente
- **Integração com Google Gemini** para respostas automáticas
- **Sistema de avaliação** de respostas da IA
- **Registro de sessões** com logs individuais
- **RAG (Retrieval-Augmented Generation)** com documentos de contexto
- **Interface web moderna** com atualização automática

## 🚀 Primeira Configuração

### Pré-requisitos
- Python 3.8+
- Chave de API do Google Gemini ([obter aqui](https://aistudio.google.com/))

### Passo a Passo

1. **Clonar repositório**:
   ```bash
   git clone https://github.com/seu-usuario/TECH_flask_chat.git
   cd TECH_flask_chat
   ```
   
2. **Criar ambiente virtual**:

   ```bash
   python -m venv .venv
   ```

3. **Ativar ambiente**:

   ```bash
   # Windows:
   .venv\Scripts\activate

   # Linux/Mac:
   source .venv/bin/activate
   ```

4. **Instalar dependências**:

   ```bash
   pip install -r requirements.txt
   ```
   
5. **Configurar chave Gemini**:
Criar arquivo .env na raiz do projeto:
    ```bash
   .env
   GEMINI_API_KEY=sua_chave_aqui

6. **Adicionar documentos de contexto**:
Colocar arquivos .txt em app/gemini/docs/

7. **Executar aplicação**:

   ```bash
   flask run
   
8. **Acessar no navegador**:
http://localhost:5000

## 🗂️ Estrutura de Arquivos
   ```bash
app/
├── gemini/               # Integração com Google Gemini
│   ├── docs/             # Documentos de contexto
│   ├── juiz.py           # Avaliador de respostas
│   ├── modelo.py         # Configuração do modelo
│   └── vector_store.py   # Banco vetorial e RAG
│
├── routes/               # Controladores
│   └── chat_routes.py    # Rotas e lógica principal
│
├── utils/                # Utilitários
│   └── logging_utils.py  # Gerenciamento de logs
│
├── templates/            # Views
├── static/               # Assets estáticos
└── __init__.py           # Inicialização do app
