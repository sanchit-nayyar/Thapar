import mechanize
from bs4 import BeautifulSoup
import os, time

BR = mechanize.Browser()
f = open("data_webkiosk-thapar.txt", 'r')
data = f.readlines()
f.close()
username = data[0]
password = data[1]

print "Logging In With " + username + " " + password

while True:
    BR.open("https://webkiosk.thapar.edu/")
    print "Page Open"
    BR.select_form(nr = 0)
    BR.form['MemberCode'] = username
    BR.form['Password'] = password
    request = BR.submit()
    print "Submitted"
    ScorePage = BR.open("https://webkiosk.thapar.edu/StudentFiles/Exam/StudentEventMarksView.jsp")
    print "Score Open"
    BR.select_form(nr = 0)
    BR.form['exam'] = ["1718ODDSEM"]
    OutPage = BR.submit()
    print "Submitted"
    BS = BeautifulSoup(OutPage, 'html.parser')
    res = BS.find_all('td')
    res = res[::-1]
    a = res[7]
    a = list(unicode.join(u'\n', map(unicode, a)).encode("ascii", "ignore"))
    a = ''.join(a)
    print a
    f = open("history_webkiosk-thapar.txt", "r")
    hist = f.read()
    f.close()
    if(hist != a):
        f = open("history_webkiosk-thapar.txt", "w+")
        f.write(a)
        f.close()
        os.system("notify-send \"Thapar University, Patiala: Webkiosk\" \"New Scores have been Declared\"")
    time.sleep(60*60)
