import discord
import datetime
from discord.ext import commands, tasks
import json
import requests
from discord_keys import SECRET_TOKEN_BOT, SECRET_ID_CHANNEL_TO_SEND_MESSAGE

global events_list
events_list = []

TOKEN_BOT = SECRET_TOKEN_BOT
ID_CHANNEL_TO_SEND_MESSAGE = SECRET_ID_CHANNEL_TO_SEND_MESSAGE


def exec():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print('Bot iniciado!')
        get_events.start()
        post_event.start()

    @bot.command()
    async def hello(ctx):
        await ctx.send('Olá, tudo bem?')

    @tasks.loop(seconds=10)
    async def get_events():
        global events_list
        link = 'http://127.0.0.1:8000/api'
        events = requests.get(link)
        events_list = events.json()

    @tasks.loop(seconds=30)
    async def post_event():
        global events_list
        for event in events_list:
            if event['is_published']:
                now = datetime.datetime.now()
                ajusted_now = f'{now.hour}:{now.minute}:00'
                date = f"{datetime.date(now.year, now.month, now.day)}"
                if ajusted_now == event['event_time'] and date == event['event_date']:
                    channel = bot.get_channel(ID_CHANNEL_TO_SEND_MESSAGE)
                    event_name = event['event_name']
                    await channel.send('@everyone')
                    await channel.send(f'Evento iniciado "{event_name}"')
                    await channel.send(event['event_message'])
            else:
                pass

    bot.run(TOKEN_BOT)


if __name__ == '__main__':
    exec()
