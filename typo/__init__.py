from gingerit.gingerit import GingerIt

import rich
from rich import pretty
from rich.console import Console

console = Console()

class typos():

    def __init__(self):
        self.setup()

    def setup(self):
        self.parser = GingerIt()

    def check(self, text):

        try:
            console.print(self.parser.parse(text)["result"][1:], style="green")
            return True

        except:
            console.print("An error has occurred while trying to parse the typo!", style="red")
            return False