 
from __future__ import print_function
import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists
import subprocess # executing program
import hashlib

with open("dictPwdFile1.txt","r") as myTxt:
    for line in myTxt:
        eachLine = line.strip()
        user = line.split(", ")[0]
        salt = line.split(", ")[1]  
        pas = line.split(", ")[2]
        pasw = pas.rstrip()
        with open ("wordsEn.txt","r") as myDict:
            for words in myDict:
                word = words.rstrip()
                temp = word + salt
                saltedDictWord = hashlib.sha1(temp).hexdigest()
                if(saltedDictWord == pasw):
                    print ("yes_",user,"_",pasw) 
#---------------------------------------------------------------
