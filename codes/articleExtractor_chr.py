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
		self.tags = set(["publisher","fulltext","document","pub_title","full_text","pub_date","author","abstract","title","document_url","pq_doc_id", "pub_title", "document_url", "abstract", "title","database", "query","pub_date","document_id","source", "script", "p"])
		self.current_tag = "NULL"
		self.end_tag = "NULL"
		self.document_id = "NULL"
		self.publisher = "NULL"
		self.content = ""
		self.pub_title = "NULL"
		self.document_url = "NULL"
		self.abstract = "NULL"
		self.title = "NULL"
		self.database = "NULL"
		self.query = "NULL"
		self.pub_date = "NULL"
		self.document_id = "NULL"
		self.source = "NULL"
		self.counter = 0
		self.p_tag = 0

	def handle_starttag(self, tag, attrs):
		if tag == "document":
			self.current_tag = "document"
		if tag == "publisher":
			self.current_tag = "publisher"
		if tag == "fulltext":
			self.current_tag = "fulltext"
		if tag == "pub_title":
			self.current_tag = "pub_title"
		if tag == "document_url":
			self.current_tag = "document_url"
		if tag == "abstract":
			self.current_tag = "abstract"
		if tag == "title":
			self.current_tag = "title"
		if tag == "database":
			self.current_tag = "database"
		if tag == "query":
			self.current_tag = "query"
		if tag == "pub_date":
			self.current_tag = "pub_date"
		if tag == "document_id":
			self.current_tag = "document_id"
		if tag == "source":
			self.current_tag = "source"
		if tag == "script":
			self.current_tag = "script"
		if tag == "p":
			if self.current_tag == "fulltext":
				self.p_tag += 1

	def handle_endtag(self, tag):
		if tag == "document":
			self.current_tag = ""
			self.end_tag = "document"
			self.printout()
		if tag == "publisher":
			self.current_tag = ""
			self.end_tag = "publisher"
		if tag == "fulltext":
			self.current_tag = ""
			self.end_tag = "fulltext"
		if tag == "pub_title":
			self.current_tag = ""
			self.end_tag = "pub_title"
		if tag == "document_url":
			self.current_tag = ""
			self.end_tag = "document_url"
		if tag == "abstract":
			self.current_tag = ""
			self.end_tag = "abstract"
		if tag == "title":
			self.current_tag = ""
			self.end_tag = "title"
		if tag == "database":
			self.current_tag = ""
			self.end_tag = "database"
		if tag == "query":
			self.current_tag = ""
			self.end_tag = "query"
		if tag == "pub_date":
			self.current_tag = ""
			self.end_tag = "pub_date"
		if tag == "document_id":
			self.current_tag = ""
			self.end_tag = "document_id"
		if tag == "source":
			self.current_tag = ""
			self.end_tag = "source"
		if tag == "script":
			self.current_tag = ""
			self.end_tag = "script"
		if tag == "p":
			if self.current_tag == "fulltext":
				self.content += "\n"
				self.p_tag -= 1


	def handle_data(self, text):
		text = text.strip()
		#print len(text)

			#		if self.current_tag == "script":
		#	print text

		if self.current_tag == "fulltext" or self.current_tag not in self.tags:
			self.content += text
		#print self.current_tag+"\t"+text
	#	print self.current_tag+"|"+ self.document_id+"|"+ text
		if self.current_tag == "publisher":
			if self.publisher == "NULL":
				self.publisher = text
			else:
				print "ERROR: Uncleared Publisher "+self.publisher+" from "+self.document_id + ", "+text+", "+a.file_name
				sys.exit(0)
				self.printout()
				self.publisher = text

		if self.current_tag == "pub_title":
			if self.pub_title == "NULL":
				self.pub_title = text
			else:
				print "ERROR: Uncleared Publisher Title "+ self.pub_title +", from "+self.document_id + ", "+text
				sys.exit(0)
				self.printout()
				self.pub_title = text

		if self.current_tag == "document_url":
			if self.document_url == "NULL":
				self.document_url = text 
			else:
				print "ERROR: Uncleared Document URL "+self.document_url+", from "+self.document_id + ", "+text
				sys.exit(0)
				self.printout()
				self.publication_date = text

		if self.current_tag == "title":
			if self.title == "NULL":
				self.title = text
			else:
				print "ERROR: Uncleared Paper Title "+ self.title +", from "+self.file_name + ", "+text
				sys.exit(0)
				self.printout()
				self.title = text

		if self.current_tag == "database":
			if self.database == "NULL":
				self.database = text
			else:
				print "ERROR: Uncleared Paper Database "+ self.database +", from "+self.file_name + ", "+text
				sys.exit(0)
				self.printout()
				self.database = text

		if self.current_tag == "query":
#			self.counter += 1
#			print str(self.counter)+"\t"+self.query
			if self.query == "NULL":
				self.query = text
			else:
				print "ERROR: Uncleared Paper Query "+ self.query +", from "+self.file_name + ", "+text
				sys.exit(0)
				self.printout()
				self.query = text

		if self.current_tag == "pub_date":
			if self.pub_date == "NULL":
				self.pub_date = " ".join(text.strip().split(" ")[0:3])
			else:
				print "ERROR: Uncleared Paper pubdate "+ self.pub_date +", from "+self.file_name + ", "+text
				sys.exit(0)
				self.printout()
				self.pub_date = text

		if self.current_tag == "document_id":
			if self.document_id == "NULL":
				self.document_id = text
			else:
				print "ERROR: Uncleared Document ID "+self.document_id + ", " + text
				sys.exit(0)
				self.printout()
				self.document_id = text

		if self.current_tag == "source":
			if self.source == "NULL":
				self.source = text
			else:
				print "ERROR: Uncleared Document ID "+self.source + ", " + text
				sys.exit(0)
				self.printout()
				self.source = text

#	Print out the information as needed
#	Output two files, one contains the meta-data, while the second one contains full text
	def printout(self):
		if 1:
			fout = open(sys.argv[4]+"/"+self.document_id + ".txt", "a")
			fout.write("\n".join(self.content.split("/pp")))
			fout.close()

		self.content = ""

		fout = open(sys.argv[3], "a")
		fout.write(self.document_id+"\t"+self.query+'\tChronicle\t'+self.pub_title+"\tNULL\t0\t"+self.pub_date+"\n")
		fout.close()

		# Clear status of the variables, to avoid missing values
		self.document_id = "NULL"
		self.publication_date = "NULL"
		self.authors = "NULL"
		self.pub_title = "NULL"
		self.publisher = "NULL"
		self.content = ""
		self.publisher = "NULL"
		self.pub_title = "NULL"
		self.document_url = "NULL"
		self.title = "NULL"
		self.database = "NULL"
		self.query = "NULL"
		self.pub_date = "NULL"
		self.source = "NULL"

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
	source = re.sub("&#13;","",source)

	#try:
	a.file_name = file
	#a.query = query
	a.feed(source)
	#print file
	#except:
	#	print "ERROR: "+file
		

