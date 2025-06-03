from flask import Blueprint, render_template, request, session
from datetime import datetime
from app.gemini.juiz import avaliar_resposta
from app.gemini.vector_store import rag_chain
from app.utils.logging_utils import registrar_log, carregar_historico

bp = Blueprint("chat", __name__)

@bp.route("/")
def home():
    return render_template("index.html", title="Página Inicial")

@bp.route("/usuario", methods=["GET", "POST"])
def usuario():
    if "chat_id" not in session:
        session["chat_id"] = datetime.now().strftime("%Y%m%d-%H%M%S")
        registrar_log("SISTEMA", f"=== Início da Sessão {session['chat_id']} ===", session["chat_id"])

    if request.method == "POST":
        if "enviar" in request.form:
            msg = request.form["mensagem"]
            registrar_log("USUÁRIO", msg, session["chat_id"])

            if msg.strip().endswith("?"):
                resposta = rag_chain(msg)
                avaliacao_juiz = avaliar_resposta(msg, resposta)

                if "aprovado" in avaliacao_juiz.lower():
                    registrar_log("GEMINI", resposta["result"], session["chat_id"])
                else:
                    registrar_log("JUIZ", f"IA Aluncinou ⚠️. Disse: {resposta['result']}", session["chat_id"])

        elif "encerrar" in request.form:
            registrar_log("SISTEMA", f"=== Fim da Sessão {session['chat_id']} ===", session["chat_id"])
            session.pop("chat_id", None)
    
    historico = carregar_historico(session.get("chat_id", ""))
    return render_template("usuario.html", historico=historico, title="Chat - Usuário")

@bp.route("/atendente", methods=["GET", "POST"])
def atendente():
    if "chat_id" not in session:
        session["chat_id"] = datetime.now().strftime("%Y%m%d-%H%M%S")
        registrar_log("SISTEMA", f"=== Início da Sessão {session['chat_id']} ===", session["chat_id"])

    if request.method == "POST":
        if "enviar" in request.form:
            msg = request.form["mensagem"]
            registrar_log("ATENDENTE", msg, session["chat_id"])
        elif "encerrar" in request.form:
            registrar_log("SISTEMA", f"=== Fim da Sessão {session['chat_id']} ===", session["chat_id"])
            session.pop("chat_id", None)
    
    historico = carregar_historico(session.get("chat_id", ""))
    return render_template("atendente.html", historico=historico, title="Chat - Atendente")