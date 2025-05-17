import streamlit as st
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")


if "chat" not in st.session_state:
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash"
    chat_config = types.GenerateContentConfig(
        system_instruction=(
            "Você é um assistente de estudos personalizado. "
            "Explique os temas solicitados de forma clara e sucinta, como se estivesse ensinando a uma criança de 10 anos. "
            "Inclua exemplos simples e, ao final, faça duas perguntas para ajudar na fixação do conteúdo. "
            "Se o usuário errar uma resposta, corrija de forma educada e explique o motivo da correção."
        )
    )
    st.session_state.chat = client.chats.create(model=model, config=chat_config)
    st.session_state.perguntas_feitas = False
    st.session_state.perguntas = []
    st.session_state.feedbacks = []


st.title("📚 Assistente de Estudos")
st.write("Digite um tema para começar seu estudo.")


tema = st.text_input("Tema de estudo:", key="tema")

if st.button("Enviar"):
    prompt = (
        f"Explique o tema '{tema}' com exemplos simples. "
        "Depois faça 2 perguntas para o usuário fixar o conteúdo."
    )
    resposta = st.session_state.chat.send_message(prompt)
    st.session_state.explicacao = resposta.text
    st.session_state.perguntas_feitas = True


if st.session_state.get("perguntas_feitas"):
    st.markdown("### Explicação do assistente:")
    st.write(st.session_state.explicacao)

    st.markdown("### Suas respostas:")
    with st.form("respostas_form"):
        resposta1 = st.text_input("Resposta da pergunta 1:")
        resposta2 = st.text_input("Resposta da pergunta 2:")
        enviar = st.form_submit_button("Enviar respostas")

    if enviar:
        for i, resposta_usuario in enumerate([resposta1, resposta2]):
            feedback = st.session_state.chat.send_message(
                f"O usuário respondeu: '{resposta_usuario}'. "
                "Corrija se estiver errado e explique o motivo de forma educada."
            )
            st.session_state.feedbacks.append(feedback.text)

    if st.session_state.feedbacks:
        st.markdown("### Feedback do assistente:")
        for i, fb in enumerate(st.session_state.feedbacks, 1):
            st.write(f"**Resposta {i}**: {fb}")
