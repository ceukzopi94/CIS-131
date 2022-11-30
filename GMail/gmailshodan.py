import os
import ezgmail

#os.chdir(r'C:\json')
os.chdir(r'D:\Pima\CIS 131\GMail')

#ezgmail.init()

def send_test_email(email):
    ezgmail.send('ceurbanski@gmail.com', 
            'TEST', 
            'This is a test of email capabilities.')