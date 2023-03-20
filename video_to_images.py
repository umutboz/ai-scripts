"""
Convert each frame in a anime video to 256 x 256 images
"""
import os
import imageio.v3 as iio
import argparse
from PIL import Image
#from skimage.transform import resize


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video-path', type=str, default='/videos')
    parser.add_argument('--save-path', type=str, default='/dataset')
    parser.add_argument('--frame_splitter', type=int, default=100)
    parser.add_argument('--size', default=(512,512))

    return parser.parse_args()
    
    
if __name__ == '__main__':

    args = parse_args()

    frame_counter = 0
    for idx, frame in enumerate(iio.imiter(args.video_path)):
        frame_counter = frame_counter + 1
        if (frame_counter % args.frame_splitter) == 0:
            img = Image.fromarray(frame)
            img_resize = img.resize(args.size, Image.LANCZOS)
            iio.imwrite(f"{args.save_path}/frame{idx:03d}.jpg", img_resize)
