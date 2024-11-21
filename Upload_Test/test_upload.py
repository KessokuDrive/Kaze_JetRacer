import numpy as np
import asyncio
from jetcam.csi_camera import CSICamera
#from jetcam.utils import bgr8_to_jpeg
import cv2  # OpenCV
import pillow_heif
# camera = CSICamera(width=640, height=480, capture_fps=24)
import uvloop
from websockets.client import connect

import io

# Change to async
async def ws_send(data=None,close=False):
    """
    :param data: the data need to send, 
        will be force converted to bytes before sent
    
    """
    async with connect("ws://192.168.31.7:8765",
                       ping_timeout=None,
                       compression=None,
                       ping_interval=None,
                       write_limit=None,
                       ) as websocket:    
        if(len(data)>0):
            print("Now send")
            #await websocket.send(str(np.asarray(data)))
            #print(len(data.data))
            await websocket.send(bytes(data.data))
            #await websocket.send(b'')
            # await websocket.send("233")
            xy = await websocket.recv()
            print(f"Received: {xy}")
           # websocket.close()
            
#Capture Image
#raw_image = camera.read()
def demo(raw_image):

    heif_file = pillow_heif.from_bytes(
        mode="BGR",
        size=(raw_image.shape[1], raw_image.shape[0]),
        data=bytes(raw_image)
    )
    # heif_file.save("output.heif", quality=60)
    # print("done saving")
    # heif_file = pillow_heif.read_heif("output.heif")
    uvloop.install()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(ws_send(heif_file)) 