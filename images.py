# Copyright TU Wien (2022) - EVC: Task2
# Institute of Computer Graphics and Algorithms.

import numpy as np
import scipy.ndimage
import utils
from PIL import Image


def read_img(inp: str) -> Image.Image:
    """
    Returns a PIL Image given by its input path.

    Args:
        inp: The path to the input image.

    Returns:
        A PIL Image object.
    """
    img = Image.open(inp)
    return img


def convert(img: Image.Image) -> np.ndarray:
    """
    Converts a PIL image [0,255] to a numpy array [0,1].

    Args:
        img: A PIL Image object.

    Returns:
        A float numpy array of the image in range [0,1].
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: Loops, or functions that use loops internally, are forbidden for
    #       this task.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.array(img) / 255.0

    ### END STUDENT CODE

    return out


def switch_channels(img: np.ndarray) -> np.ndarray:
    """
    Swaps the red and green channel of an RGB image given by a numpy array.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W, 3) with the red and green channels swapped.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: Loops, or functions that use loops internally, are forbidden for
    #       this task.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = img.copy()
    out[:, :, 0] = img[:, :, 1]
    out[:, :, 1] = img[:, :, 0]

    ### END STUDENT CODE

    return out


def image_mark_green(img: np.ndarray) -> np.ndarray:
    """
    Returns a numpy-array (HxW) with 1 where the green channel of the input
    image is greater than or equal to 0.7, otherwise zero.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W) with 1 where the green channel is >= 0.7, otherwise 0.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: Loops, or functions that use loops internally, are forbidden for
    #       this task.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    mask = img[:, :, 1] >= 0.7

    ### END STUDENT CODE

    return mask


def image_masked(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
    Sets the pixels of the input image to zero where the mask is 1.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.
        mask: A numpy array of shape (H, W) with 1 where the pixel should be masked, otherwise 0.

    Returns:
        A numpy array of shape (H, W, 3) where the pixels are set to zero where the mask is 1.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: Loops, or functions that use loops internally, are forbidden for
    #       this task.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = img.copy()
    out[mask] = 0.0

    ### END STUDENT CODE

    return out


def grayscale(img: np.ndarray) -> np.ndarray:
    """
    Returns a grayscale image of the input. Use utils.rgb2gray().

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W) representing the grayscale image.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = utils.rgb2gray(img)

    ### END STUDENT CODE

    return out


def cut_and_reshape(img_gray: np.ndarray) -> np.ndarray:
    """
    Cuts the image in half (x-dim) and stacks it together in y-dim.

    Args:
        img_gray: A numpy array of shape (H, W) representing a grayscale image.

    Returns:
        A numpy array of shape (2*H, W/2) representing the cut and reshaped image.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    half = img_gray.shape[1] // 2
    left = img_gray[:, :half]
    right = img_gray[:, half:]
    out = np.vstack([right, left])

    ### END STUDENT CODE

    return out


def filter_image(img: np.ndarray) -> np.ndarray:
    """
    Filters the image with the gaussian kernel given below.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W, 3) representing the filtered image.
    """
    gaussian = utils.gauss_filter(5, 2)

    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: Functions like np.convolve, scipy.ndimage.convolve, or
    #       scipy.ndimage.correlate are forbidden for this task. This list is
    #       not exhaustive but serves as an example of forbidden functions.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    h, w, c = img.shape
    out = np.zeros_like(img)
    pad = 2
 
    for i in range(h):
        for j in range(w):
            for ch in range(c):
                val = 0.0
                for ki in range(5):
                    for kj in range(5):
                        ni = i + ki - pad
                        nj = j + kj - pad
                        if 0 <= ni < h and 0 <= nj < w:
                            val += gaussian[ki, kj] * img[ni, nj, ch]
                out[i, j, ch] = val

    ### END STUDENT CODE

    return out


def horizontal_edges(img: np.ndarray) -> np.ndarray:
    """
    Defines a sobel kernel to extract horizontal edges and convolves the image with it.

    Args:
        img: A numpy array of shape (H, W, 3) representing an RGB image.

    Returns:
        A numpy array of shape (H, W) representing the horizontal edges of the image.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    sobel = np.array([[ 1,  2,  1],
                      [ 0,  0,  0],
                      [-1, -2, -1]])
    out = scipy.ndimage.correlate(img, sobel, mode='constant', cval=0.0)

    ### END STUDENT CODE

    return out
