import os
os.chdir("C:/Python27/Scripts")
os.system("pip install mechanize")
os.system("pip install bs4")

username = raw_input("Enter Thapar Roll Number: ")
password = raw_input("Enter Webkiosk Password: ")
f = open("data_webkiosk-thapar.txt", "w+")
f.write(username + "\n" + password)
f.close()

