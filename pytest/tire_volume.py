import math

width = float(input("Enter the width of the tire: "))
aspect_ratio = float(input("Enter the aspect ratio: "))
diameter = float(input("Enter the diameter: "))

#Formula
volume = math.pi *width**2*aspect_ratio*(width*aspect_ratio + 2540*diameter)/10000000000

#Rounding off
volume = round(volume,2)

print(f"The volume is : {volume}")
print()

#Get current date
from datetime import datetime
current_date = datetime.now()
print(f'{current_date:%y-%m-%d}')
print()

#Open text file for appending
with open('volumes.txt', "a") as b:

    print(f'{current_date:%y-%m-%d}\n{width}\n{aspect_ratio}\n{diameter}\n{volume}')
    b.write(f'{current_date:%y-%m-%d} {width} {aspect_ratio} {diameter} {volume}')


