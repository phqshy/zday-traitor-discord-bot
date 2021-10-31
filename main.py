import nationstates
from nationstates import Shard
import time
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='=', help_command=None)

traitors = []

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="=help"))
    print('bot online')

@bot.command()
async def startBot(ctx):
    await ctx.send("Bot started!")
    while True:
        api = nationstates.Nationstates("The Yeetusa (CCD)")
        ccd = api.region("confederation_of_corrupt_dictators")
        data = ccd.nations
        count = 0
        for i in ccd.nations:
            count+=1
            e = str(i)
            nation1 = e[9:]
            nation1 = nation1[:-19]
            zdata = nationstates.Shard("zombie", view="nation.{}".format(nation1))
            r = api.nation(nation1).get_shards(zdata)
            r = str(r)
            if "export" in r:
                if nation1 in traitors:
                    pass
                else:
                    traitors.append(nation1)
                    await ctx.send(nation1 + " is embracing zombies @everyone")
            elif "exterminate" in r:
                if nation1 in traitors:
                    pass
                else:
                    traitors.append(nation1)
                    await ctx.send(nation1 + " is exterminating zombies @everyone")
            else:
                if nation1 in traitors:
                    traitors.pop(traitors.index(nation1))
                print(count)
        channel = bot.get_channel(904358370243395616)
        await channel.send(traitors)


bot.run('Nzg1ODU1NDMzNDc4NzY2NjMy.X8965w.qmrwyPu7nCL_xn-9-xe6knWHWtY')
