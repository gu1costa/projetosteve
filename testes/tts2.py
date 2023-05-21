import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
pt_voices = [v for v in voices if 'brazil' in v.languages]

# Itera sobre a lista de vozes masculinas em português e seleciona a primeira voz encontrada
for voice in pt_voices:
    if voice.gender == 'male':
        engine.setProperty('voice', voice.id)
        break

engine.say("Vou falar esse texto")
engine.runAndWait()
