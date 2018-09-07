#ver. 0.01
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
#main


for j in range(i):

    with open(f_log, 'a') as iFile:
        time_ = str(datetime.datetime.now())
        temp_ = str(ADC.read(P_temp) * 0.18 * 1000)
        iFile.write(time_ + "\t" + temp_ +"\n")
    time.sleep(12)
    sys.stderr.write(str(j)+ "\n")

