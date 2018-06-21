import discord
import json

bot = discord.Client()
with open('secrets.json') as f:
	secrets = json.load(f)

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
		await bot.send_message(message.channel, "nya")

bot.run(secrets["bot"]["token"])
