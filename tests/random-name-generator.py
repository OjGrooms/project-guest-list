import datetime
from time import sleep

for ii in range (10 ):
  basename = "randomname"
  suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
  fullname = "_".join([basename, suffix])
  print(fullname)
  sleep(1)