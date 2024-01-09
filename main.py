from asgiref.sync import sync_to_async
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
        channel = bot.get_channel(ID_CHANNEL_TO_SEND_MESSAGE)
        # await channel.send('@here')
        await channel.send('Salve!')

    @tasks.loop(seconds=10)
    async def birthday():
        events = await sync_to_async(Event.objects.filter(is_published=True))
        for i in events:
            now = datetime.datetime.now()
            # time = datetime.time(hour=1, minute=27, second=now.second, microsecond=now.microsecond)
            # date = datetime.date(day=10, month=12, year=now.year)
            if now.time() == i.event_time and now.date() == i.event_date:
                channel = bot.get_channel(ID_CHANNEL_TO_SEND_MESSAGE)
                await channel.send('Parabéns Corno!!!')

    bot.run(TOKEN_BOT)


if __name__ == '__main__':
    asyncio.run(exec())
