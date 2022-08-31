import time
import os
import shutil
import datetime
import glob
import sys
import pathlib
outputs=os.path.dirname(os.path.abspath(__file__))


all_files=list(os.listdir(outputs))

for files in all_files:
    try:
        inputs=glob.glob(files+"\\*")
        for ele in inputs:
            shutil.move(ele,outputs)
        shutil.rmtree(files)
    except:
        pass

for file in os.listdir('.'):
    if file=='organize.py' or file=='run.ps1':
        continue
    time_format=time.gmtime(os.path.getmtime(file))
    datetime_object=datetime.datetime.strptime(str(time_format.tm_mon),"%m")
    full_month_name=datetime_object.strftime("%b")
    dir_name=str(time_format.tm_year)+'-'+\
        str(time_format.tm_mon)+'-'+\
        str(time_format.tm_mday)
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    dest=dir_name
    shutil.move(file,dest)

print("done")
wait=input("press any key to exit")





