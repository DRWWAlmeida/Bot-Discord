from channels.db import database_sync_to_async
import asyncio
import discord
import datetime
from discord.ext import commands, tasks
from discord_keys import SECRET_TOKEN_BOT, SECRET_ID_CHANNEL_TO_SEND_MESSAGE
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "discordbot.settings")
django.setup()
from web.models import Event

TOKEN_BOT = SECRET_TOKEN_BOT
ID_CHANNEL_TO_SEND_MESSAGE = SECRET_ID_CHANNEL_TO_SEND_MESSAGE


@database_sync_to_async
def get_events():
    return list(Event.objects.filter(is_published=True))


def exec():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print('Bot iniciado!')
        task_test.start()
        birthday.start()

    @bot.command()
    async def hello(ctx):
        await ctx.send('Olá, tudo bem?')

    @tasks.loop(seconds=60)
    async def task_test():
        # channel = bot.get_channel(ID_CHANNEL_TO_SEND_MESSAGE)
        # await channel.send('@here')
        # await channel.send('Salve!')
        print('test')

    @tasks.loop(seconds=30)
    async def birthday():
        events = await get_events()
        for i in events:
            now = datetime.datetime.now()
            ajusted_now = datetime.time(hour=now.hour, minute=now.minute)
            if ajusted_now == i.event_time and now.date() == i.event_date:
                channel = bot.get_channel(ID_CHANNEL_TO_SEND_MESSAGE)
                await channel.send('@everyone')
                await channel.send(f'Evento iniciado "{i.event_name}"')
                # await channel.send(f'Event by {i.author}')
                await channel.send(i.event_message)

    bot.run(TOKEN_BOT)


if __name__ == '__main__':
    asyncio.run(exec())
