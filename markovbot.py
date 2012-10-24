from pymarkovchain import MarkovChain
# You'll need the pymarkovchain package. See README
from errbot.botplugin import BotPlugin
from errbot import botcmd
import requests


class MarkovBot(BotPlugin):

    @botcmd
    def talk(self, mess, args):
        """ Generate a sentence based on database """
        return MarkovChain().generateString()

    @botcmd
    def complete(self, mess, args):
        """ Try to complete a sentence """
        return MarkovChain().generateStringWithSeed(args)

    @botcmd
    def dbgenfromfile(self, mess, args):
        """ Generate markov chain word database """
        markov = MarkovChain()
        try:
            with open(args) as txtFile:
                txt = txtFile.read()
        except IOError as e:
            return 'Error: could not open text file'
        # At this point, we've got the file contents
        if markov.generateDatabase(txt):
            return 'Done.'
        else:
            return 'Error: Could not generate database'

    @botcmd
    def dbgenfromstring(self, mess, args):
        if MarkovChain().generateDatabase(args):
            return 'Done.'
        else:
            return 'Error: Could not generate database from String'

    @botcmd
    def dbgenfromurl(self, mess, args):
        req = requests.get(args)
        if req.ok and MarkovChain().generateDatabase(req.content):
            return 'Done.'
        else:
            return 'Error: Could not generate database from URL'
