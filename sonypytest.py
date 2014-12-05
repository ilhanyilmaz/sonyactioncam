from sonypy import Discoverer, Camera

discoverer = Discoverer()
cameras = discoverer.discover()
print cameras

if len(cameras) > 0:
    cam = cameras[0]
    cam.act_take_picture()
else:
    print "No camera"
