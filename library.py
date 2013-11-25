class Library:
	"""Contains dictionaries of authors and papers"""
	def __init__(self):
		self.papers = dict()
		self.authors = dict()

	def getPaper(self,title):
		if title not in self.papers:
			self.papers[title] = Paper(self, title)
		return self.papers[title]

	def getAuthor(self, name):
		if name not in self.authors:
			self.authors[name] = Author(self,name)
		return self.authors[name]

class Paper:
	"""A paper with authors and citations"""
	def __init__(self,library,title):
		self.title = title
		self.authors = list()
		self.citations = list()
		self.library = library

	def addAuthorIds(self,authors):
		for author in authors:
			self.addAuthorId(author)

	def addAuthorId(self,author):
		author_obj = self.library.getAuthor(author)
		self.authors.append(author_obj)
		author_obj.addPaper(self)

	def addCitationIds(self,cited_list):
		for cited in cited_list:
			self.addCitationId(cited)

	def addCitationId(self,cited):
		author_obj = self.library.getAuthor(cited)
		self.authors.append(author_obj)

	def __repr__(self):
		return self.title+" | authors: "+' '.join(auth.name for auth in self.authors)

class Author:
	"""An author of papers"""
	def __init__(self,library,name):
		self.name = name
		self.papers = list()
	def addPaper(self,paper):
		self.papers.append(paper)


if __name__ == "__main__":
	lib = Library()
	paper = lib.getPaper("The discovery of things")
	paper.addAuthorIds(['sally','bob','alice'])
	paper.addCitationIds(['alice','sam','john'])

	paper2 = lib.getPaper("Another paper")
	paper2.addAuthorIds(['sam','kevin','alice'])
	paper2.addCitationIds(['sally','bob','alice'])

	divider = ''.join('-' for x in range(10))
	for author in lib.authors.values():
		print divider
		print author.name
		print len(author.papers)
		for paper in author.papers:
			print paper
