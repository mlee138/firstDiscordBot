import discord
import random

TOKEN = "ODg3Nzk4OTAwNzc2MzgyNTA0.YUJZKA.9K_rTtOnbFXg5ig2wTIPju26Xgs"

client = discord.Client()


# on_ready: called when the bot is started
@client.event
async def on_ready():
    print('{0.user} has connected to Discord!'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

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

    if user_message.lower() == "!anywhere":
        await message.channel.send("This can be used anywhere!")
        return


client.run(TOKEN)