The purpose of this repository is to allow someone to always know the public IP (also called external IP) of their home network, even when away from home.

The intended use of this repository is in conjuction with a task schedule, such as Windows Task Scheduler, or perhaps a custom task scheduling system, that can periodically run the main.py script from a networked 
computer, such as a home server.

When main.py is executed it checks whether the network's public IP address has changed since the last time the program was run. If a change is detected, then the program sends a notification email to the destination of your choice.

Please remember to assign email address, email host, and password information in the main.py script so that notification emails can be sent. Be advised that this program cannot send emails from email addresses that require multi-factor authentication.
