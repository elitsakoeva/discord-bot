import discord
from discord.ext import commands 
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event 
async def on_ready():
    print("Logged in as {bot.user}")

    await bot.change_presence(
        status = discord.Status.online,
    )

    try:
        synced = await bot.tree.sync()
        print(f"Sync slash cmd: {len(synced)}")
    except Exception as e:
        print(e)

bot.run(TOKEN)
