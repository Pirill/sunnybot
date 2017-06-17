from discord.ext import commands
import random
import re

class RNG():
    #initialize class
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, message: str = "1d6"):
        """
            Displays a random die value.
            Optional parameter allows for rolling of more dice (maximum 20).
            Examples: !roll | !roll 3
        """

        pattern = re.compile('^(\d+)d(\d+)$')
        if re.match(pattern, message):
            await self.bot.say('correct format: {0}'.format(message))
        else:
            await self.bot.say('wrong format: {0}'.format(message))

       # if dice < 1 or dice > 20:
       #     await self.bot.say('Invalid number of dice.')
       #     return
       #
       # for i in range(0, dice):
       #     message = message + random.choice([
       #        ":one:,",":two:,",":three:,",":four:,",":five:,",":six:,"
       #     ])


    #error handler for the poot command
    # @roll.error
    # async def roll_error(self, exc, ctx):
    #     if isinstance(exc, commands.BadArgument):
    #         await self.bot.send_message(ctx.message.channel,'"{0}" is not a valid integer.'.format(ctx.message.content[6:]))


def setup(bot):
    bot.add_cog(RNG(bot))