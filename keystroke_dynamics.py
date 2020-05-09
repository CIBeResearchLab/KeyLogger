
'''
This piece of code computes the following:
1. Prints the Key Up and Key Down events as logged by keylogger.py
2. Hold Time
3. Latency - Press to Press, Press to Release, Release to Press, Release to Release
4. Error Rate
'''

#from pprint import pprint
from datetime import timedelta
count=0
i=0

with open('key_logs.txt') as logs_file:
	#reading the file
	logs=logs_file.read().splitlines()  

	#take a step of 2 because we are dealing with key up and key down for one key
	for i in range(1,len(logs)-2,2): 

		#pick 4 entries at a time for press to press, press to release, release to press and release to release
		key_1=logs[i].split()

		#splitting the time into hours, minutes and milliseconds
		time_1=key_1[1].split(':') 

		key_2=logs[i+1].split()
		time_2=key_2[1].split(':')
		key_3=logs[i+2].split()
		time_3=key_3[1].split(':')
		key_4=logs[i+3].split()
		time_4=key_4[1].split(':')

		#checking if we have the same consective pairs of key up/key down for the same key
		if key_1[3]==key_2[3] and key_3[3]==key_4[3]:

			#removing the , from say - 31,256 - used slicing hereas milliseconds do not exceed 60,000
			sec_1=str(time_1[2])[:-4]+str(time_1[2])[-3:]
			sec_2=str(time_2[2])[:-4]+str(time_2[2])[-3:]
			sec_3=str(time_3[2])[:-4]+str(time_3[2])[-3:]
			sec_4=str(time_4[2])[:-4]+str(time_4[2])[-3:]

			#using timedelta to later compute time differences
			t1=timedelta(hours=int(time_1[0]),minutes=int(time_1[1]),seconds=float(sec_1[2])/1000)
			t2=timedelta(hours=int(time_2[0]),minutes=int(time_2[1]),seconds=float(sec_2[2])/1000)
			t3=timedelta(hours=int(time_3[0]),minutes=int(time_3[1]),seconds=float(sec_3[2])/1000)
			t4=timedelta(hours=int(time_4[0]),minutes=int(time_4[1]),seconds=float(sec_4[2])/1000)

			#computing difference in time for press to press, press to release, release to press and release to release
			press_2_p=t3-t1
			press_2_r=t2-t1
			release_2_p=t4-t3
			release_2_r=t4-t2

			#printing the key with key up and key down timings
			print(f"{key_1[3]} was pressed on {key_1[0]} at hours={time_1[0]}, minutes={time_1[1]} and milliseconds={time_1[2]}")
			print(f"{key_2[3]} was released on {key_2[0]} at hours={time_2[0]}, minutes={time_2[1]} and milliseconds={time_2[2]}")

			#printing key hold time
			print(f"Hold Time is {str(press_2_r.microseconds)} in MilliSeconds")

			print(f"{key_3[3]} was pressed on {key_3[0]} at hours={time_3[0]}, minutes={time_3[1]} and milliseconds={time_3[2]}")
			print(f"{key_4[3]} was released on on {key_4[0]} at hours={time_4[0]}, minutes={time_4[1]} and milliseconds={time_4[2]}")

			#printing time difference in press to press, press to release, release to press and release to release
			print(f"MilliSeconds between press to press is {str(press_2_p.microseconds/1000)}")
			print(f"MilliSeconds between press to release is {str(press_2_r.microseconds/1000)}")
			print(f"MilliSeconds between release to press is {str(release_2_p.microseconds/1000)}")
			print(f"MilliSeconds between release to release is {str(release_2_r.microseconds/1000)}")
			print()
		else:
			continue # to code later for more complexities in key presses

	#computing the error rate
	for log in logs:
		key=log.split()
		if key[3]=='Key.backspace' or key[3]=='Key.delete':
			count=count+1

#computing the error rate stored in counter - Divide by 2 because each backspace or delete key will be counted twice 
#because of recording of press and release events
count=count/2
print(f"The Error Rate is {str(count)}")




		