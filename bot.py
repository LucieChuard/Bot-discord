import discord

salutation=["Hello","hello", "Bonjour", "bonjour", "bjr", "slt", "Bjr", "Slt", "hi", "Hi" ]
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        #await self.change_presence(activity=discord.Streaming(name="GameNWatch", url="twitch.tv/sharwina_gameNWatch")) --> tentative affichage en live
        print('------')



    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content in salutation :
            await message.channel.send('Hello {0.author.mention}'.format(message) +" :)")

    async def on_member_join (member):
        print ("Bienvenue {0.author.mention}!")

#réaction déclanchée sur une réaction
    async def on_reaction_add(emoji):
        emoji = "{SharwiHii}"
        await reaction.message (emoji)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA4MzAwNTM0NDMyNzkyOTg3Nw.Ghyagr.k5riYex9-LOnbrEeFpnviEzQ3YOApbjaqWF_A8')