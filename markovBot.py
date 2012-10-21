from errbot.botplugin import BotPlugin
from errbot import botcmd


class MarkovBot(BotPlugin):

    @botcmd
    def talk(self, mess, args):
        """ Generate a sentence based on database """
        return "Desu." # TODO

	@botcmd
	def dbgen(self, mess, args):
		""" Generate markov chain word database """
		return "Not doing anything." # TODO
