import asyncio

import discord
from discord import app_commands
from discord.ext import commands


class BasicDiscordBot(commands.Bot):
    async def setup_hook(self):
        
        await self.load_cogs(["cogs.ping_cog"])
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
            return await interaction.response.send_message(f"Command is currently on cooldown! Try again in {error.retry_after}s.", ephemeral=True)

        elif isinstance(error, app_commands.MissingPermissions):
            return await interaction.response.send_message("You're missing the proper permissions!", ephemeral=True)
            
        else:
            raise error