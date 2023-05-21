from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core


# Síntese da voz
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Reconhecimento de fala

model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Opens microphone for listening.
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
stream.start_stream()

respostas = {
    'Quem é dev crafters': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro.Que Almeja construir um futuro melhor para a sociedade através de projetos.',
    'quem são devidos créditos': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro.Que Almeja construir um futuro melhor para a sociedade através de projetos.',
    'dev crafters quem são': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro.Que Almeja construir um futuro melhor para a sociedade através de projetos.',
    'dev crafters': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro.Que Almeja construir um futuro melhor para a sociedade através de projetos.'
}

# Loop do reconhecimento de fala
while True:
    data = stream.read(4096)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # result is a string
        result = rec.Result()
        # convert it to a json/dictionary
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
           

            if text == 'que horas são' or text == 'me diga que horas são':
                speak(core.SystemInfo.get_time())
            
            if text.lower() in respostas:
                speak(respostas[text.lower()])
