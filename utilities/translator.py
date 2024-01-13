import os
from re import S
from typing import Dict, Optional

import discord
from discord import Locale, app_commands
from discord.app_commands import locale_str as _
from fluent.runtime import FluentLocalization, FluentResourceLoader


class Translator(app_commands.Translator):
    resource_ids = os.listdir("t10n/en-US/") 
    
    async def load(self) -> None:
        self.loader = FluentResourceLoader("t10n/{locale}")
        self.english_l10n = FluentLocalization(["en-US"], self.resource_ids, self.loader)
        self.spanish_l10n = FluentLocalization(["es-ES", "en-US"], self.resource_ids, self.loader)
        print('Translator loaded')
        
    async def unload(self) -> None:
        print('Translator unloaded')
        
    async def translate(self, string: app_commands.locale_str, locale: discord.Locale, context: app_commands.TranslationContext) -> Optional[str]:
        
        data: Dict[str, str] | None = None
        
        # todo use better logic
        if type(context.data).__name__ == 'dict':
            data = context.data
        
        match locale:
            case Locale.spain_spanish:
                new_string = self.spanish_l10n.format_value(string.message, data)
            case _:
                new_string = self.english_l10n.format_value(string.message, data)

        if locale == Locale.american_english and string.message == new_string:
            print(f"***MISSING TRANSLATION: {string}")
        
        return new_string