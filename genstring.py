# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki

# Credits to Akshay


from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c("Alexa", api_id=API_ID, api_hash=API_HASH, in_memory=True)

with i:
    ss = i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")
