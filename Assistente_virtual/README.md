# 🤖 Assistente Virtual com Python

Este projeto tem como objetivo criar um **sistema de assistência virtual do zero** utilizando técnicas de **Processamento de Linguagem Natural (PLN)** em Python.

---

## 🧠 Funcionalidades

O assistente virtual é capaz de:

- 🎙️ **Ouvir comandos de voz** e convertê-los para texto (Speech-to-Text)
- 🗣️ **Converter texto em voz** para responder (Text-to-Speech)
- 🌐 **Pesquisar na Wikipédia** e ler um resumo em voz alta
- 🔎 **Realizar buscas no YouTube**
- 🎵 **Tocar música local** ou **um vídeo específico no YouTube**
- 🕒 **Informar as horas**
- 😄 **Contar piadas**
- 🗑️ **Esvaziar a lixeira do sistema**
- 🛑 **Encerrar o assistente por comando de voz**

---

## 📁 Estrutura de Arquivos

- `speech-text.py` – Arquivo principal com o código do assistente virtual&#8203;:contentReference[oaicite:0]{index=0}
- `requirements.txt` – Lista de bibliotecas necessárias para rodar o projeto&#8203;:contentReference[oaicite:1]{index=1}
- `voice.mp3` – Áudio gerado dinamicamente para as respostas do assistente
- `text_speechipynb.ipynb` – **Notebook para demonstração de Text-to-Speech e Speech-to-Text**  
  ⚠️ **Este arquivo deve ser executado no Google Colab.**

---

## 📦 Como instalar

1. Clone este repositório ou baixe os arquivos.
2. (Opcional) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
