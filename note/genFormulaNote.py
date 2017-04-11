#!/usr/bin/python

import sys
import os
import pickle
import re

#===  class define ...

class argListOut:
 
   def __init__(self,argList):
     self.argList = argList
     self.argStr = ""


   def ListOut(self):
     for value in self.argList:
         self.argStr = self.argStr+" "+value
     print(self.argStr) 

#===  main program start ...

if len(sys.argv) != 2:
   print "The line option is not assigned correctly : ",
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()
   print "EXIT "
   exit()
else :
   argList = (sys.argv) 
   argListOutInst = argListOut(argList)
   argListOutInst.ListOut()

#=== Input File handling area ...

fileNow = open(argList[1], 'r')
#print fileNow.read()
listNow = fileNow.readlines()
fileNow.close()

#=== Output File handling area ...



for i, item in enumerate(listNow):
    #print item.strip()
    regex = r"===========\s*<a\s+name=\"(\d+)\"></a>"
    if (re.findall(regex, item.strip())):
        print i, item
        match = re.search(regex, item)
        fileNow = "formula_"+match.group(1)+".html"
        new_file = open(fileNow, "w")

        new_file.write("<pre style=\"color: rgb(0, 0, 0); word-wrap: break-word; white-space: pre-wrap;\">\n")
        g=i
        while not ("==========" in listNow[g+1]):
            if g==i+3:
               new_file.write("<b><h2>"+listNow[g]+"</h2></b><h3>")         
            else:
               new_file.write(listNow[g])         
            g+=1 
        new_file.write("</pre></h3>")
        new_file.close()













