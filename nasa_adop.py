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
    
def downaload_images(response_apod):
    apod_photos = []
    for url_on_photo in response_apod.json():
        adop_images = url_on_photo['url']
        if os.path.splitext(adop_images)[1] in ['.jpg', '.png']:
            apod_photos.append(adop_images)
    
    for image_number, image in enumerate(images, start=1):
        download_image(image, f'images/nasa_adop{image_number}.jdg')

            
if __name__ == '__main__':
    Path('images').mkdir(exist_ok=True)
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    response_apod = fetch_nasa_adop(token)
    download_images(response_apod)
    
