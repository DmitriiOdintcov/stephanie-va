import datetime as dt
import random
import pyttsx3 as pyttsx
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import winsound

import Stephanie.configurer as conf

#import pygame.camera
#import wmi

#pygame.camera.init()
#webcam = pygame.camera.Camera(0, (720,360))

#winmgr = wmi.WMI()

engine = None
chatbot = ChatBot('Computer')
chatbot2 = ChatBot('Computer 2')
corpus_trainer = ChatterBotCorpusTrainer(chatbot)
list_trainer = ListTrainer(chatbot)
modules_path = conf.config.abs_mods_filename
user_authorisation = False

def beep():
    winsound.Beep(1500, 600)

affirmative = ["yes", "yeah", "sure", "yah", "ya"]
negative = ["no", "negative", "nah", "na", "nope"]
stop_requests = ["stop","enough","that's enough","cease","silence"]

allow_gibberish = False
wake_up_engine = False
sleeping = False

#global listening
listening = False

additional_names = []#"stupid machine","servant","slave","pathetic program","badly coded abomination"]
invoked_replies = ["What do you require?","How can I help you?","At your service"]
repeat_requests = ["Could you repeat?", "I did not understand, please repeat", "I did not understand that, could you repeat?"]
completed_replies = ["There you go.","Completed!","Request fulfilled."]

def randomPhrase(lst):
    update()
    return random.choice(lst)

def intersection(lst1,lst2):
    update()
    print("intersecting")
    return bool(set(lst1) & set(lst2))

def time_greeting():
    time = dt.datetime.now()
    hour = time.hour
    if hour < 12:
        return 'Good Morning'
    elif 12 <= hour < 18:
        return 'Good Day'
    if hour > 6:
        return 'Good Evening'
        
greetings = ["Hello!","Good to hear you!", time_greeting()]
smalltalk_questions = ["How are you?", "How have you been?", "How was today?","How are you doing?"]

negatives = ["bad","terrible","horrible","horrendous","awful"]
neutrals = ["fine","ok","okay","so-so",]
positives = ["good","great","wonderful","awesome","lovely","fabulous"]

regrets = ["I am sorry to hear that","That is a shame","Do not worry, I am sure the situation will improve"]
congrats = ["I am glad to hear that!", "Congratulations!"]
contents = ["I see"]

def update():
    time_greeting()
    #allow_gibberish = False