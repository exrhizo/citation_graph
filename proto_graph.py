
#dictionary of all the authors
AUTHORS = dict()

class Author:
	"""representation of an author"""
	def __init__(self,name):
		self.name = name
		self.cited_count = 0
		self.cited_by = []
	def addCitation(self, from_auth):
		self.cited_count += 1
		if from_auth not in self.cited_by:
			if from_auth in AUTHORS:
				self.cited_by.append(AUTHORS[from_auth])
			else:
				new_author = Author(from_auth)
				self.cited_by.append(new_author)
				AUTHORS[from_auth] = new_author
	def __repr__(self):
		return self.name

auth1 = Author('bob')
auth2 = Author('sam')
auth3 = Author('alice')

AUTHORS['bob'] = auth1
AUTHORS['sam'] = auth2
AUTHORS['alice'] = auth3

auth1.addCitation('kevin')
auth1.addCitation('sam')
auth1.addCitation('bob')
auth2.addCitation('alice')
auth2.addCitation('bob')
auth3.addCitation('sam')
auth3.addCitation('kevin')

divider = ''.join('-' for x in range(10))
for author in AUTHORS.values():
	print divider
	print author.name
	print author.cited_count
	print author.cited_by