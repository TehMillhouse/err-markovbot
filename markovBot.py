from errbot.botplugin import BotPlugin
from errbot import botcmd
from markovchain import MarkovChain
import requests

class MarkovBot(BotPlugin):

	@botcmd
	def talk(self, mess, args):
		""" Generate a sentence based on database """
		return MarkovChain().generateString()


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
	def dbgenfromurl(self, mess, args):
		req = requests.get(args)
		if req.ok and MarkovChain().generateDatabase(req.content):
			return 'Done.'
		else:
			return 'Error: Could not generate database from URL'

