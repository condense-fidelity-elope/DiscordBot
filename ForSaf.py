import discord, math, requests, random, time
from discord.ext import commands
from datetime import datetime

client_token = "NzY5NzE0OTc3MzAwMjgzNDEx.X5TC7w.O6SrhG11aqPRohOW68oxIGlqS3U"
client_hexcolor = 0xF88379

client = commands.Bot(command_prefix="sheeb ")

async def getReddit(subreddit):
    size = 1
    r = requests.get(f"https://api.pushshift.io/reddit/search/submission?subreddit=dankmemes&size=1")
    json = r.json()
    theList = json["data"]
    return theList

@client.event
async def on_ready():
    print("Ready.")
    await client.change_presence(activity=discord.Game(name="bot stuff"))
    activity = discord.Activity(name="with your diharreah", type=discord.ActivityType.watching)

@client.command(aliases=["ping", "p"])
async def _ping(ctx, *args):
    await ctx.send(f"I am {math.floor(client.latency*1000)}ms behind you.")

@client.command(aliases=["define", "urb"])
async def _defines_whatever_you_want(ctx, *args):
    word = " ".join(args)
    r = requests.get(f"http://api.urbandictionary.com/v0/define?term={word}", headers = {'User-agent': "your bot 0.1"})
    json = r.json()
    theList = json["list"]

    e = theList[0]

    definition = e["definition"]
    permalink = e["permalink"]
    thumbs_up = e["thumbs_up"]
    sound_urls = e["sound_urls"]
    author = e["author"]
    word = e["word"]
    defid = e["defid"]
    written_on = e["written_on"]
    example = e["example"]
    thumbs_down = e["thumbs_down"]

    embed = discord.Embed(
        title = word,
        colour = discord.Colour(client_hexcolor),
        url = permalink
    )
    embed.add_field(name="Definition:", value = definition, inline = False)
    embed.add_field(name="Example:", value = example, inline = False)

    embed.set_footer(text=f"{thumbs_up}🔼  |  {thumbs_down}🔽 - Created By {author} - {written_on}")
    await ctx.send(embed=embed)

@client.command(aliases=["reddit", "r"])
async def _reddit(ctx, *args):

    if (len(args) < 1):
        await ctx.send("```incorrect use of command, do >reddit <subreddit>```")
        return

    subreddit = args[0]

    r = requests.get(f"https://reddit.com/r/{subreddit}/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

@client.command(aliases=["searchreddit", "sr"])
async def _searchreddit(ctx, *args):
    if (len(args) < 2):
        await ctx.send("```incorrect use of command, do >searchreddit <subreddit> <search_term>```")
        return

    subreddit = args[0]
    search_term = " ".join(args[1:len(args)])
    amount = 100

    r = requests.get(f"https://api.pushshift.io/reddit/search/submission?subreddit={subreddit}&size={amount}&q={search_term}")
    json = r.json()
    theList = json["data"]

    if len(theList) == 0:
        await ctx.send(f"```None Found with search term \"{search_term}\".```")
        return

    index = random.randint(0, len(theList))

    title = theList[index]["title"]
    description = theList[index]["selftext"]

    url = theList[index]["url"]
    author = theList[index]["author"]
    created_utc = theList[index]["created_utc"]
    score = theList[index]["score"]
    
    embed = discord.Embed(
        title = title,
        description = description[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = url
    )

    embed.set_footer(text=f"{score}🔼 - Created By {author} - {datetime.utcfromtimestamp(created_utc).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

@client.command(aliases=["meme", "m"])
async def _meme(ctx, *args):
    r = requests.get(f"https://reddit.com/r/dankmemes/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

@client.command(aliases=["dadjoke", "dj"])
async def _dadjoke(ctx, *args):
    r = requests.get(f"https://reddit.com/r/dadjokes/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

@client.command(aliases=["stuff", "sf"])
async def _stuff(ctx, *args):
    r = requests.get(f"https://reddit.com/r/ComedyNecrophilia/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

@client.command(aliases=["bleach", "eb"])
async def _bleach(ctx, *args):
    r = requests.get(f"https://reddit.com/r/eyebleach/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

@client.command(aliases=["wholesome", "ws"])
async def _wholesome(ctx, *args):
    r = requests.get(f"https://reddit.com/r/wholesomememes/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)
    
    
@client.command(aliases=["fart", "ft"])
async def _fart(ctx, *args):
    r = requests.get(f"https://reddit.com/r/fart/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)

@client.command(aliases=["gangsta", "gt"])
async def _gangsta(ctx, *args):
    r = requests.get(f"https://reddit.com/r/whothefuckup/random/.json", headers = {'User-agent': "your bot 0.1"})
    json = r.json()

    try:
        theList = json["data"]
    except:
        theList = json[0]["data"]

    author = theList["children"][0]["data"]["author"]
    title = theList["children"][0]["data"]["title"]
    selftext = theList["children"][0]["data"]["selftext"]
    image = theList["children"][0]["data"]["url"]
    up_votes = theList["children"][0]["data"]["ups"]
    link = "https://reddit.com"+theList["children"][0]["data"]["permalink"]
    nsfw = theList["children"][0]["data"]["over_18"]
    created = theList["children"][0]["data"]["created"]

    embed = discord.Embed(
        title = title,
        description = selftext[0:2048],
        colour = discord.Colour(client_hexcolor),
        url = link
    )

    embed.set_image(url=image)
    embed.set_footer(text=f"{up_votes}🔼 - Created By {author} - {datetime.utcfromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')}")
    await ctx.send(embed=embed)


client.run(client_token)
