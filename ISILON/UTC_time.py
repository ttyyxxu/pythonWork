import time,datetime
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

## Print UTC time
print(datetime.datetime.fromtimestamp(1617947400).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.fromtimestamp(1617941400).strftime("%Y-%m-%d %H:%M:%S"))

