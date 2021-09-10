import pyttsx3  #importing pyttsx3 library

textToSpeech = pyttsx3.init() #initializing the library

text=input("enter the text: ") #taking the text input from the user
textToSpeech.say("text")#say fuction to convert the text to speech
textToSpeech.runAndWait()




