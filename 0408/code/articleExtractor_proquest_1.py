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
		self.tags = set(["publisher","fulltext","document","pub_title","full_text","pub_date","author","abstract","title","document_url","pq_doc_id"])
		self.current_tag = "NULL"
		self.end_tag = "NULL"
		self.document_id = "NULL"
		self.content = ""
		self.publication_date = "NULL"
		self.authors = "NULL"
		self.abstract = "NULL"
		self.title = "NULL"
		self.pub_title = "NULL"
		self.subject = "NULL"
		self.link = "NULL"
		self.concept = "NULL"
		self.line_num = 0
		self.file_name = "NULL"
		self.content = ""

	def handle_starttag(self, tag, attrs):
		if tag == "publisher":
			self.current_tag = "publisher"
		if tag == "fulltext":
			self.current_tag = "fulltext"
		if tag == "document":
			self.current_tag = "document"
		if tag == "pub_title":
			self.current_tag = "pub_title"
		if tag == "full_text":
			self.current_tag = "full_text"
		if tag == "pub_date":
			self.current_tag = "pub_date"
		if tag == "author":
			self.current_tag = "author"
		if tag == "abstract":
			self.current_tag = "abstract"
		if tag == "title":
			self.current_tag = "title"
		if tag == "document_url":
			self.current_tag = "document_url"
		if tag == "pq_doc_id":
			self.current_tag = "pq_doc_id"

	def handle_endtag(self, tag):
		if tag == "publisher":
			self.end_tag = "publisher"
		if tag == "fulltext":
			self.end_tag = "fulltext"
		if tag == "document":
			self.end_tag = "document"
			self.printout()
		if tag == "pub_title":
			self.end_tag = "pub_title"
		if tag == "full_text":
			self.end_tag = "full_text"
		if tag == "pub_date":
			self.end_tag = "pub_date"
		if tag == "author":
			self.end_tag = "author"
		if tag == "abstract":
			self.end_tag = "abstract"
		if tag == "title":
			self.end_tag = "title"
		if tag == "document_url":
			self.end_tag = "document_url"
		if tag == "pq_doc_id":
			self.end_tag = "pq_doc_id"

	def handle_data(self, text):

		text = text.strip()
		#print len(text)

		if self.current_tag == "fulltext" or self.current_tag not in self.tags:
			self.content += text
		#print self.current_tag+"\t"+text
	#	print self.current_tag+"|"+ self.document_id+"|"+ text
		if self.current_tag == "pq_doc_id":
			if self.document_id == "NULL":
				self.document_id = text
			else:
				print "ERROR: Uncleared Document ID "+self.file_name + ", " + text
				sys.exit(0)
				self.printout()
				self.document_id = text

		if self.current_tag == "pub_date":
			if self.publication_date == "NULL":
				self.publication_date = text
			else:
				print "ERROR: Uncleared Publication Date "+self.publication_date+" from "+self.document_id + ", "+text
				sys.exit(0)
				self.printout()
				self.publication_date = text

		if self.current_tag == "author":
			if self.authors == "NULL":
				self.authors = text 
			else:
				print "ERROR: Uncleared Author Name "+self.authors+", from "+self.document_id + ", "+text
				sys.exit(0)
				self.printout()
				self.publication_date = text

		if self.current_tag == "pub_title":
			if self.pub_title == "NULL":
				self.pub_title = text
			else:
				print "ERROR: Uncleared Publisher Title "+ self.title +", from "+self.document_id + ", "+text
				sys.exit(0)
				self.printout()
				self.pub_title = text

		if self.current_tag == "title":
			if self.title == "NULL":
				self.title = text
			else:
				print "ERROR: Uncleared Paper Title "+ self.title +", from "+self.file_name + ", "+text
				sys.exit(0)
				self.printout()
				self.title = text


#	Print out the information as needed
#	Output two files, one contains the meta-data, while the second one contains full text
	def printout(self):
		if 1:
			fout = open(sys.argv[4]+"/"+self.document_id + ".txt", "a")
			fout.write(self.content)
			fout.close()

		self.content = ""

		fout = open(sys.argv[3], "a")
		fout.write(self.document_id+"\t"+self.query+'\tProquest\t'+self.pub_title+"\tNULL\t0\t"+self.publication_date+"\n")
		fout.close()

		# Clear status of the variables, to avoid missing values
		self.document_id = "NULL"
		self.publication_date = "NULL"
		self.authors = "NULL"
		self.pub_title = "NULL"
		self.title = "NULL"

files = glob.glob(sys.argv[1])
query = sys.argv[2]
meta_location = sys.argv[3]
txt_location = sys.argv[4]

for file in files:
	a = articleExtractor()
	fin = open(file, "r")
	source = fin.read()
	fin.close()

	# pre-process the source html content
	source = re.sub("&amp;","and",source)
	source = re.sub("&quot;",'"',source)
	source = re.sub("&apos;","'",source)
	source = re.sub("&lt;","<",source)
	source = re.sub("&gt;",">",source)

	#try:
	a.file_name = file
	a.query = query
	a.feed(source)
	#print file
	#except:
	#	print "ERROR: "+file
		

