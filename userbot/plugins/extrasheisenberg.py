from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"^.yo$", outgoing=True))
async def yo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)	


@borg.on(events.NewMessage(pattern=r"^.oof$", outgoing=True))
async def yo(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)		      


@borg.on(events.NewMessage(pattern=r"^.noice$", outgoing=True))
async def noice(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.fwd_from:
            return
        message_id = e.message.id
        if e.reply_to_msg_id:
            message_id = e.reply_to_msg_id
        await e.client.send_message(
            e.chat_id,
            file="https://media.giphy.com/media/yJFeycRK2DB4c/giphy.gif"
        )
        await e.delete()		      


@borg.on(events.NewMessage(pattern=r"^.lol$", outgoing=True))
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("L😂L")


@borg.on(events.NewMessage(pattern=r"^.alol$", outgoing=True))	
async def alol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = "L😂L"
        for j in range(15):
            t = "L🤣L" if j%2==0 else "L😂L"
            await e.edit(t)
		

@borg.on(events.NewMessage(pattern=r"^.nice$", outgoing=True))
async def nice(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Noice")
	
	
@borg.on(events.NewMessage(pattern=r"^.p$", outgoing=True))
async def p(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Participate is giveaways.")	

	
@borg.on(events.NewMessage(pattern=r"^.w$", outgoing=True))
async def w(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Wait for results.")	


@borg.on(events.NewMessage(pattern=r"^.b$", outgoing=True))
async def b(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Better luck next time.")	
	
	
	
@borg.on(events.NewMessage(pattern=r"^.mm$", outgoing=True))
async def mm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.fwd_from:
            return
        message_id = e.message.id
        if e.reply_to_msg_id:
            message_id = e.reply_to_msg_id
        await e.client.send_message(
            e.chat_id,
            file="https://telegra.ph/file/2f132c4536670dd0d7dce.jpg"
        )
        await e.delete()		   
