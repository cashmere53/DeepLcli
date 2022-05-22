# -*- coding: utf-8 -*-

from typing import Final

from deepl import Translator, Language


API_KEY: Final[str] = "8a84459e-10da-32d5-3e63-13749c3b6c13:fx"
TRANSLATOR: Translator = Translator(API_KEY)

def translate(string: str) -> None:
    result = TRANSLATOR.translate_text(string, target_lang=Language.JAPANESE)
    print(result)
