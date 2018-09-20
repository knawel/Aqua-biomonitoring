#sensor logger, ver. 1.0
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time
import datetime
from datetime import timedelta
import numpy as np

# SENSOR DATA IS: <TEMP>  <LIGHT>   <SEN1>  <SEN2>  <SEN3>

def write_last(sens_data, time_now, time_delta, fname):

    #write the last data
    with open(fname, 'a') as iFile:
        iFile.write(time_now + \
                    "\t" + "\t".join([str(x_) for x_ in sens_data]) + "\n")

    #read the file
    sens_all_dat = []
    time_all_dat = []
    time_all_str = []
    with open(fname, "r") as iFile:
        for i_ in iFile:
            j_ = i_.strip().split('\t')
            time_ = j_[0]
            sens_ = j_[1:]
            sens_all_dat.append(sens_)
            time_all_str.append(time_)
            time_all_dat.append(datetime.datetime.strptime(time_, "%Y-%m-%d %H:%M:%S.%f"))
    time_all_dat = np.array(time_all_dat)
    sens_all_dat = np.array(sens_all_dat)
    time_all_str = np.array(time_all_str)

    #remove far than time_lenght
    time_short = time_all_str[time_all_dat[-1] - time_all_dat < time_delta]
    sens_short = sens_all_dat[time_all_dat[-1] - time_all_dat < time_delta]
    with open(fname, 'w') as iFile:
        for ii in range(len(time_short)):
            iFile.write(time_short[ii] + "\t"\
                        + "\t".join([str(x_) for x_ in sens_short[ii]]) + "\n")



#setup and constants
ADC.setup()
P_temp = "P9_37"
P_light = "P9_40"

f_log = "sensors.log"
days_records = 60.0 # 60 days of records
sleep_time = 15.0*60 # every 15 mins
n_reps = days_records * 24 * 60 * 60 / sleep_time

n = 3 # number of measurements for temp

                #main loop

for j in range(n_reps):
    time_ = str(datetime.datetime.now())

    ### measure ###
    #temperature
    t = 0
    for i in range(n):
        t += ADC.read(P_temp) * 0.18 * 1000
        # t += 0.35
    temp_ = str(t/n)
    #light
    light_ = 1.0 - ADC.read(P_data)
    # light_ = 0.1

    sen1_ = 'na'
    sen2_ = 'na'
    sen3_ = 'na'

    sensors_data = [temp_, light_, sen1_, sen2_, sen3_ ]

    ## save ##
    #main
    with open(f_log, 'a') as iFile:
        iFile.write(time_ + "\t"\
                    + "\t".join([str(x_) for x_ in sensors_data]) + "\n")


    #24h
    td = timedelta(hours=24)
    write_last(sensors_data, time_, td, "24h_" + f_log)
    #7 days
    td = timedelta(days=7)
    write_last(sensors_data, time_, td, "7d_" + f_log)
    #30 days
    td = timedelta(days=30)
    write_last(sensors_data, time_, td, "30d_" + f_log)

    ##sleep##
    time.sleep(sleep_time)

