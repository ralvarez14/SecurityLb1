import hashlib
import time
import itertools
start_time = time.time()                                # Start time
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = [x.upper() for x in lower]
numbers = ["1","2","3","4","5","6","7","8","9","0","-","_"]
all_Lists = []
all_Lists = lower + upper + numbers
for i in range(1,10):                                   # Permutator
    for j in itertools.product(all_Lists,repeat=i):
        word = ''.join(j)                               # Append the word
        saltedWord = hashlib.sha1(word).hexdigest()     # Hash word & convert it to hexidecimal
        
        with open("randPwdFile1.txt","r") as myTxt:     # Open and itirate through text file1
            for line in myTxt:
                eachLine = line.rstrip()                # Remove last character
                username = eachLine.split(", ")[0]      # Split into colums according with commas
                saltedPasw = eachLine.split(", ")[1]
                if(saltedWord == saltedPasw):           # Compare Password with Hashword
                    print ("Seconds: %s"%(time.time()-start_time),"User: ",username,"Pasword: ",word)
