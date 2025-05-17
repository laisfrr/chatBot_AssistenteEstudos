from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

# Carrega variáveis de ambiente
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")


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
chat = client.chats.create(model=model, config=chat_config)
print("____________________________________________________________\n")
print("🤖 Assistente de Estudos")
print("Digite 'sair' para encerrar.\n")
print("____________________________________________________________\n")

while True:
    tema = input("📚 Informe o tema que deseja estudar: ").strip()
    if tema.lower() == "sair":
        break

    print("____________________________________________________________\n")
    prompt = (
        f"Explique o tema '{tema}' com exemplos simples. "
        "Depois faça 2 perguntas para o usuário fixar o conteúdo."
    )
    
    resposta = chat.send_message(prompt)
    print("\n🤖 Explicação do assistente:\n")
    print("____________________________________________________________\n")
    print(resposta.text)
    print("____________________________________________________________")
    print("\n ⚠️ Agora responda as perguntas feitas pelo assistente:")
    print("____________________________________________________________\n")
    for i in range(2):
        resposta_usuario = input(f"🔶 Resposta {i+1}: ").strip()
        feedback = chat.send_message(
            f"O usuário respondeu: '{resposta_usuario}'. "
            "Corrija se estiver errado e explique o motivo de forma educada."
        )
        print("____________________________________________________________\n")
        print(f"🔍 Feedback do assistente para resposta {i+1}:\n\n{feedback.text}\n")
        print("____________________________________________________________\n")

print("😃 Obrigado por usar o assistente de estudos! Até a próxima.")
