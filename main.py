from discord import Client, File
#get token from env
from os import getenv
from replit import db
import count
from keep_alive import keep_alive
import config

def clean_msg(msg):
  msg=msg.strip()
  msg=msg.lower()
  return msg

print("starting...")
keep_alive()
print("server running...")

client = Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg=clean_msg(message.content)
    if message.author == client.user:
      return
    if(config.is_config_msg(msg)):
      await message.channel.send(config.apply_config_msg(message), reference=message, mention_author=False)
    if (str(message.channel)!=db.get("CONFINED_CHANNEL") and db.get("CONFINED_CHANNEL")!=""):
      print("private msg")
      return
    
    #print(msg)

    if("fotomiku" in msg):
      with open('images/snale.png', 'rb') as f:
        picture = File(f)
        await message.channel.send(file=picture)
      print("fotomiku")
      #await message.channel.send(file=File('images/miku.jpeg'))
      #await message.channel.send('nyan nyaa :3', reference=message, mention_author=False)
    
    if('miau' in msg):
      print("miau")
      await message.channel.send('nyan nyaa :3', reference=message, mention_author=False)

    if (count.is_count_msg(msg)):
      print("número")
      await message.channel.send('número', reference=message, mention_author=False)

    if (count.is_roman_number(msg)):
      print("número romano")
      await message.channel.send('número romano {0}'.format(count.roman_to_int(msg)), reference=message, mention_author=False)

client.run(getenv('TOKEN'))
