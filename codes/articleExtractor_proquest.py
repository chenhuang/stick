#! /usr/bin/python
# USAGE: Extract Full texts from Jia's input
# INPUT: Take a list of Jia's files "/home/chhuang/stick/DataForCody/corpus/*" 
# OUTPUT: meta data about the files as meta_data, and full texts of the articles.

import sys
import os
import re
import glob
import codecs

from HTMLParser import HTMLParser

class articleExtractor(HTMLParser):
	def reset(self):
		HTMLParser.reset(self)
		self.tags = set(["document_id", "full_text", "publication_date", "author", "title", "link", "concept", "title", "document", "data", "query", "time_period", "number_of_result", "resource","subject","publication_title", "source_type", "issn"])
		self.current_tag = "NULL"
		self.end_tag = "NULL"
		self.document_id = "NULL"
		self.full_text = "NULL"
		self.publication_date = "NULL"
		self.authors = "NULL"
		self.abstract = "NULL"
		self.title = "NULL"
		self.subject = "NULL"
		self.link = "NULL"
		self.concept = "NULL"
		self.line_num = 0
		self.file_name = "NULL"
		self.content = ""

	def handle_starttag(self, tag, attrs):
		if tag == "data":
			self.current_tag = "data"
		if tag == "query":
			self.current_tag = "query"
		if tag == "document":
			self.current_tag = "document"
		if tag == "document_id":
			self.current_tag = "document_id"
		if tag == "full_text":
			self.current_tag = "full_text"
		if tag == "publication_date":
			self.current_tag = "publication_date"
		if tag == "author":
			self.current_tag = "author"
		if tag == "title":
			self.current_tag = "title"
		if tag == "link":
			self.current_tag = "link"
		if tag == "concept":
			self.current_tag = "concept"

	def handle_endtag(self, tag):
		if tag == "document":
			self.end_tag = "document"
		if tag == "document_id":
			self.end_tag = "document_id"
		if tag == "full_text":
			self.end_tag = "full_text"
		if tag == "publication_date":
			self.end_tag = "publication_date"
		if tag == "author":
			self.end_tag = "author"
		if tag == "title":
			self.end_tag = "title"
		if tag == "link":
			self.end_tag = "link"
		if tag == "concept":
			self.end_tag = "concept"
	
	def transform_date(self, text):
		month_three_letter_to_number = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
		itms = text.split(" ")
		if len(itms) == 3:
			month = itms[0]
			if month in month_three_letter_to_number.keys():
				month = month_three_letter_to_number[month]
			else:
				return "NULL"
			day = itms[1][:-1]
			year=itms[2]
			if len(day) == 1:
				day = '0'+str(day)

			return year+'-'+month+'-'+day
		elif len(itms) == 2:
			#print text
			month = itms[0]
			year = itms[1]
			if month in month_three_letter_to_number.keys():
				month = month_three_letter_to_number[month]
			else:
				return "NULL"
			return year+'-'+month+'-01'
		else:
			return "NULL"

	def handle_data(self, text):
		text = text.strip()
		#print len(text)
		
		if self.current_tag == "full_text" or self.current_tag not in self.tags:
			self.content += text
		#print self.current_tag+"\t"+text
		

		if self.current_tag == "document_id":
			if self.document_id == "NULL":
				self.document_id = text
			else:
				print "ERROR: Uncleared Document ID "+self.document_id + ", " + text
				self.printout()
				self.document_id = text

		if self.current_tag == "publication_date":
			text = text[0:13]
			text = self.transform_date(text)
			if self.publication_date == "NULL":
				self.publication_date = text
			else:
				print "ERROR: Uncleared Publication Date "+self.publication_date+" from "+self.document_id + ", "+text
				self.printout()
				self.publication_date = text

		if self.current_tag == "author":
			if self.authors == "NULL":
				self.authors = text 
			else:
				print "ERROR: Uncleared Author Name "+self.authors+", from "+self.document_id + ", "+text
				self.printout()
				self.publication_date = text

		if self.current_tag == "concept":
			self.concept = text

		if self.current_tag == "title":
			if self.title == "NULL":
				self.title = text
			else:
				print "ERROR: Uncleared Paper Title "+ self.title +", from "+self.document_id + ", "+text
				self.printout()
				self.title = text

		if self.end_tag == "document":
				self.printout()

#	Print out the information as needed
#	Output two files, one contains the meta-data, while the second one contains full text
	def printout(self):
		if 1:
			fout = open(self.document_id + ".txt", "a")
			fout.write(self.full_text)
			fout.close()

		self.full_text = ""

		fout = open(sys.argv[2], "a")
		fout.write(self.document_id+"\t"+self.publication_date+"\t"+self.authors+"\t"+self.title+"\n")
		fout.close()

		# Clear status of the variables, to avoid missing values
		self.document_id = "NULL"
		self.publication_date = "NULL"
		self.authors = "NULL"
		self.title = "NULL"

a = articleExtractor()
files = glob.glob(sys.argv[1])
for file in files:
	fin = open(file, "r")
	source = fin.read()
	fin.close()

	#try:
	a.file_name = file
	a.feed(source)
	#except:
	#	print "ERROR: "+file
		

