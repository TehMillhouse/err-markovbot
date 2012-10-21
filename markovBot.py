from errbot.botplugin import BotPlugin
from errbot import botcmd
from markovchain import MarkovChain

class MarkovBot(BotPlugin):

	@botcmd
	def talk(self, mess, args):
		""" Generate a sentence based on database """
		return MarkovChain().generateString()

	@botcmd
	def dbgen(self, mess, args):
		""" Generate markov chain word database """
		# TODO: implement loading text from URL
		markov = MarkovChain()
		if markov.generateDatabase(args):
			# Generating gatabase worked
			return 'Done.'
		else:
			# Something went wrong :/
			return 'Error: Could not generate database'
