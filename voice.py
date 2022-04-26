import pyttsx3
class voice:
    
    def speak(query):
        engine = pyttsx3.init()
        voices= engine.getProperty('voices') 
        engine.setProperty('voice', voices[1].id)
        engine.say(query)
        engine.runAndWait()

query = "9"
voice.speak(query)