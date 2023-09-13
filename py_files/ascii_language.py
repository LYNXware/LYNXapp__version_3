print('ascii_language.py')

from py_files.memory import loadAsciiLanguage
from py_files.preferences import prefs


class AsciiTable:
    def __init__(self):
        loadAsciiLanguage(prefs.get('language_ascii'))

    def loadAsciiTable(self, language):
        table = loadAsciiLanguage(language)
        self.letters = table['letters']
        self.numbers = table['numbers']
        self.keypad = table['keypad']
        self.punctuations = table['punctuations']
        self.symbols = table['symbols']
        self.whithespaces = table['whitespaces']
        self.modifiers = table['modifiers']

        print(table)




asciiTable = AsciiTable()