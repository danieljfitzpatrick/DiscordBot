# bot.py
import os
import sqlite3
import discord

from dotenv import load_dotenv
from dateutil.parser import parse

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class MyClient(discord.Client):
    async def on_ready(self):
        self.conn = sqlite3.connect('reminders.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS reminders (date text, content text, repeat integer)''')
        self.conn.close()
        print(self.user)

    async def on_message(self, message):
        response = ""
        if message.content[0] == '!':
            if message.channel.name == "reminders":
                if "!RemindMe" in message.content:
                    _date, content = self.parse_remind_me(message.content.replace("!RemindMe ", ""))
                    self.conn = sqlite3.connect('reminders.db')
                    self.conn.execute("INSERT INTO reminders VALUES (?, ?, ?)", (_date, content, 0))
                    self.conn.commit()
                    response = "Reminder set for " + str(_date)
                    cursor = self.conn.execute("SELECT * FROM reminders")
                    for row in cursor:
                        print(row)
                    self.conn.close()
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
    
    def schedule():
        thre
        
        
        
        

client = MyClient()
client.run(TOKEN)
