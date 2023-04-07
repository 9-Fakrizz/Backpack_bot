import discord
import os
import requests
import json
import random
#import discord.voice_client
from replit import db
from keeping import keep_alive
from discord.ext import commands
from discord import FFmpegPCMAudio
import time

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '~', intents=intents)


bad_word = []
good_Word =["โลกนี้จะเจ๋งขึ้นถ้ามีคนอย่างคุณ!", "คนโง่ย่อมแสดงออกโง่ๆ", "ควายเป็นสัตว์ที่มหัศจรรย์ชนิดหนึ่ง!", "ผมอยู่ข้างคุณเสมอ","โอ้ว!! คุณดูฉลาดสุดๆ", "น่ารักที่สุด~", "<3","จำเป็นต้องรู้ไหมนะ~",".....","แล้วไง ?","ถามจริง!","เหนื่อยไหม ถามจริง ?", "หว้ายยย~" ,"แน่ใจอ่อ ?","5555","แหวะ~","อี๋~"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "  [{}]  ".format(json_data[0]['a'])
  return(quote)


def delete_word(index):
  good_Word = db["good_Word"]
  if len(good_Word) > index :
    del good_Word[index]
    db["good_Word"] = good_Word

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
  await client.process_commands(message)
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('~hello'):
    await message.channel.send('(FAK) study: 02:34:59 hr')


  if msg.startswith('~inspire'):
    quote = get_quote()
    await message.channel.send(quote)

    
  if any(word in msg for word in bad_word):
   await message.channel.send(random.choice(good_Word))

@client.command(pass_context = True)
async def join(ctx):
  await ctx.send("almost")
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You are not in a voice channel")

@client.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.send("im not in vc")
    await ctx.guild.voice_client.disconnect()

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command()
async def s(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    source = FFmpegPCMAudio('Sound/nacom.mp3')
    player = vc.play(source)
    await ctx.message.delete()
    time.sleep(3)
    await vc.disconnect()
  else :
    await ctx.send("Go to some voice channel first?")

@client.command()
async def q(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    source = FFmpegPCMAudio('Sound/summertime.mp3')
    player = vc.play(source)
    await ctx.message.delete()

  else :
    await ctx.send("Go to some voice channel first?")

  
 



keep_alive()
client.run(os.environ['token'])