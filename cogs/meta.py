from discord.ext import commands

class Meta():
    #initialize class
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, *, message: str):
        """
            Copies what you just said.
            It's not rocket science y'know?
        """
        await self.bot.say(message)

    @commands.command()
    async def ping(self):
        """
            Responds to a ping command.
            Yep...it's exactly what you'd expect.
        """
        await self.bot.say('Pong!')

def setup(bot):
    bot.add_cog(Meta(bot))