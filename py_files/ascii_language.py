print('ascii_language.py')

from py_files.memory import loadAsciiLanguage
from py_files.preferences import prefs


class AsciiTable:
    def __init__(self):
        self.loadAsciiTable(prefs.get('language_ascii'))

    def loadAsciiTable(self, language):
        table = loadAsciiLanguage(language)
        self.letters = table['letters']
        self.numbers = table['numbers']
        self.keypad1 = table['keypad1']
        self.keypad2 = table['keypad2']
        self.symbols = table['symbols']
        self.specials = table['specials']
        self.modifiers = table['modifiers']
        self.functions = table['functions']


asciiTable = AsciiTable()