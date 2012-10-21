import pickle
import sys

class MarkovChain(object):
	def __init__(self, dbFilePath="markovdb"):
		self.dbFilePath = dbFilePath
		try:
			with open(dbFilePath) as dbfile:
				self.db = pickle.load(dbfile)
		except IOError as e:
			sys.stderr.write('Database file not found, using empty database\n')
			self.db = {}

	def generateDatabase(self, string):
		""" Generate word probability database from raw content string """
		# TODO actual frequency analysis
		self.db = {}
		try:
			with open(self.dbFilePath, 'w') as dbfile:
				pickle.dump(self.db, dbfile)
				# It looks like db was written successfully
				return True
		except IOError as e:
			sys.stderr.write('Database file could not be written')
			return False
	
	def generateString(self):
		# TODO implement actual markov chain
		return "This is just a placeholder"
