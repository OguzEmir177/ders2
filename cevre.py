import discord
from discord.ext import commands
import random
from bilgiler import *


intents = discord.Intents().all()  
bot = commands.Bot(command_prefix='#', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to Discord!')


@bot.event
async def on_message(message):
    
    if message.author.bot:
        return

    
    if message.content.startswith('!cevrekirliligi'):
        responses = [
            "Çevre kirliliğini önlemek için şu adımları izleyebiliriz:\n"
            "1. Daha az plastik kullanarak çevreye zarar veren atıkları azaltabiliriz.\n"
            "2. Enerji tasarruflu cihazlar kullanarak enerji tüketimini azaltabiliriz.\n"
            "3. Düzenli olarak çöpleri geri dönüştürerek kaynakları koruyabiliriz.",
            "Çevre kirliliğini önlemek için doğal kaynakları korumak önemlidir."
        ]
        response = random.choice(responses)
        await message.channel.send(response)
    elif message.content.startswith('!cevremizitemiztutalım'):
        responses = [
            "Çevremizi temiz tutmanın yolları şunlar olabilir:\n"
            "1. Dışarıda piknik yaparken çöpleri toplamak ve uygun şekilde atmak.\n"
            "2. Kendi kullan-at ürünlerini azaltarak çöp miktarını azaltmak.\n"
            "3. Düzenli olarak doğa temizliği etkinliklerine katılmak.",
            "Çevremizi temiz tutmak hepimizin sorumluluğundadır."
        ]
        response = random.choice(responses)
        await message.channel.send(response)


bot.run(token)
