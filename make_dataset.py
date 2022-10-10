import os
import shutil
from tqdm import tqdm
import argparse


def main(root, resolution, output_dir):
    assert resolution in ['32', '64', '128'], 'Resolution must be 32, 64 or 128'
    cat_dir = os.path.join(root, 'png/labeled/' + resolution)
    categories = os.listdir(cat_dir)
    os.makedirs(output_dir, exist_ok=True)
    for cat in tqdm(categories, desc=f'copy to "{output_dir}"'):
        img_dir = os.path.join(cat_dir, cat)
        for img_name in os.listdir(img_dir):
            img_path = os.path.join(img_dir, img_name)
            shutil.copyfile(img_path, os.path.join(output_dir, img_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Make dataset')
    parser.add_argument('--root', type=str, default='joypixels-7.0-free', help='Path to the downloaded directory. default: "joypixels-7.0-free"')
    parser.add_argument('--resolution', type=str, default='64', help='The resolution of the images. default: 128')
    parser.add_argument('--output_dir', type=str, default='data/images', help='Path to the output directory. default: "data/images"')
    args = parser.parse_args()
    main(**vars(args))