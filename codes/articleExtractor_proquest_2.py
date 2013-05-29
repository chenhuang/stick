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
		self.document_id_tag = 0
		self.document_id = "NULL"
		self.full_text_tag = 0
		self.full_text = "NULL"
		self.publication_date_tag = 0
		self.publication_date = "NULL"
		self.authors_tag = 0
		self.authors = "NULL"
		self.abstract_tag = 0
		self.abstract = "NULL"
		self.title_tag = 0
		self.title = "NULL"
		self.subject_tag = 0
		self.subject = "NULL"
		self.document_end = 0
		self.link_tag = 0
		self.link = "NULL"
		self.concept_tag = 0
		self.concept = "NULL"

	def handle_starttag(self, tag, attrs):
		if tag == "document_id":
			self.document_id_tag = 1
		if tag == "full_text":
			self.full_text_tag = 1
		if tag == "publication_date":
			self.publication_date_tag = 1
		if tag == "author":
			self.authors_tag = 1
		if tag == "title":
			self.title_tag = 1
		if tag == "link":
			self.link_tag = 1
		if tag == "concept":
			self.concept_tag = 1
		if tag == "title":
			self.title_tag = 1

	def handle_endtag(self, tag):
		if tag == "document":
			self.document_end = 1
		if self.document_id_tag == 1:
		 	self.document_id_tag = 0
		if self.publication_date_tag == 1:
			self.publication_date_tag = 0
		if self.authors_tag == 1:
			self.authors_tag = 0
		if self.concept_tag == 1:
			self.concept_tag = 0
		if self.title_tag == 1:
			self.title_tag = 0
	
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
			print text
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
		if self.document_id_tag == 1:
		 	self.document_id = text
		if self.full_text_tag == 1:
			self.full_text += text
		if self.publication_date_tag == 1:
			text = text[0:13]
			text = self.transform_date(text)
			self.publication_date = text
		if self.authors_tag == 1:
			self.authors = text
		if self.concept_tag == 1:
			self.concept = text
		if self.title_tag == 1:
			self.title = text
		if self.document_end == 1:
			self.printout()
			self.document_end = 0

#	Print out the information as needed
# 	Output two files, one contains the meta-data, while the second one contains full text
	def printout(self):
		if 1:
			fout = open(self.document_id + ".txt", "w")
			fout.write(self.full_text)
			fout.close()

		self.full_text = ""

		fout = open(sys.argv[2], "a")
		fout.write(self.document_id+"\t"+self.publication_date+"\t"+self.authors+"\t"+self.title+"\n")
		fout.close()

		# Clear the status of the variables, to avoid missing values
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
	a.feed(source)
	#except:
	#	print "ERROR: "+file
		

