#import ChatBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot=ChatBot('Candid')
#import ListTrainer
bot.set_trainer(ListTrainer)
# Training 
bot.train(['What is your name?', 'My name is Candice'])
bot.train(['Who are you?', 'I am a bot, created by you' ])
