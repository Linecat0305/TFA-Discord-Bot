import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import logger

# 機器人
intent = discord.Intents.default()
bot = commands.Bot(intent=intent, help_command=None)
# 常用物件、變數
base_dir = os.path.abspath(os.path.dirname(__file__))
# 載入TOKEN
load_dotenv(dotenv_path=os.path.join(base_dir, "TOKEN.env"))
TOKEN = str(os.getenv("TOKEN"))

# 建立logger
real_logger = logger.CreateLogger()
bot.logger = real_logger


bot.load_extensions("cogs.role_giver")
bot.run(TOKEN)
