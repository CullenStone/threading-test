Coding Assignment - SAV


A few assumptions were made while creating this script.
	1. The list of timestamps given at the begging of each day is an ordered list (earliest to latest)
	2. The list of timestamps will be given in a text file (timestamps.txt)

This script will run until the last timestamp has been run/last API called.

To run this script, make sure there is a timestamps.txt file, so it can open and read the desired times.

For testing purposes, I made times close to the current time, and ran the script with ssh. 'python run.py'
	- using python 3.7

I also used logging to log the times the API calls were made, it would append to this file, to show when the GET requests were made.
	- This file is not in the folder, it will create it when the script is ran.

I used threading to handle parallel API calls (if two timestamps were at the same time)

Thank you,

Cullen

