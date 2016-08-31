import threading
import ActivitySummaryFetcher
import sys

duration = 10.0
userName = ''
password = ''

def callAPI():
	'''
		This function schedules a call to FitBit API every 10 minutes to fetch the user activity.
	'''
	threading.Timer(duration, callAPI).start() # Call after 10 mins
	ActivitySummaryFetcher.getActivityLog(userName, password)

def registerUser(time, user_name, passwd):
	global duration, userName, password
	duration = time
	userName = user_name
	password = passwd
	callAPI()