# -*- coding: utf-8 -*-

from pathlib import Path
from typing import Final

from deepl import Translator, Language


API_KEY: Final[str] = Path("./token.txt").read_text().rstrip("\r\n")
TRANSLATOR: Translator = Translator(API_KEY)

def translate(string: str) -> None:
    result = TRANSLATOR.translate_text(string, target_lang=Language.JAPANESE)
    print(result)
