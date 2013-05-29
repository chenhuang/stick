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
#		self.tags = set(["document_id", "full_text", "publication_date", "author", "title", "link", "concept", "title", "document", "data", "query", "time_period", "number_of_result", "resource","subject","publication_title", "source_type", "issn"])
        self.tags = set(["data","query","time_period","concept","number_of_result","resource","document","link","title","abstract","inventor","assignee","filed"])
        self.filed_tag = "NULL"
        self.assignee_tag = "NULL"
        self.current_tag = "NULL"
        self.end_tag = "NULL"
        self.document = "NULL"
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
        self.companies = "NULL"
        self.patent_no = "NULL"

    def handle_starttag(self, tag, attrs):
        if tag == "data":
            self.current_tag = "data"
        if tag == "query":
            self.current_tag = "query"
        if tag == "document":
            self.current_tag = "document"
        if tag == "link":
            self.current_tag = "link"
        if tag == "concept":
            self.current_tag = "concept"
        if tag == "filed":
            self.current_tag = "filed"
        if tag == "assignee":
            self.current_tag = "assignee"
        if tag == "title":
            self.current_tag = "title"
        if tag == "pat_no":
            self.current_tag = "pat_no"

    def handle_endtag(self, tag):
        if tag == "document":
            self.end_tag = "document"
            self.current_tag = "NULL"
        if tag == "document_id":
            self.end_tag = "document_id"
            self.current_tag = "NULL"
        if tag == "full_text":
            self.end_tag = "full_text"
            self.current_tag = "NULL"
        if tag == "publication_date":
            self.end_tag = "publication_date"
            self.current_tag = "NULL"
        if tag == "author":
            self.end_tag = "author"
            self.current_tag = "NULL"
        if tag == "title":
            self.end_tag = "title"
            self.current_tag = "NULL"
        if tag == "link":
            self.end_tag = "link"
            self.current_tag = "NULL"
        if tag == "concept":
            self.end_tag = "concept"
            self.current_tag = "NULL"
        if tag == "filed":
            self.end_tag = "filed"
            self.current_tag = "NULL"
        if tag == "assignee":
            self.end_tag = "assignee"
            self.current_tag = "NULL"
        if tag == "pat_no":
            self.end_tag = "pat_no"
            self.current_tag = "NULL"
    
    def handle_data(self, text):
        text = text.strip()
		
        if self.current_tag == "filed":
            if self.publication_date == "NULL":
                self.publication_date = text
            else:
                print "ERROR: Uncleared Publication Date "+self.publication_date+" from "+self.title + ", "+text
                self.printout()

        if self.current_tag == "assignee":
            if self.companies == "NULL":
                self.companies = text 
            else:
                print "ERROR: Uncleared Company Name "+self.companies+", from "+self.title + ", "+text
                self.printout()

        if self.current_tag == "concept":
            self.concept = text

        if self.current_tag == "title":
            if self.title == "NULL":
                self.title = text
            else:
                print "ERROR: Uncleared Paper Title "+ self.title +", from "+self.title + ", "+text
                self.printout()

        if self.current_tag == "pat_no":
            if self.patent_no == "NULL":
                self.patent_no = text
                self.patent_no = re.sub(",", "", self.patent_no)
            else:
                print "ERROR: Uncleared Patent No " + self.patent_no + ", from " + self.title + ", " + text
                self.printout()

        if self.end_tag == "document":
            self.printout()

#	Print out the information as needed
#	Output two files, one contains the meta-data, while the second one contains full text
    def printout(self):
        if 0:
            fout = open(self.document_id + ".txt", "a")
            fout.write(self.full_text)
            fout.close()

        self.full_text = ""

        fout = open(sys.argv[2], "a")
#        fout.write(self.title+"\t"+self.publication_date+"\t"+self.companies+"\n")
        fout.write(self.patent_no+"\t"+self.title+"\n")
        fout.close()

        # Clear status of the variables, to avoid missing values
        self.publication_date = "NULL"
        self.authors = "NULL"
        self.title = "NULL"
        self.companies = "NULL"
        self.end_tag = "NULL"
        self.patent_no = "NULL"

a = articleExtractor()
files = glob.glob(sys.argv[1])
for file in files:
    fin = open(file, "r")
    source = fin.read()
    fin.close()

    a.file_name = file
    a.feed(source)

