from jetracer.nvidia_racecar import NvidiaRacecar
import asyncio
from websockets.asyncio.server import serve

Car = NvidiaRacecar()

import asyncio
import websockets

async def detection(websocket):
        data = await websocket.recv()
        cmd = data.split()
        x,y = cmd
        Car.steering = (float(x))
        Car.throttle = (float(y))
        print("Gear {}, throttle {} ようそろ".format(x,y))
        await websocket.send("Gear {}, throttle {} ようそろ".format(x,y))

async def main():
    async with serve(detection,
                     "0.0.0.0",
                     8765,
                     max_size= 5000000,
                     ping_timeout=None,
                     compression=None,
                     ping_interval=None,
                     write_limit=[10000000,300000]):
        print("Server started")
        await asyncio.get_running_loop().create_future()  # run forever


if __name__ == "__main__":

    asyncio.run(main())