import torch
from PIL import Image
import numpy as np
import os


def to_tensor(root: str = 'data/images/', RGBA: bool = False) -> torch.Tensor:
    """
    Convert images to a tensor.

    Args:
        root (str, optional): path to images.
        RGBA (bool, optional): if True, RGBA. else, RGB.

    Returns:
        torch.Tensor: tensor of images.
    """
    images = []
    image_names = os.listdir(root)
    for image_name in image_names:
        image = Image.open(os.path.join(root, image_name))
        images.append(np.array(image))
    images = np.array(images)[:, :, :, :(3 + RGBA)]
    images = np.transpose(images, (0, 3, 1, 2))
    images = torch.tensor(images)
    return images
