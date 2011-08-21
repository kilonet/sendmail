# Import smtplib for the actual sending function
from email.mime.multipart import MIMEMultipart
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
f = open('mail.txt', 'rb')
html = f.read()
f.close()
# Create a text/plain message
msg = MIMEMultipart('alternative')
msg['Subject'] = "hello py"
msg['From'] = 'kilonet@1gb.ru <Aleksei Marathon Mail>'
msg['To'] = 'kpdpok@gmail.com'

part1 = MIMEText(html, 'html')
msg.attach(part1)

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp-56.1gb.ru', port=465)
s.login('u268923', '842a19f4')
s.sendmail('kilonet@1gb.ru', ['kpdpok@gmail.com'], msg.as_string())
s.quit()