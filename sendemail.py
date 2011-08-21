# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open('mail.txt', 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp-56.1gb.ru', port=465)
s.login('u268923', '842a19f4')
s.sendmail('kilonet@1gb.ru', ['kpdpok@gmail.com'], msg.as_string())
s.quit()