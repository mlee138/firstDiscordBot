import discord
import random
import os
from dotenv import load_dotenv

load_dotenv('./venv/.env')

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

checklists = {}


def handle_checklist(message, author):
    _, action, *rest = message.split(" ")
    value = " ".join(rest) if len(rest) >= 0 else ""

    if author not in checklists:
        checklists[author] = []

    if action == "help":
        return """```AVAILABLE ACTIONS
        view
        add <item>
        completed <item number>
        delete <item number>
        clear 
        ```"""
    elif action == "view":
        if len(checklists[author]) == 0:
            return "```no items in your checklist```"
        list_str = ""
        for i in range(len(checklists[author])):
            list_str += f'{i}. {checklists[author][i]}\n'
        # list_str = f'```{list_str}```'
        return list_str
    elif action == "add" and value:
        checklists[author].append(value)
        return "```successfully added to checklist```"
    elif action == "complete" and value:
        checklists[author][int(value)] = f'~~{checklists[author][int(value)]}~~'
        return "```item has been marked as completed```"
    # elif action == "" and value:
    #     checklists[author][value] = f'~~${checklists[author][value]}~~'
    #     return "item has been marked as completed"
    elif action == "delete" and value:
        checklists[author].remove(checklists[author][int(value)])
        return "```deleted item from checklist```"
    elif action == "clear":
        checklists[author] = []
        return "```cleared checklist```"
    else:
        return f'{action} is not recognized or was used incorrectly'


# on_ready: called when the bot is started
@client.event
async def on_ready():
    print('{0.user} has connected to Discord!'.format(client))


@client.event
async def on_message(message):
    author = str(message.author)
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    # if the bot sent the message, return
    if message.author == client.user:
        return
    if message.channel.name == 'discord-bot-channel':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye {username}')
            return
        elif user_message.lower() == 'random':
            response = f'random number: {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.split(" ")[0] == '!checklist':
            response = handle_checklist(user_message, author)
            await message.channel.send(response)
            return

    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return


client.run(TOKEN)