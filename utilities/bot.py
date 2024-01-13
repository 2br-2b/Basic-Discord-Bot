import asyncio

import discord
from discord import app_commands
from discord.app_commands import locale_str as _
from discord.ext import commands

from utilities.translator import Translator


class BasicDiscordBot(commands.Bot):
    async def setup_hook(self):
        
        await self.load_cogs(["cogs.ping_cog"])
        await self.tree.set_translator(Translator())
        
        asyncio.create_task(self.tree.sync())
        
    async def load_cogs(self, cog_list: list):
        for cog_name in cog_list:
            try:
                await self.load_extension(cog_name)
            except commands.errors.ExtensionNotFound:
                print(cog_name + " cog not found")
            except commands.errors.ExtensionAlreadyLoaded:
                pass
            except commands.errors.NoEntryPointError:
                print("Put the setup() function back in " + cog_name)
                
    async def on_ready(self) -> None:
        print("Bot started!")

    async def on_tree_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            
            
            return await interaction.response.send_message(await interaction.translate(_("missing-perms"), data={"seconds": error.retry_after}), ephemeral=True)

        elif isinstance(error, app_commands.MissingPermissions):
            return await interaction.response.send_message(await interaction.translate(_("missing-perms")), ephemeral=True)
            
        else:
            raise error