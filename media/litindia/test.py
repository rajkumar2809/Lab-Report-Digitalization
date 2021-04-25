import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
 
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    '''if os.path.exists('audio.mp3'):
        #os.system('dir audio.mp3')
        print ('file is deleted')'''
    tts.save("audio.mp3")
    os.system("start audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    source = sr.Microphone()
    speak("Say something!")
    audio = r.listen(source)
    source.close()
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def litindia(data):
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
#time.sleep(2)
#speak("Hi Sritam, what can I do for you?")
while 1:
    data = recordAudio()
    litindia(data)
    break
