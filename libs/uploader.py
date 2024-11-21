from websockets.sync.client import connect

def coord2cmd(x,y):
    return '{:.2f}'.format(x)+" "+'{:.2f}'.format(y)

def send_ws(websocket, msg):
    websocket.send(msg)
    
async def async_send_ws(websocket, command):
    await websocket.send(command)

def hello_world(URL,x,y):
    with connect(URL) as websocket:
        websocket.send(coord2cmd(x,y))
        message = websocket.recv()
        print(f"Received: {message}")
        websocket.close()

async def ws_send(URL,data=None,close=False):
    """
    :param data: the data need to send, 
        will be force converted to bytes before sent
    
    """
    async with connect(URL,
                       ping_timeout=None,
                       compression=None,
                       ping_interval=None,
                       write_limit=None,
                       ) as websocket:    
        if(len(data)>0):
            print("Now send")
            #await websocket.send(str(np.asarray(data)))
            #print(len(data.data))
            await websocket.send(data)
            #await websocket.send(b'')
            # await websocket.send("233")
            xy = await websocket.recv()
            print(f"Received: {xy}")
           # websocket.close()