import discord
import time
from discord.ext import commands
import random
import asyncio
import g4f
client=g4f.client.Client()
config = {
    'token': '[insert token]',
    'prefix': '',
}
intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
bot = commands.Bot(command_prefix=config['prefix'], intents = intents)
with open('memory.txt', 'r') as file:
    messages = file.read().replace('\n', '').split()
file.close()
@bot.event
async def on_message(ctx):
    if ctx.author != bot.user:
        if ctx.content == "/list":
            await ctx.reply(messages)
        else:
            if ctx.content == "/reset":
                messages.clear()
                await reply("cleared data base")
            else:
                if ctx.content == "/randomn":
                    r = random.randint(1, 100)
                    await ctx.reply(r)
                else:
                    file = open("memory.txt", "a")
                    new = ctx.content
                    lst = new.split(" ")
                    addingstep=0
                    while addingstep < len(lst):
                         messages.append(lst[addingstep])
                         file.write(lst[addingstep]+" ")
                         addingstep=addingstep+1
                    leng = len(messages)
                    leng += -1
                    wordamount=random.randint(1,10)
                    repeatdef = []
                    wordstep=0
                    reply=""
                    while wordstep < wordamount:
                        index = random.randint(1, leng)
                        if not messages[index] in repeatdef:
                            repeatdef.append(messages[index])
                            reply = reply + " " + messages[index]
                            wordstep=wordstep+1
                    file.close()
                    if random.randint(1,1000)==1000:
                        reply="https://cdn.discordapp.com/attachments/1244567071577084026/1266674912945373205/attachment-1.gif?ex=66c5a670&is=66c454f0&hm=aa9fb517d8cc63724fb6cd3656127f29ed5fa7937b1d11cb8450b24b79ee0d91&"
                    response = client.chat.completions.create(provider=g4f.Provider.Blackbox,model="blackbox",messages=[{"role": "user", "content": ctx.content}])
                    await asyncio.sleep(0)
                    try:
                        await ctx.reply(response.choices[0].message.content)
                    except:
                        await ctx.reply("Error!")


            

bot.run(config['token'])
