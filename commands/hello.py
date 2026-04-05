import discord
from discord import app_commands

def setup(bot):
    @bot.tree.command(name="hello", description='Says hello.')
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")