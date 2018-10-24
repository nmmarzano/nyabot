import discord
import json
import random

bot = discord.Client()
with open('secrets.json') as f:
	secrets = json.load(f)
with open('nya.json') as f:
	nyas = json.load(f)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print("Nyabot running. Press Ctrl+C to quit.")
	print('------')

@bot.event
async def on_message(message):
	if "nya" in message.content and message.author.id != secrets["client"]["id"]:
		await bot.send_message(message.channel, nyas[random.randint(0,len(nyas)-1)])

bot.run(secrets["bot"]["token"])
