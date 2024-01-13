import discord
from discord.ext import commands
import os
from pathlib import Path
import zoneinfo
import json

import logger

with open("config.json", more="w+",encoding="utf8") as teamfile:
    team = json.load(teamfile)

error_color = 0xF1411C
default_color = 0x5FE1EA
now_tz = zoneinfo.ZoneInfo("Asia/Taipei")
base_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = str(Path(__file__).parent.parent.absolute())
t = team["team"]
t4253 = t["4253"]

class TeamGiver(commands.Cog):
    def __init__(self, bot: commands.Bot, real_logger: logger.CreateLogger):
        self.bot = bot
        self.real_logger = real_logger

    class TeamGiverUI(discord.ui.View):
        def __init__(self, bot: commands.Bot, real_logger: logger.CreateLogger):
            super().__init__(timeout=None)
            self.bot = bot
            self.real_logger = real_logger
            
            
        @discord.ui.button(label=team["team"], style=discord.ButtonStyle.blurple)
        async def engineering(self, button, interaction: discord.Interaction):
            roles = interaction.user.roles
            if t4253 not in interaction.user.roles:
                await interaction.user.add_roles(t4253)
                self.real_logger.info(f"{interaction.user} 加入4253!")
                embed = discord.Embed(title="成功！", description="已加入4253!", color=default_color)
                embed.set_footer(text="如要退出隊伍，請再次點擊按鈕")
            else:
                await interaction.user.remove_roles(t4253)
                self.real_logger.info(f"{interaction.user} 退出4253")
                embed = discord.Embed(title="成功！", description="已退出4253!", color=default_color)
                embed.set_footer(text="如要重新加入隊伍，請再次點擊按鈕")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            
            

        
    @discord.slash_command(name="role_giver", description="傳送「選取隊伍」訊息")
    @commands.has_permissions(administrator=True)
    async def role_giver(self, ctx: commands.Context):
        embed = discord.Embed(title="請選擇你的隊伍加入", color=default_color)
        embed.set_footer(text="如果沒有看到你的隊伍，請向有 <@&1193209412018524180> 的管理員聯繫")
        await ctx.send(embed=embed, view=self.RoleGiverUI(self.bot, self.real_logger))


def setup(bot):
    bot.add_cog(TeamGiver(bot, bot.logger))