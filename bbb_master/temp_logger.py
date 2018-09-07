#ver. 0.01
#import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import datetime
import sys

#setup and constants
ADC.setup()
P_data = "P9_40"
#f_log = "../../data_logs/light.log"
f_log = "light.log"
i = 500
#main


for j in range(i):

    with open(f_log, 'a') as iFile:
        iFile.write(str(datetime.datetime.now())+\
 "\t" + str(ADC.read(P_data))+"\n")
    time.sleep(1200)
    sys.stderr.write(str(j)+ "\n")

