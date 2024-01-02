# create final gif

import os
from PIL import Image

path='static/images/frame_list'
frames= []
for el in os.listdir(path):
    el
    img= Image.open(path+'/'+el)
    frames.append(img)

gif_path = 'static/images/output.gif'
frames[0].save(gif_path, format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0)
# duration: time between frames in milliseconds
