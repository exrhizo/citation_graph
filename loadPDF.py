from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
#from pdfminer.pdfpage import PDFTextExtractionNotAllowed
import re
#import our library to keep track of the stuff
from library import Library, Paper, Author
# Open a PDF file.

#\W*([A-Z ,])\(\d
author_pattern = re.compile('\d+\.(.*)\(\d')
#lt_obj.get_text()

def loadPDF(library, file_name):
	"""adds a paper to the library"""
	fp = open(file_name, 'rb')
	# Create a PDF parser object associated with the file object.
	parser = PDFParser(fp)
	# Create a PDF document object that stores the document structure.
	document = PDFDocument(parser)
	# Supply the password for initialization.
	# (If no password is set, give an empty string.)
	password = ""
	document.initialize(password)
	# Check if the document allows text extraction. If not, abort.
	if not document.is_extractable:
		print "CANT"
	#	raise PDFTextExtractionNotAllowed
	# Create a PDF resource manager object that stores shared resources.
	rsrcmgr = PDFResourceManager()
	# Set parameters for analysis.
	laparams = LAParams()
	# Create a PDF page aggregator object.
	device = PDFPageAggregator(rsrcmgr, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	
	text_content = []
	authors = []       #list of authors
	citations = []     #list of authors that have been cited
	for page in PDFPage.create_pages(document):
		interpreter.process_page(page)
		# receive the LTPage object for the page.
		layout = device.get_result()
		for lt_obj in layout._objs:
			if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
				cur_line = lt_obj.get_text()
				#print cur_line
				#print "\n NEW LINE \n"
				match = author_pattern.match(cur_line)
				if match is not None:
						match_span = match.span()
						print match.group(1)
				#text_content.append(lt_obj.get_text())
	paper_title = file_name
	paper = library.getPaper(paper_title)
	paper.addAuthorIds(authors)
	paper.addCitationIds(citations)

if __name__ == "__main__":
	lib = Library()
	loadPDF(lib, './test_papers/2009 Tseng predicting function and binding profile.pdf')
	divider = ''.join('-' for x in range(10))
	for author in lib.authors.values():
		print divider
		print author.name
		print len(author.papers)
		for paper in author.papers:
			print paper
