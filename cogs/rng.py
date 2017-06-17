from discord.ext import commands
import random
import re as regex

class RNG():
    #initialize class
    def __init__(self, bot):
        self.bot = bot

    #Converts a number to a string in order to display it using emoji
    def convertToString(self, value):
        list = [':zero:',':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:']
        message = ''

        string = str(value)

        for c in string:
            message = message + list[int(c)]

        return message

    @commands.command()
    async def roll(self, message: str = "1d6"):
        """
            Displays a random d6 value.
            Optional parameter allows for rolling dice using XdY dice notation (maximum 20 dice)
            Examples: !roll | !roll 3d10 | !roll 10D4
        """
        pattern = regex.compile('^(\d+)(d|D)(\d+)$')
        if regex.match(pattern, message):
            #Process string to obtain int values
            message = message.replace('D','d')
            numDice, diceValue = message.split('d')
            numDice = int(numDice)
            diceValue = int(diceValue)

            #Limit the maximum number of dice
            if numDice > 20:
                await self.bot.say('Too many dice! Maximum number is 20.')
                return
            else:
                returnMessage = 'Rolled {0}:  '.format(message)

                for i in range(0, numDice - 1):
                    value = random.randint(1, diceValue)
                    returnMessage = returnMessage + self.convertToString(value) + " - "

                #Last value shouldn't display a separator
                value = random.randint(1, diceValue)
                returnMessage = returnMessage + self.convertToString(value)

                await self.bot.say(returnMessage)

        else:
            await self.bot.say('wrong format: {0} Please use dice notation. (XdY)'.format(message))
            return


    #error handler for the poot command
    # @roll.error
    # async def roll_error(self, exc, ctx):
    #     if isinstance(exc, commands.BadArgument):
    #         await self.bot.send_message(ctx.message.channel,'"{0}" is not a valid integer.'.format(ctx.message.content[6:]))


def setup(bot):
    bot.add_cog(RNG(bot))