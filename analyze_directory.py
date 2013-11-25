from library import Library, Paper, Author
from loadPDF import loadPDF
import glob
from os import path
from os import makedirs

lib = Library()
#loadPDF(lib, './test_papers/2009 Tseng predicting function and binding profile.pdf')

conf_record_files = glob.glob(path.join('test_papers','*.pdf'))
i = 0
for conf_record_file in conf_record_files:
	print "{} Loading: {}".format(i,conf_record_file)
	loadPDF(lib,conf_record_file)
	i+=1
	if i>10:
		break