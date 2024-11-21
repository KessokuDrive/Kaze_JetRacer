import cv2
import numpy as np
import pillow_heif
import cffi


SIZE = (1280,720)

heif_send = pillow_heif.read_heif("output.heif")
print(type(heif_send.data))
data_received = bytes(heif_send.data)
heif_received = pillow_heif.from_bytes("BGR",SIZE,data_received)

heif_received.save("received.heif")