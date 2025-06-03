from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
import os
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

juiz = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.3,
    google_api_key=api_key
)

prompt_juiz = '''
Você é um avaliador imparcial. Sua tarefa é revisar a resposta de um tutor de IA para uma pergunta de aluno.
'
Critérios:
- A resposta está tecnicamente correta?
- Está clara para o nível médio técnico?
- O próximo passo sugerido está bem formulado?

Se a resposta for boa, diga “✅ Aprovado” e explique por quê.
Se tiver problemas, diga “⚠️ Reprovado” e proponha uma versão melhorada.
'''

def avaliar_resposta(pergunta, resposta_tutor):
    mensagens = [
        SystemMessage(content=prompt_juiz),
        HumanMessage(content=f"Pergunta do aluno: {pergunta}\n\nResposta do tutor: {resposta_tutor['result']}")
    ]
    return juiz.invoke(mensagens).content

