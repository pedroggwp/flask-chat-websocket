import os
from datetime import datetime
from app import socketio

def registrar_log(origem, mensagem, chat_id):
    os.makedirs("logs", exist_ok=True)
    caminho = f"logs/chat_{chat_id}.log"
    mensagem = mensagem.strip()
    if mensagem:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(caminho, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] [{origem}] {mensagem}\n")
        html = f"[{timestamp}] [{origem}] {mensagem}"
        socketio.emit("nova_mensagem", {"html": html})
    
def carregar_historico(chat_id):
    caminho = f"logs/chat_{chat_id}.log"
    linhas_coloridas = []
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = list(f.readlines())
            for linha in linhas:
                if "[USUÁRIO]" in linha:
                    cor = "red"
                elif "[ATENDENTE]" in linha:
                    cor = "blue"
                else:
                    cor = "black"
                linhas_coloridas.append(f'<font color="{cor}">{linha.strip()}</font>')
    return linhas_coloridas