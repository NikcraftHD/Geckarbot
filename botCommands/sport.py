import discord
from discord.ext import commands

class sportCommands(commands.Cog, name="Sport Commands"):
    """Sport related commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kicker", help="Returns frequently used links to kicker.de", pass_context=True)
    async def kicker_table(self, ctx):
        """Returns the kicker.de Bundesliga tables"""
        linklist=("Tabelle Bundesliga: https://www.kicker.de/1-bundesliga/tabelle\n"
                  "Tabelle 2. Bundesliga: https://www.kicker.de/2-bundesliga/tabelle\n"
                  "Tabelle 3. Liga: https://www.kicker.de/3-liga/tabelle\n"
                  "Tabelle AT-Bundesliga: https://www.kicker.de/tipp3-bundesliga/tabelle")
        await ctx.send(linklist)
