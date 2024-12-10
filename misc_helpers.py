from typing import List
import requests
from PIL import Image
from io import BytesIO


def getPNGfromImgUrl(url: str) -> bytes | None:
    """
    Fetches an image from a given URL and returns the PNG data.

    Args:
        url (str): The URL of the image to fetch.

    Returns:
        bytes | None: The PNG data of the fetched image, or None if an error occurred.
    """
    # Fetch the image
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using Pillow
        imgData = Image.open(BytesIO(response.content))
        # imgData.show()

        return imgData._repr_png_()
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")
        return None


def getPNGsFromImgUrls(urls: List[str]) -> List[bytes]:
    """
    Fetches multiple images from a list of URLs and returns a list of PNG data.

    Args:
        urls (list[str]): A list of URLs of the images to fetch.

    Returns:
        list[bytes]: A list of PNG data of the fetched images.
    """
    pngs = []
    for url in urls:
        png = getPNGfromImgUrl(url)
        if png is not None:
            pngs.append(png)
    return pngs


def saveImageFromUrl(url: str, filename: str) -> None:
    """
    Fetches an image from a given URL and saves it to a file.

    Args:
        url (str): The URL of the image to fetch.
        filename (str): The name of the file to save the image to with qualifying file extension.
                        Example: 'avatar.jpg'
    """
    # Fetch the image
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image using Pillow
        imgData = Image.open(BytesIO(response.content))
        # imgData.show()

        # Save the image
        imgData.save(filename)
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")
