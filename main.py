import speech_recognition as sr 
import time 
from time import ctime 
import webbrowser

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try: 
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            print('Lo siento, no te entedi')
        except sr.RequestError:
            print('Lo siento, error de conexión')
        return voice_data

def respond(voice_data):
    if 'como te llamas' in voice_data:
        print('Mi nombre es el de tu puta madre')
    if 'que hora es'in voice_data:
        print(ctime())
    if 'search' in voice_data:
        buscar = record_audio('Que quieres hijo de tu ptm?')
        url = 'https://google.com/search?q=' + buscar
        webbrowser.get().open(url)
        print('Esto es lo que encontre para: ' + buscar)
    if "Lugar" in voice_data:
        lugar = record_audio("que lugar pinche puto?")
        url = 'https://google.nl/maps/place/' + lugar + '/&amp;'
        print('Esto es lo que encontre para: ' + lugar)
    if 'colo favorito' in voice_data:
        print('Mi color favorito es del tu puta madre')
    if 'comida favorita' in voice_data:
        print('Mi cominda favorita es la de tu puta madre')

time.sleep(1)
print('¿Como te puedo ayudar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)