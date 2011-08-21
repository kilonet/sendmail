# -*- coding:utf-8 -*-
from datetime import datetime
from email.mime.multipart import MIMEMultipart
import random
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from time import sleep
from dialect import translate

def send(link):
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    f = open('mail.html', 'rb')
    html = f.read()
    f.close()
    # Create a text/plain message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hello Marathoner!"
    msg['From'] = 'kilonet@1gb.ru Aleksei Marathon Mail'
    msg['To'] = 'kpdpok@gmail.com'

    html += '<br><br>Вот тебе линк на <a href="%s">марафон</a>' % (link)
    part1 = MIMEText(html, 'html')
    msg.attach(part1)

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('smtp-56.1gb.ru', port=465)
    s.login('u268923', '842a19f4')
    s.sendmail('kilonet@1gb.ru', ['kpdpok@gmail.com'], msg.as_string())
    s.quit()

if __name__ == '__main__':
    while True:
        links = translate('http://www.aimsworldrunning.org/Calendar.htm ')
        link = links[random.randint(0, len(links))]
        send(link)
        print 'sent on %s' % (str(datetime.utcnow()))
        secs = random.randint(0 * 3600, 3 * 3600)
        sleep(secs)