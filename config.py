from replit import db

help=\
"""
!nya help: returns help
!nya restrict: the bot will ignore messages from outside this channel
!nya unrestrict: the bot will read messages everywhere
!nya channel: replies with the current restricted channel
"""

def is_config_msg(s):
  return s.startswith('!nya')

def apply_config_msg(msg):
  print(msg)
  s=msg.content.split()
  if(s[1]=="help"):
    return help
  if(s[1]=="restrict"):
    db["CONFINED_CHANNEL"] = str(msg.channel)
    print(db["CONFINED_CHANNEL"])
    return "I will ignore messages from outside this channel"
  if(s[1]=="unrestrict"):
    db["CONFINED_CHANNEL"] = ""
    print(db["CONFINED_CHANNEL"])
    return "I will read all messages from this server"
  if(s[1]=="channel"):
    if(len(db["CONFINED_CHANNEL"])==0):
      return "I can read all messages from this server"
      
    return "my channel is "+db["CONFINED_CHANNEL"]