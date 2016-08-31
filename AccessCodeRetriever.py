"""
This is a support module for FitBit to automate the process of Access Code retrieval.

"""

import mechanize

def getAcessCodeUrl(userName, password, auth_url):
	""" 
		This function sends a request to fetch the login form and then sutomatically fills the form details to retrieve the redirect url.
	"""

	br = mechanize.Browser() 
	br.set_handle_robots(False)

	br.addheaders = [("User-agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"), ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"), ("Accept-Charset", "ISO-8859-1,utf-8;q=0.7,*;q=0.3"), ("Accept-Encoding", "none"), ("Accept-Language", "en-US,en;q=0.8"), ("Connection", "keep-alive")] 

	response = br.open(auth_url)

	formcount = getFormCount(br)
	br.select_form(nr=formcount)

	br.set_all_readonly(False)

	#print br.form	# Print the form fields

	br.form.set_value(userName, nr=5)
	br.form.set_value(password, nr=6)

	br.method = "POST"
	response = br.submit()
	responseUrl = response.geturl()

	#print responseUrl	# Print the Access_Code_Url
	
	return getAccessCode(responseUrl)

def getFormCount(br):
	""" 
		Function to return the form number[Multiple forms available on the page] to be filled in order to login
	"""
	formcount=0
	for frm in br.forms():  
		if str(frm.attrs["id"])=="loginForm":
			break
		formcount=formcount+1
		return formcount
		
def getAccessCode(responseUrl):
	""" 
		Function to extract and return the Access Code from the url
	"""
	print responseUrl
	try:
		startIndex = responseUrl.index("code=") + 5
		endIndex = responseUrl.index("#_=_")
		code = responseUrl[startIndex: endIndex]
		return code
	except ValueError:
		print 'Authentication Not Successful!'
		exit()