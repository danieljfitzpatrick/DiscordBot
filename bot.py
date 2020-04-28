# bot.py
import os

import discord
from dotenv import load_dotenv
from dateutil.parser import parse

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class MyClient(discord.Client):
    async def on_ready(self):
        print(self.user)

    async def on_message(self, message):
        response = ""
        if message.content[0] == '!':
            if message.channel.name == "reminders":
                if "!RemindMe" in message.content:
                    _date, content = self.parse_remind_me(message.content.replace("!RemindMe ", ""))
                    response = "Reminder set for " + str(_date)
                else:
                    response = "Unknown Command"
                
                await message.channel.send(response)

    def parse_remind_me(self, message):
        words = message.split(" ")
        content = ""
        try:
            _date = parse(words[0] + " " + words[1])
            content = " ".join(words[2:])
        except:
            _date = "Error: Invalid Date"
        
       
        return _date, content
        
        
        
        

client = MyClient()
client.run(TOKEN)
