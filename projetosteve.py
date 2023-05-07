#projeto kleberesto

import speech_recognition as sr

#Cria um reconhecedor
r = sr.Recognizer()

#Abrir mic para captura
with sr.Microphone() as source:
    audio = r.listen(source) #Define mic como fonte de áudio
    print(r.recognize_google(audio, language='pt'))
