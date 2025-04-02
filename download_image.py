from os.path import splitext
from urllib.parse import urlsplit
import requests
import os
import traceback


if not os.path.exists('images'):
    os.makedirs('images')


def save_photo_in_folder(file_name, image_link, image_number, *args):
    response = requests.get(image_link, *args)
    response.raise_for_status()

    with open(f'images/{file_name}_{image_number}.jpg', 'wb') as file:
        file.write(response.content)
        
def download_image(url, directory, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(f'{directory}{fetch_file_extension(url)}', 'wb') as image:
        image.write(response.content)


def fetch_file_extension(url):
    parsed_link = urlsplit(url)
    root, extension = splitext(parsed_link.path)
    return extension
