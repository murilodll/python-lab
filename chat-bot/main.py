# Titulo do Projeto: Chat-Bot
  # Campo de Mensagem [Input]
    # Quando usuário enviar mensagem na conversa
    # Mandar mensagem para IA Responder
    # Mostrar resposta da IA na Conversa

# Streamlit e OpenAI

import streamlit as st
import chave
from openai import OpenAI

modelo_ia = OpenAI(api_key=chave.API_KEY, 
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")

st.title("Chat-Bot com IA")
st.write("Este é um exemplo de um Chat-Bot simples usando Streamlit e OpenAI.")

msg_usuario = st.chat_input("Digite sua mensagem:")

if not "lista_mensagens" in st.session_state:
  st.session_state["lista_mensagens"] = []

# Mostrar histórico de mensagens
for msg in st.session_state["lista_mensagens"]:
  st.chat_message(msg["role"]).write(msg["content"])

# Mostrar mensagem do usuário
if msg_usuario:

  # Mostrar mensagem do usuário e adicionar na Conversa
  st.chat_message("user").write(msg_usuario)
  msg = {"role": "user", "content": msg_usuario}
  st.session_state["lista_mensagens"].append(msg)

  # Mandar mensagem para IA Responder
  # resposta_ia = "Esta é uma resposta simulada da IA para a mensagem: " + msg_usuario

  # Chamar a API da IA para obter a resposta
  resposta_ia = modelo_ia.chat.completions.create(
    model="gemini-flash-lite-latest",
    messages=st.session_state["lista_mensagens"]
  ).choices[0].message.content

  # Mostrar resposta da IA na Conversa e adicionar na Conversa
  st.chat_message("assistant").write(resposta_ia)
  msg = {"role": "assistant", "content": resposta_ia}
  st.session_state["lista_mensagens"].append(msg)