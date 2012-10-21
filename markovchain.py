import pickle
import sys

class MarkovChain(object):
	def __init__(self, dbFilePath="markovdb"):
		try:
			with open(dbFilePath) as dbfile: pass
			self.db = pickle.load(dbfile)
		except IOError as e:
			sys.stderr.write('Database file not found, using empty database\n')
			self.db = {}

	def generateDatabase(self, string):
		self.db = {}
		return True
		# TODO
	
	def generateString(self):
		# TODO
		return "This is just a placeholder"
