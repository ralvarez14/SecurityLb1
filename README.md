URL used on assigment: http://www-01.sil.org/linguistics/wordlists/english/

URL1: https://www.darknet.org.uk/2008/02/password-cracking-wordlists-and-tools-for-brute-forcing/
    This url contains a set of links that lead to common passwords in french and eanglish

URL2: http://www.wirelesshack.org/wpa-wpa2-word-list-dictionaries.html
    Contains list of wpa/wpa2 word list dictionaries

Approches: 

dictionary Attack: First I store all usernames, salts and passwords on diferent structures so I can access them, then after getting, salting and encripting the password of the dictionary I compare them to the hased password.

Brute Force Attack: For the brute force attack I appended all list's into one, then I itirate trough that one, using itertools from python allowed me to itirate trough the list the necesary times, and I was able to retrieve 3 passwords (4 if I left it long enough) because I am using python library, I asume that the itiration would be faster if I didn't used that library, but creating my own itiration.

Online Attack: Using the web I manage to understand the use of cookies to store information and was able to log in succesfully using a combination of urllib and urllib2

Problems: for the Online attack I was unable to get the password to log in until I discover that I have to specify the field name of the bos I want to fill specified by the webmaster of the page; I solve it by changing it.

Results:

Dictionary Attack:
    [student@localhost Lab1]$ python dictAtck.py 
    Time: 0.443984031677 User:  james1_KnS Pass:  spite
    Time: 0.962715864182 User:  linda1_KnS Pass:  standard
    Time: 1.16655397415 User:  sofia1_KnS Pass:  datura
    Time: 1.80447506905 User:  santiago1_KnS Pass:  matrixing
    Time: 2.35928988457 User:  isabella1_KnS Pass:  scrapings
    Time: 2.74764585495 User:  diego1_KnS Pass:  psychosexuality
    Time: 3.0248439312 User:  robert1_KnS Pass:  forgeries
    Time: 3.71357989311 User:  mary1_KnS Pass:  winningly
    Time: 3.81251192093 User:  patricia1_KnS Pass:  decaffeinated
    Time: 4.51313591003 User:  daniela1_KnS Pass:  tetrachloride
Online Atack:
    [student@localhost Lab1]$ python onlineAtck.py 
    ('Time: 12.6478309631', 'User:', 'jonathan1_-KnS', 'password is:', 'sf')
Brunte Force Attack ( only reached 3 passwords):
    [student@localhost Lab1]$ python BFAtck.py 
    ('Seconds: 0.00553393363953', 'User: ', 'robert1-KnS', 'Pasword: ', '8')
    ('Seconds: 0.114439964294', 'User: ', 'patricia1-KnS', 'Pasword: ', 'uM')
    ('Seconds: 4.79373002052', 'User: ', 'mary1-KnS', 'Pasword: ', 'r9c')

The salting technique is a usefull method of handleing intrusions on a sysstem; by salting a password you provide an extra layer of security, sincce the attacker does not know the exact methon it was used for salting, of the type of hased it used.

For reference I based myself on this website: http://opensourceforu.com/2015/03/python-requests-interacting-with-the-web-made-easy/
