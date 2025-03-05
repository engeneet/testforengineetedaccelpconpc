from main.modules.baseCLI import *
import random

class BootEngi: #do not ask me why is it called "bootengi" lol
    def __init__(self, sys):
        self.sys = sys
        self.cli = sys.cli
        self.sc = sys.screen

        self.on_init()

    def on_init(self):
        self.cli.clearLines()
        self.cli.addLine("Hello World!")

    def update(self):
        return
