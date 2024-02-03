import pyttsx3  
# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech  
text = "Hello, Rupesh you are the Genius and you born on the earth to do something big."  
engine.say(text)  
# play the speech  
engine.runAndWait()