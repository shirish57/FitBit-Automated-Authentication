# FitBit-Automated-Authentication-
Automated FitBit authentication and API Calls

The project provides the automatic authorization for the users who trying to access Fitbit API. After one time manual authorization, the project automatically refreshes the token which expires every 8 hours [1] and the new refreshed token and the access-token will be saved in a file. According to the FitBit API, the token expires every 8 hours and we need to get a new token for the authorization again. It then reads the saved token from the file and re-authorizes the program and saves the new token in the file.

FitBit allows 150 API calls per day [2], so the program calls the API every 9.6 minutes and stores the user data in a file.

Usage: ```python MainApp <Duration> <UserName> <Password>```


# References:
[1] Access Token Request, https://dev.fitbit.com/docs/oauth2/

[2] Rate Limits, https://dev.fitbit.com/docs/basics/
