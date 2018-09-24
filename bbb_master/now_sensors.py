import Adafruit_BBIO.ADC as ADC
import datetime
import sys



#setup and constants
ADC.setup()
P_temp = "P9_37"
P_light = "P9_40"



#measure
time_ = str(datetime.datetime.now())
t = 0
for i in range(n):
    t += ADC.read(P_temp) * 0.18 * 1000
    # t += 0.35
temp_ = str(t / n)
light_ = 1.0 - ADC.read(P_light)

sen1_ = 'na'
sen2_ = 'na'
sen3_ = 'na'

sensors_data = [temp_, light_, sen1_, sen2_, sen3_]

#output

sys.stdout.write(time_ + '\t' + '\t'.join(sensors_data))
