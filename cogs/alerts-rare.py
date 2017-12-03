import discord
from discord.ext import commands

class Quotes:

    def __init__(self, bot):
        self.bot = bot
    async def on_message(self, message):
        msg = message.clean_content.lower()
        
        if message.channel.id in [263032521325936642]:
            channel2 = self.bot.get_channel(335838871205969920)
            await self.bot.send_message(channel2, msg)

def setup(bot):
    bot.add_cog(Quotes(bot))