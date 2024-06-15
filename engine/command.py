import pyttsx3
import speech_recognition as sr
import eel
import re
import time
# from gtts import gTTS
# import os

voice_query = []

def speak(text):
    text = str(text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 180)
    print(voices)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

# def speak(text):
#     text = str(text)
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     for voice in voices:
#         if 'vi' in voice.languages:
#             engine.setProperty('voice', voice.id)
#             break
#     engine.setProperty('rate', 180)
#     engine.say(text)
#     eel.DisplayMessage(text)
#     eel.receiverText(text)
#     engine.runAndWait()

def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        eel.DisplayMessage("Listening....")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, 10, 6)
    try:
        print("Recognizing")
        eel.DisplayMessage("Recognizing....")
        query = recognizer.recognize_google(audio, language='en-vi')
        print(f"You Said: {query}")
        eel.DisplayMessage(query)
    except Exception as ex:
        print("sorry, could not recognize")
        return ""

    return query.lower()


@eel.expose
def allCommands(message=1):
    global voice_query

    if (message == 1):
        query = takeCommand()
        voice_query.append(str(query))
        print(query)
        eel.senderText(query)
    else:
        query = message
        voice_query.append(str(query))
        eel.senderText(query)
    try:
        if "open" in query:
            from engine.feature import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.feature import PlayYoutube
            PlayYoutube(query)
        elif "stop" in query or "pause" in query or "continue" in query:
            from engine.feature import conPauseYoutubeVideo
            conPauseYoutubeVideo(query)
        elif "skip" in query or "rewind" in query:
            from engine.feature import skipRewindYoutubeVideo
            numbers = re.findall(r'\d+', query)
            number = 5
            if numbers:
                number = int(numbers[0])
            skipRewindYoutubeVideo(number, query)
        elif "volume" in query:
            from engine.feature import volumeDownUp
            numbers = re.findall(r'\d+', query)
            change = 15
            if numbers:
                change = int(numbers[0])
            volumeDownUp(change, query)
        elif "translate" in query:
            from engine.feature import translateLanguage
            voice_query = [element for element in voice_query if "translate" not in element]
            if len(voice_query) > 1:
                element = voice_query[-2]
            else:
                element = voice_query[-1]
            translateLanguage(element)
        elif "google" in query:
            from engine.feature import SearchGoogle
            query = takeCommand().lower()
            SearchGoogle(query)
        elif "wikipedia" in query:
            from engine.feature import SearchWikipedia
            query = takeCommand().lower()
            SearchWikipedia(query)
        elif "hello" in query or "hi" in query:
            speak("Hello sir, how are you?")
        elif "temperature" in query or "weather" in query:
            from engine.feature import temperatureSearch
            temperatureSearch(query)
        elif "time" in query or "date" in query:
            from engine.feature import getCurrentDateTime
            getCurrentDateTime(query)
        else:
            from engine.feature import chatBot
            chatBot(query)
    except Exception as e:
        print(f"Error {e}")
    eel.ShowHood()
