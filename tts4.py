from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio
import pyttsx3
import json
import time


# Configuração do reconhecimento de fala
def setup_speech_recognition():
    SetLogLevel(-1)  # Desativa logs desnecessários
    model = Model("model")
    recognizer = KaldiRecognizer(model, 16000)
    return recognizer


# Configuração da síntese de voz
def setup_text_to_speech():
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Ajusta a velocidade da fala
    return engine


# Função para sintetizar a fala
def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


# Obtém a hora atual
def get_current_time():
    current_time = time.strftime("%H:%M")  # Obter a hora atual no formato HH:MM
    return current_time


# Mapeamento de perguntas e respostas
responses = {
    'Quem é dev crafters': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro. Almeja construir um futuro melhor para a sociedade através de projetos.',
    'quem são devidos créditos': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro. Almeja construir um futuro melhor para a sociedade através de projetos.',
    'dev crafters quem são': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro. Almeja construir um futuro melhor para a sociedade através de projetos.',
    'dev crafters': 'DevCrafters é uma equipe de desenvolvedores estudantes da Unifametro. Almeja construir um futuro melhor para a sociedade através de projetos.'
}


# Configuração do áudio
def setup_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    return p, stream


# Função principal
def main():
    recognizer = setup_speech_recognition()
    engine = setup_text_to_speech()
    p, stream = setup_audio()

    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())

            if result is not None and 'text' in result:
                text = result['text']
                print(text)

                if 'que horas' in text.lower():
                    current_time = get_current_time()
                    speak(engine, current_time)

                if text.lower() in responses:
                    speak(engine, responses[text.lower()])