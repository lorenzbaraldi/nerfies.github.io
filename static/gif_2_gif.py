# create a gif of gif

import os
import imageio
from PIL import Image
import matplotlib.pyplot as plt

# ['from_gif', 'from_disk_images']
mode= 'from_disk_images'

frames_1 = []
frames_2 = []
frames_3 = []
frames_4 = []
captions = []

if mode == 'from_gif':
    # Load four GIFs
    gif1 = Image.open('elsa.gif')
    gif2 = Image.open('elsa.gif')
    gif3 = Image.open('elsa.gif')
    gif4 = Image.open('elsa.gif')

    while True:
        try:
            frames_1.append(gif1.copy())
            gif1.seek(len(frames_1))  # Move to the next frame
        except EOFError:
            break

    # Extract frames from GIFs
    frame1 = gif1.convert('RGBA')

    # Create a figure with 2x2 subplots
    for i in range(0, len(frames_1)):
        fig, axs = plt.subplots(2, 2, figsize=(8, 8))
        if mode == 'from_disk_images':
            fig.suptitle(f'Correct caption to place here')

        else:
            fig.suptitle('Global Title')
            #fig.suptitle('Global Title', fontsize=16, fontweight='bold')

        # Display each frame in a subplot
        axs[0, 0].imshow(frames_1[i])
        axs[0, 0].axis('off')
        axs[0, 0].set_title('DF-IF')

        axs[0, 1].imshow(frames_1[i])
        axs[0, 1].axis('off')
        axs[0, 1].set_title('SD-1.4')

        axs[1, 0].imshow(frames_1[i])
        axs[1, 0].axis('off')
        axs[1, 0].set_title('SD-2.1')

        axs[1, 1].imshow(frames_1[i])
        axs[1, 1].axis('off')
        axs[1, 1].set_title('SD-XL')

        plt.tight_layout()
        plt.savefig(f'frame_list/output_{i}.png')

elif mode == 'from_disk_images':
    # load 6 images from different generators, following the order
    # store in a list the captions
    n_frames= 8
    for idx, el in enumerate(os.listdir('static/images/d3_images')):
        if idx < n_frames:
            frames_1.append(Image.open('static/images/d3_images/'+el+'/'+el+'_img_gen0.png'))
            frames_2.append(Image.open('static/images/d3_images/'+el+'/'+el+'_img_gen1.png'))
            frames_3.append(Image.open('static/images/d3_images/'+el+'/'+el+'_img_gen2.png'))
            frames_4.append(Image.open('static/images/d3_images/'+el+'/'+el+'_img_gen3.png'))

            with open('static/images/d3_images/'+el+'/'+el+'_prompt.txt', 'r') as f:
                txt= f.read()
            captions.append(txt)
        else: break    

    # Create a figure with 2x2 subplots
    for i in range(0, len(frames_1)):
        fig, axs = plt.subplots(2, 2, figsize=(8, 8))
        fig.suptitle(f'{captions[i]}')
        #fig.suptitle('Global Title', fontsize=16, fontweight='bold')

        # Display each frame in a subplot
        axs[0, 0].imshow(frames_1[i])
        axs[0, 0].axis('off')
        axs[0, 0].set_title('DF-IF')

        axs[0, 1].imshow(frames_2[i])
        axs[0, 1].axis('off')
        axs[0, 1].set_title('SD-1.4')

        axs[1, 0].imshow(frames_3[i])
        axs[1, 0].axis('off')
        axs[1, 0].set_title('SD-2.1')

        axs[1, 1].imshow(frames_4[i])
        axs[1, 1].axis('off')
        axs[1, 1].set_title('SD-XL')

        plt.tight_layout()
        plt.savefig(f'static/images/frame_list/output_{i}.png')

print('done')
val=''




# from a list of COMLETE frames, create a gif
#gif_path = 'output.gif'
#frames[0].save(gif_path, format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)