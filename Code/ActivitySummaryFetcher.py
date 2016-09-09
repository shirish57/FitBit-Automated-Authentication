import MyFitbit, json
import AccessCodeRetriever
import time

def getActivityLog(userName, password):
	tokenfile = "user_settings.txt"
	activityLogFile = "activity_log.txt"
	currentDate = time.strftime("%Y-%m-%d")

	z = MyFitbit.KHealthFitbit()

	# Try to read existing token pair
	# try:
		# token = json.load(open(tokenfile))
		# print "Getting tokens from saved file :\n\n access_token = "+ token['access_token'] +" \n\n refresh_token == ", token['refresh_token']
	# except IOError:
		# If not generate a new file
	# Get the authorization URL for user to complete in browser.
	auth_url = z.GetAuthorizationUri()
   
	'''   
	chromedriver = "C:/Users/jpsain/Downloads/chromedriver_win32"
	os.environ["webdriver.chrome.driver"] = chromedriver
	driver = webdriver.Chrome(chromedriver)
	driver.get(auth_url)
	print driver.current_url
	
	''' 
	
	print "Please visit the link below and approve the app:\n %s" % auth_url + "\n"
	
	# Fetch the access_code from the auth_url. Set the access code that is part of the arguments of the callback URL FitBit redirects to.
	access_code = AccessCodeRetriever.getAcessCodeUrl(userName, password, auth_url);
	print 'Access Code: ' + access_code + "\n"
	# access_code = raw_input("Please enter code (from the URL you were redirected to): ")
	
	# Use the temporary access code to obtain a more permanent pair of tokens
	print "Calling GetAccessToken()"
	token = z.GetAccessToken(access_code)
	print "Tokens are : ", token
	print "\n"
	# Save the token to a file
	print "calling json.dump()"
	json.dump(token, open(tokenfile,'w'))

	# Sample API call
	 #response = z.ApiCall(token, '/1/user/-/activities/log/steps/date/today/1d.json')
	# Possible API Calls, or read the FitBit documentation for the full list
	# (https://dev.fitbit.com/docs/), e.g.:
	#request_URL='/1/user/-/devices.json'
	#request_URL='/1/user/-/profile.json'
	#request_URL='/1/user/-/activities/date/2015-10-22.json'
	#request_URL='/1/user/-/activities/log/steps/date/today/7d.json'
	request_URL='/1/user/-/activities/date/' + currentDate + '.json'	# Current Date
	#request_URL='/1/user/[user-id]/activities/date/[date].json  : [user-id] = '-' for current logged-in user
	#request_URL='/1/user/-/activities.json'
	#request_URL='/1/user/-/activities/recent.json'
	#request_URL='/1/user/-/activities/frequent.json'
	#request_URL='/1/user/-/activities/favorite.json'
	#request_URL='/1/user/-/activities/goals/daily.json'
	#request_URL='/1/user/-/activities/goals/weekly.json'
	#request_URL='/1/user/-/foods/log/date/2015-03-01.json'
	#request_URL='/1/user/-/foods/log/caloriesIn/date/2015-03-01/7d.json'
	#request_URL='/1/user/-/foods/log/water/date/2015-03-01.json'
	#request_URL='/1/user/-/meals.json'
	#request_URL='/1/user/-/sleep/date/2015-03-01.json'
	#request_URL='/1/user/-/heart/date/2015-03-01.json'
	#request_URL='/1/user/-/bp/date/2015-03-01.json'
	#request_URL='/1/user/-/glucose/date/2015-03-01.json'
	#request_URL='/1/user/-/activities/date/'+ (datetime.date.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')+'.json'
	print 'Request URl : ' ,request_URL
	response = z.ApiCall(token, request_URL)
	print "Response after API call : ", response 
	# Token is part of the response. Note that the token pair can change when a refresh is necessary.
	# So we replace the current token with the response one and save it.
	token = response['token']
	json.dump(token, open(tokenfile,'w'))

	# Do something with the response
	#print "Welcome %s!" % response['user']['displayName']
	###print "\n\n", response['lifetime']['total']
	###print "\n\n", response['summary']['heartRateZones']

	try:
		print response['summary']['distances']
		json.dump(response['summary']['distances'], open(activityLogFile,'w'))	# Print the Activity Log
	except KeyError:
		print 'No Summary Available'