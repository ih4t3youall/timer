from playsound import playsound
import sys
import time


if len(sys.argv) < 2:
    print('you need to pass as parameter an integer, will be the amount of minutes.')
    exit()

try:
    sleep_time = int(sys.argv[1])
except ValueError:
    # Handle the exception
    print('The number should be an integer')
    exit()

time.sleep(sleep_time*60)
playsound('alarm.mp3')
