claw is intended to be a more streamlined, purpose built reimagination of the venerable network configuration management tool RANCID. 

The primary purpose of claw is to retreive and store configuration files for network hardware in a git repository. Its secondary goal is to provide notification of changes. As a value add it will remove passwords and perhaps check versions. 

It is flexible enough to add any command to, however, due to the bloat around RANCID it is not intended to do much else. 
My opinion is that inventory, disk space, flash statistics, hardware checking, etc. should all be handled by a proper network monitoring system performing real-time alerting if those items are deemed critical. 

INSTALL Notes: see README.install

Requirements: Python, network hardware supporting ssh. Since it is no longer 1997, telnet should not be used. It will not be supported in this build. If you feel that telnet is a requirement, I urge you to re-evaluate your security policy for managing critical infrastructure. 
