# create final gif

import os
from PIL import Image
import imageio

path='static/images/frame_list'
frames= []
for el in os.listdir(path):
    el
    img= Image.open(path+'/'+el)
    frames.append(img)

gif_path = 'static/images/output.gif'
gif_path_pil = 'static/images/output_pil.gif'
gif_path_no_compression = 'static/images/output_no_compression.gif'
imageio.mimsave(gif_path_no_compression, frames, format='GIF', fps=1, loop=0) #example 1

frames[0].save(gif_path, format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0, optimize=False, quality=100) #example 2

with Image.open('static/images/frame_list/output_0.png') as img:
    img.save(gif_path_pil, save_all=True, append_images=frames[1:], duration=500, loop=0, optimize=False, quality=100) #example 3
