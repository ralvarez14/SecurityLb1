import hashlib
import itertools

lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = [x.upper() for x in lower]
numbers = ["1","2","3","4","5","6","7","8","9","0","-","_"]
all_Lists = []
all_Lists = lower + upper + numbers
for i in range(1,10):
    for j in itertools.product(all_Lists,repeat=i):
        word = ''.join(j)
        saltedWord = hashlib.sha1(word).hexdigest()
        
        with open("randPwdFile1.txt","r") as myTxt:
            for line in myTxt:
                eachLine = line.rstrip()
                username = eachLine.split(", ")[0]
                saltedPasw = eachLine.split(", ")[1]
                if(saltedWord == saltedPasw):
                    print ("yes_",username,"_",word)
