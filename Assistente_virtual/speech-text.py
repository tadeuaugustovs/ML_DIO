# seção de importações
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import webbrowser
import winshell
from pygame import mixer

wikipedia.set_lang("pt")  # Define o idioma do Wikipedia para português

# função para capturar o áudio do microfone
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)  # ajusta o ruído do ambiente
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="pt-BR")  # usa reconhecimento de voz do Google
            print(said)
        except sr.UnknownValueError:
            speak("Desculpe, não entendi.")
        except sr.RequestError:
            speak("Desculpe, o serviço não está disponível.")
    return said.lower()

# função para converter texto em fala
def speak(text):
    tts = gTTS(text=text, lang='pt')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

# função para responder aos comandos reconhecidos
def respond(text):
    print("Texto reconhecido: " + text)
    
    if 'tocar minha música' in text:
        speak("Tocando sua música!")
        url = "https://www.youtube.com/watch?v=pAgnJDJN4VA&t=5s"
        webbrowser.get().open(url)
        pause_listening()

    elif 'youtube' in text or 'procurar no youtube' in text:
        speak("O que você quer buscar?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Aqui está o que encontrei sobre {keyword} no YouTube.")

    elif 'wikipédia' in text or 'pesquisar' in text:
        speak("O que você quer pesquisar?")
        query = get_audio()
        if query != '':
            result = wikipedia.summary(query, sentences=2)
            speak("De acordo com a Wikipédia:")
            print(result)
            speak(result)

    elif 'piada' in text:
        speak(pyjokes.get_joke(language="en"))

    elif 'esvaziar lixeira' in text or 'lixeira' in text:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Lixeira esvaziada.")

    elif 'horas' in text or 'que horas' in text:
        strTime = datetime.today().strftime("%H:%M")
        print(strTime)
        speak(f"Agora são {strTime}")

    elif 'tocar música' in text or 'tocar som' in text:
        speak("Tocando música agora...")
        music_dir = "C:\\Users\\UserName\\Downloads\\Music\\"  # ajuste o caminho para sua pasta de músicas
        songs = os.listdir(music_dir)
        print(songs)
        playmusic(music_dir + "\\" + songs[0])
        pause_listening()

    elif 'parar música' in text:
        speak("Parando a música.")
        stopmusic()

    elif 'sair' in text:
        speak("Tchau! Até a próxima.")
        exit()

# função que pausa o reconhecimento até o usuário digitar 'voltar'
def pause_listening():
    print("[PAUSADO] Digite 'voltar' para continuar ouvindo...")
    while True:
        cmd = input().strip().lower()
        if cmd == 'voltar':
            break

# função para tocar música local
def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()

# função para parar a música
def stopmusic():
    mixer.music.stop()

# loop principal do assistente
while True:
    print("Estou ouvindo...")
    text = get_audio()
    respond(text)
