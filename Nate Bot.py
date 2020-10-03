import discord, random, linecache, itertools
from discord.ext import commands

bot = commands.Bot(command_prefix = '/')

Natelib = 'nate_individual.txt'
linenum = sum(1 for line in open(Natelib,'r',encoding='utf8'))
# print(linenum)

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    
    triggers ='nate honey thoughts? feel? bet think?'
    triggers = triggers.split()
    # print(triggers)

    text = message.content.lower().split()
    # print(text)
    numdif = (len(text)+len(triggers)-len(Diff(text,triggers)))/2
    #print(numdif)

    if numdif > 0:
        responses = linecache.getline(Natelib, random.randrange(0,linenum))
        print(random.randrange(0,linenum))
        await message.channel.send(responses)

@bot.command(name='gay', help='Responds with the latency of the server')
async def gay(ctx):
    await ctx.channel.send(f'what up kid, the lag is {round(bot.latency * 1000)}ms')

@bot.command(aliases=['8ball','test'], help='Gives an 8ball reponse to a given question')
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.','Ask again later.','Better not tell you now.','Cannot predict now.''Concentrate and ask again.','Don’t count on it.','It is certain.','It is decidedly so.',
        'Most likely.','My reply is no.','My sources say no.','Outlook not so good.','Outlook good.','Reply hazy, try again.','Signs point to yes.','Very doubtful.','Without a doubt.',
        'Yes.','Yes – definitely.','You may rely on it.']
        
    await ctx.channel.send(f'question: {question}\nAnswer: {random.choice(responses)}')

@bot.command()
async def clear(ctx, amount=5, help='will clear N previous lines in chat'):
    await ctx.channel.purge(limit=amount+1)

bot.run('NzYxNDU1NDMxNTc4MTU3MDY3.X3a2og.-yJTsioc_Gh_7Jlo2dkYc0x9SJc')