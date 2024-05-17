from typing import Final
import os
import certifi
from dotenv import load_dotenv
from discord import Intents,Client, Message
import discord
import asyncio
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True 
intents.presences = True
intents.members = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    is_private = user_message[0]
    if is_private in '?':
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        if is_private == '?':
            await message.author.send(response) 
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message:Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message:str = message.content
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')
    if user_message == 'hi':
        
        for member in message.guild.members:
            await message.channel.send(f'{member}')
            await asyncio.sleep(1)
            if member.activity:
                await message.channel.send(f'{member.name} is playing {member.activity.name}')
            else:
                await message.channel.send(f'{member.name} is not playing anything')
    else:
        await send_message(message, user_message)

def main() -> None:
    os.environ["SSL_CERT_FILE"] = certifi.where()
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()