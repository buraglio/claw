#!/usr/bin/env python

# Python CLAW Configuration fiLer And Watcher
# An alternative to the venerable RANCID, CLAW is intended to provide a low overhead, easy to impliment, git based change control tool for network equipment.
# Proof of concept and software architecture by Nick Buraglio < nick (at) buraglio (dot) com >
# significant contributions by Brandon X, Brandon Carrel, Paul Wefel

import sys
import pxssh
import paramiko
import git
import smtplib
from email.mime.text import MIMEText

def editFile( configFile ):
        #Called when script is run with -p flag.
        #Needs to look through the config file generated and remove
        #passwords and other sensitive information. Should be
        #independent of the machine.

repo = git.Repo( "/home/insertrepo" )
index = repo.index
file = open( 'hostFile', 'r' )

fromAddress = file.readline()[:-1]
toAddress = file.readline()[:-1]
subject = file.readline()[:-1]

while file.readline():
        hosts = file.readline()[:-1].split( ',' )
        username = file.readline()[:-1]
        password = file.readline()[:-1]
        commands = file.readline()[:-1].split( ',' )

        for host in hosts:

                client = paramiko.SSHClient()

                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect( host, username=username, password=password )

                for command in commands:
                        configFileName = host + "-" + command.replace( " ", "-" )
                        configFile = open( configFileName, 'w' )

                        stdin, stdout, stderr = client.exec_command( command )

                        configFile.write( stdout.read() )

                        if len( sys.argv ) == 2 and sys.argv[1] == '-p':
                                editFile( configFile )

                        configFile.close()

                        index.add( [configFileName] )

                client.close()

file.close()

diff = repo.git.diff( '--staged' )

if diff:
        index.commit( configFileName )
        message = MIMEText( diff )

        message['From'] = fromAddress
        message['To'] = toAddress
        message['Subject'] = subject

        s = smtplib.SMTP( 'localhost' )
        s.sendmail( fromAddress, [toAddress], message.as_string() )
        s.quit()
