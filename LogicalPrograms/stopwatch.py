'''
@Author: Nikita
@Date: 2022-04-06 06: 30: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-04 7: 30: 00
@Title: Gambler
'''
import time

def time_convert(sec):     # it covert second into minutes and hours
    """
        Description:
            Function to calculate time in hour mins and sec format
        Parameter:
            passing second as a parameter
        Return:   
            returning the Lapsed Time n the format of hours and mins and sec 
    """	
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start")
start_time = time.time()

input("Press Enter to stop")
end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)               