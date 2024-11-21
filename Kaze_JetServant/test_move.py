import asyncio
from jetracer.nvidia_racecar import NvidiaRacecar

car = NvidiaRacecar()
car.steering = 0
car.throttle = 0

print("now looping")
while(True):
    """    i = -1
    while(i<1):
        car.throttle = 0
        car.steering = i*0.01
        i += 0.2"""
    car.steering = 0
    car.throttle = 0