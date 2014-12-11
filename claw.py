#!/usr/bin/env python

# Python CLAW Configuration fiLer And Watcher
# An alternative to the venerable RANCID, CLAW is intended to provide a low overhead, easy to impliment, git based change control tool for network equipment.
# Proof of concept and software architecture by Nick Buraglio < nick (at) buraglio (dot) com >
# significant contributions by Brandon, Paul Wefel 


import sys
import git
import smtplib
import pxssh
