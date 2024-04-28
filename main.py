import os
import eel

from engine.feature import *
from engine.command import *
from llm_chains import load_normal_chain
from langchain.memory import StreamlitChatMessageHistory

def load_chain(chat_history): 
    return load_normal_chain(chat_history)

def start(): 
    eel.init('www')

    chat_history = StreamlitChatMessageHistory(key="history")

    playAssistantSound()

    if chat_history.messages != []:
        for message in chat_history.messages:
            return
        

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)