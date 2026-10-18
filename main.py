# Last modified: 10/17/2026
# Description: Sort Pictures by months
import os
from pathlib import Path
import sys 
import time
import shutil

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

dir_path = Path(os.getcwd()) 

possible_extensions = {".jpg",".heic",".png"}

for month in months:
    # the month folder doent already exist create it
    if not month:
        os.mkdir(month)
    
# for every path in the program directory find the images
for item in dir_path.iterdir():
    if item.suffix in possible_extensions:
        

        try:
            # get the time metadata
            c_time = os.path.getctime(item) # returns epoch seconds created
            local_time = time.ctime(c_time) # convert to usable time stamp
            print(f"{local_time}")
            month = local_time[4:7] # get the month from time stamp string
            
            shutil.move(item,month)
            print(f"{item.name} moved to month {month}")
            

        except OSError:
            print("Path '%s' does not exists or is inaccessible" %item)
            sys.exit()

        # convert ctime in
        # seconds since epoch
        # to local time
        # extract month
        
        



"""managed to make directory for every month and access file meta data"""

