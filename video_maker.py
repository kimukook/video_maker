"""
This is a script that creates the video that is comprised of a sequence of images in the given folder.

=====================================
Author  :  Muhan Zhao
Date    :  Nov. 27, 2021
Location:  UC San Diego, La Jolla, CA
=====================================
"""
import cv2
import os
import argparse


def video_maker(folder_path, video_name, image_type, save_path, quiet=True):
    """
    This function generates the video from the images in the given folder
    --------------------

    Example             :       In command line, navigate to the folder of this script, try the code below,
                                python3 video_maker.py --folder_path <the path of folder> --image_type '.png' --video_name 'video.avi'

    --------------------

    Parameters

    :param folder_path  :       String, the path of the folder containing images
    :param video_name   :       (Optional)String, the name of the video to be generated, default to be 'video.avi'
    :param image_type   :       (Optional)String, the suffix of images, default to be '.png'
    :param save_path    :       (Optional)String, the saving path of the upcoming video, default to be the same as
                                folder_path
    :param quiet        :       (Optional)Boolean, show the process of video making

    --------------------
    :return             :       None
    """
    if save_path is None:
        save_path = folder_path

    images = [img for img in os.listdir(folder_path) if img.endswith(image_type)]

    frame = cv2.imread(os.path.join(folder_path, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(os.path.join(save_path, video_name), 0, 1, (width, height))

    for i, image in enumerate(images):
        if not quiet:
            print(f' processing image No.{i}....')
        video.write(cv2.imread(os.path.join(folder_path, image)))

    cv2.destroyAllWindows()
    video.release()
    print('Done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_path', required=True, default=None, type=str,
                        help="Enter the folder path containing the images")

    parser.add_argument('--image_type', required=False, default='.png', type=str,
                        help="Enter the suffix of image files")

    parser.add_argument('--video_name', required=False, default='video.avi', type=str,
                        help="Enter the name for the video to be saved")

    parser.add_argument('--save_path', required=False, default=None, type=str,
                        help="Enter the saving path for the video")

    parser.add_argument('--quiet', required=False, default=True, type=bool,
                        help="Quiet mode in video making function")

    args = parser.parse_args()
    video_maker(args.folder_path, args.video_name, args.image_type, args.save_path, args.quiet)
