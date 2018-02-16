from __future__ import print_function
import time
import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
import hashlib
start_time = time.time()
with open("dictPwdFile1.txt","r") as myTxt:                     # Open text
    for line in myTxt:
        eachLine = line.strip()                                 # Separate by lines
        user = line.split(", ")[0]                              # put every word into different arrays
        salt = line.split(", ")[1]  
        pas = line.split(", ")[2]
        pasw = pas.rstrip()                                     # take out new line character
        with open ("wordsEn.txt","r") as myDict:                # Open txt
            for words in myDict:
                word = words.rstrip()                           # take new line character
                temp = word + salt                              # Add salt
                saltedDictWord = hashlib.sha1(temp).hexdigest() # Hash and get hex
                if(saltedDictWord == pasw):                     # Compare
                    print ("Time: %s"%(time.time()-start_time),"User: ",user,"Pass: ",word) 
#---------------------------------------------------------------
