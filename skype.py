from skpy import Skype, SkypeGroupChat, SkypeSingleChat
import sys
from dotenv import load_dotenv
import os
load_dotenv()
USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASS')

sk = Skype(USERNAME, PASSWORD, "token") # connect to Skype

print(f"Logged in as{sk.userId}")
print(sys.argv)

#groupname

#sk.user # you
#sk.contacts # your contacts
#sk.chats # your conversations

#ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
#ch = sk.chats["8:testing"] # 1-to-1 conversation
#for contact in sk.chats.recent():
    #print(contact) 

#ch.sendMsg('this is automated test msgs') # plain-text message
#ch.sendFile(open("song.mp3", "rb"), "song.mp3") # file upload
#ch.sendContact(sk.contacts["daisy.5"]) # contact sharing

#ch.getMsgs() # retrieve recent messages
#user
#pass
#group name
#msg
def list_chat_ids():
    chats = sk.chats.recent()
    for chat_id, chat in chats.items():
        if isinstance(chat, SkypeSingleChat):
            print(f"Chat ID: {chat_id}, Chat with:  {chat.userId}")
        elif isinstance(chat, SkypeGroupChat):
            print(f"Chat ID: {chat_id}, Group Chat with:  {chat.topic}")


def find_group_id(groupName):
    chats = sk.chats.recent()
    for chat_id, chat in chats.items():
        if isinstance(chat, SkypeGroupChat):
            if (chat.topic == groupName):
                return chat_id
            
        
#list_chat_ids()
import argparse
def send_msg_to_group(chat_id, msg):
    #print(f"Chat ID:{chat_id}")
    #print(f"Message:{msg}")
    chat = sk.chats[chat_id]
    #print(chat)
    chat.sendMsg(msg)

groupId = find_group_id(sys.argv[1])
myMsg = sys.argv[2]

send_msg_to_group(groupId, myMsg.replace('\\n', '\n'))
#[group name, message]
#how to call python .\skype.py 'testingqqq' 'helllo \n sadjasd'