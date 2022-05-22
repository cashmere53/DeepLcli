# -*- coding: utf-8 -*-

from deeplcli.translate import translate

def main() -> None:
    import sys
    translate(sys.argv[1])
