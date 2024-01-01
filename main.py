import discord
import datetime
from discord.ext import commands, tasks
from discord_keys import SECRET_TOKEN_BOT, SECRET_ID_CHANNEL_TO_SEND_MESSAGE

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
        await channel.send('Olá a todos!')

    @tasks.loop(seconds=1)
    async def birthday():
        now = datetime.datetime.now()
        time = datetime.time(hour=1, minute=27, second=now.second, microsecond=now.microsecond)
        date = datetime.date(day=10, month=12, year=now.year)
        if now.time() == time and now.date() == date:
            channel = bot.get_channel(ID_CHANNEL_TO_SEND_MESSAGE)
            await channel.send('Parabéns Corno!!!')

    bot.run(TOKEN_BOT)


if __name__ == '__main__':
    exec()
