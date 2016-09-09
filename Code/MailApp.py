import Scheduler
import sys

duration = sys.argv[1]
userName = sys.argv[2]
password = sys.argv[3]


def main():
	'''
		Usage: Scheduler.registerUser(Time_In_Seconds, Username, Password)
	'''
	Scheduler.registerUser(duration, userName, password)

if __name__ == "__main__":
	main()