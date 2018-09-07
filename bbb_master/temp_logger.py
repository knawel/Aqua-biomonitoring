#ver. 0.02
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import datetime
import sys

#setup and constants
ADC.setup()
P_temp = "P9_37"
#f_log = "../../data_logs/light.log"
f_log = "temp.log"
i = 500
n = 3 # number of measurements
#main


for j in range(i):

    with open(f_log, 'a') as iFile:
        time_ = str(datetime.datetime.now())

        for i in range(n):
            t += ADC.read(P_temp) * 0.18 * 1000


        temp_ = str(t/n)
        iFile.write(time_ + "\t" + temp_ +"\n")
    time.sleep(12)
    sys.stderr.write(str(j)+ "\n")

