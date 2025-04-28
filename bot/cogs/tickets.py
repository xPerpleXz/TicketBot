import discord
from discord.ext import commands
from discord import app_commands
from utils.database import get_ticket_config, save_ticket

class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ticket", description="Öffnet ein neues Ticket")
    async def ticket(self, interaction: discord.Interaction):
        config = await get_ticket_config(interaction.guild.id)
        category = interaction.guild.get_channel(config['ticket_category_id'])
        
        ticket_channel = await category.create_text_channel(name=f"ticket-{interaction.user.name}")
        await save_ticket(ticket_channel.id, interaction.user.id)

        await ticket_channel.send(f"Willkommen {interaction.user.mention}. Support kommt gleich.")
        await interaction.response.send_message(f"Ticket erstellt: {ticket_channel.mention}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Tickets(bot))
