import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from download_image import download_image, fetch_file_extension


def fetch_nasa_apod(token):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'count':'45', 'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    Path('images').mkdir(exist_ok=True)
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    apods = fetch_nasa_apod(token)
    for apod_number, apod in enumerate(apods, start=1):
        if fetch_file_extension(apod['url']):
            download_image(apod['url'], f'images/nasa_apod{apod_number}')