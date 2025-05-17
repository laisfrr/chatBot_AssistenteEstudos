# 🤖 Desafio Chat Bot — Assistente de Estudos com Google GenAI

Este projeto é um chatbot interativo com foco em educação. Ele usa a API do **Google Generative AI (Gemini)** para explicar conteúdos de forma simples, com exemplos e perguntas de fixação.

- Interface web com [Streamlit](https://streamlit.io)
- Interface por terminal

---

## 📁 Estrutura do Projeto

```
Desafio_chat_bot/
├── main.py               # Código principal do chatbot
├── .env                  # Armazena a chave da API (NÃO COMITAR)
├── requirements.txt      # Dependências do projeto
├── venv/                 # Ambiente virtual (ignorado no Git)
└── .gitignore
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Desafio_chat_bot.git
cd Desafio_chat_bot
```

### 2. Crie e ative o ambiente virtual

#### Windows (cmd)

```cmd
python -m venv venv
venv\Scripts\activate
```

#### Git Bash ou MINGW64

```bash
python -m venv venv
source venv/Scripts/activate
```

---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configure sua chave da API do Google

Crie um arquivo `.env` na raiz do projeto e adicione sua chave:

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_AQUI
```

---

### 5. Executando o Chatbot no terminal

```bash
python terminal_chatbot.py
```

---

### 6. Executando o Chatbot com interface web (Streamlit)

Se quiser uma interface web para conversar com o bot, use o Streamlit:

- Instale o Streamlit (se ainda não estiver no `requirements.txt`):

```bash
pip install streamlit
```

- Crie um arquivo, por exemplo, `app.py` com o código para rodar o chat no navegador.

- Execute o Streamlit:

```bash
streamlit run app.py
```

O navegador abrirá com a interface do chatbot.

---

## 🧠 Funcionalidades

- Explica temas de forma simples, como se fosse para uma criança.
- Fornece exemplos práticos.
- Gera perguntas para fixar o conteúdo.
- Corrige respostas com feedback educado.

---

## ✅ Requisitos

- Python 3.9+
- Chave de API do [Google Generative AI](https://aistudio.google.com/app/apikey)
- (Opcional) Streamlit para interface web

---

## 📌 Exemplo de uso no terminal

```
Informe o tema que deseja estudar: Revolução Francesa

Resposta do assistente:
"A Revolução Francesa foi um grande evento que mudou a França. Ela aconteceu porque o povo estava cansado de pagar muitos impostos (...)"

Agora é sua vez! Responda às perguntas do assistente.
Resposta 1:
```

---

## 🛑 Para sair do chatbot

Digite `sair` quando for solicitado um novo tema.

---

## ⚠️ Aviso

Não comite o arquivo `.env` com sua chave pessoal. O `.gitignore` já está configurado para isso.

---

## 📄 Licença

Este projeto é apenas para fins educacionais.
