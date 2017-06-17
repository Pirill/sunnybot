from discord.ext import commands
import logging
import json

#initiates logging
logging.basicConfig(level=logging.INFO)

#Command prefix
prefix = ['!', '\N{HEAVY EXCLAMATION MARK SYMBOL}']
#Bot description
description = """Hello! I am a Sunnybot! Best bot!"""
#Creates the bot
bot = commands.Bot(command_prefix=prefix, description=description)

#Extension names
startup_extensions = [
    'cogs.meta',
    'cogs.rng',
]

#Generic error handler event
#@bot.event
#async def on_command_error(error, ctx):
#    if isinstance(error, commands.CommandNotFound):
#        await bot.send_message(ctx.message.channel,'"{0}" is not a valid bot command. Use !help to see available commands.'.format(ctx.message.content))


#Message event
@bot.event
async def on_message(message):
    #Bot shouldn't reply to itself
    if message.author == bot.user:
        return
    #Processes commands
    await bot.process_commands(message)


#Login event
@bot.event
async def on_ready():
    print('Logged in as:')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')


@bot.command(hidden=True)
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))


@bot.command(hidden=True)
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

#If this is the main module
if __name__ == "__main__":
    #Loads the bot token from a JSON file
    with open('credentials.json') as f:
        credentials = json.load(f)

    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(credentials['token'])