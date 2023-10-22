import time
import datetime
import urllib.request
from threading import Thread
import logging

# Created a logger that will keep track of the API calls, writing them to a file called 'log_file.log' -> will create this
log_file = "log_file.log"
logging.basicConfig( filename = log_file,filemode = 'a',level = logging.INFO,format = '%(asctime)s - %(levelname)s: %(message)s',\
                     datefmt = '%m/%d/%Y %I:%M:%S %p' )


# This function will make a GET request to the specified API. Logs time in 'log_file.log'
def call_api(url):
	content = urllib.request.urlopen(url).read()
	logging.info("API Call to 'ifconfig.io")

# If there are multiple calls that need to be made at the same time, it uses threading to parallel process them.
def threading_api_call(nthreads, url):
	threads = []

	for i in range(nthreads):
		t = Thread(target=call_api, args=(url,))
		threads.append(t)

	[t.start() for t in threads]

	[t.join() for t in threads]


# Main function
if __name__ == "__main__":

	# The URL we are making a GET request from
	url = "https://ifconfig.io"

	times = []
	# Opens txt file with timestamps and writes it to 
	with open("timestamps.txt", "r") as t:
		times = [x.replace('\n', '') for x in t]

	# Converts the datetime strings to type datetime.
	times = [datetime.datetime.strptime(t, '%H:%M:%S') for t in times]

	time_dict = {}

	# Makes a dictionary of the timestamps, with key -> timestamp, value -> number of requests to be made
	for i in range(len(times)):
		if times[i] not in time_dict:
			time_dict[times[i]] = 1
		else:
			time_dict[times[i]] += 1

	# Goes through each of the elements in the dictionary.
	for t in time_dict:
		ct = datetime.datetime.today()
		# Finds the time difference and sleeps the script until the next timestamp
		next_time = datetime.datetime(year = ct.year, month = ct.month, day = ct.day, hour = t.hour, minute = t.minute, second = t.second)
		time.sleep((next_time - ct).total_seconds())

		# Once time is over, the script makes a call to the API at the correct time
		threading_api_call(time_dict[t], url)
		






