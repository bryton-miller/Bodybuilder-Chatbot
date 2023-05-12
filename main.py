import discord, openai, json
from webserver import keep_alive

DISCORDTOKEN = 'DISCORD TOKEN HERE'
openai.api_key = 'OPENAPI TOKEN HERE'

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def AIgeneration(inputmessage):
  no = json.dumps(inputmessage)
  response = openai.ChatCompletion.create(model="gpt-4",
                                         messages=[{
                                           "role": "user",
                                           "content": no
                                         }])
  return response.choices[0].message.content

@client.event
async def on_message(message):
  if client.user.mentioned_in(message):
    if message.author == client.user:
      return
    AIprompt = (f'from now on, act like a bodybuilder whose knowledge mainly resides in bodybuilding but is dumb otherwise. Now reply in character: {message.author} Says: {message.content}')
    response = await AIgeneration(AIprompt)
    await message.reply(response)

# this line is for the repl.it server, delete if unnecessary
keep_alive()

client.run(DISCORDTOKEN)
