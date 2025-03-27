from datetime import datetime
from pathlib import Path
import os
import requests
from dotenv import load_dotenv
from download_image import download_image

def fetch_nasa_epic(token):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    epics = response.json()

    for epic_number, epic in enumerate(epics, start=1):
        link = 'https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png'
        date = datetime.fromisoformat(epic['date'])
        converted_date = date.strftime("%Y/%m/%d")
        image = epic['image']
        formatted_link = link.format(converted_date, image)
        download_image(formatted_link, f'images/epic{epic_number}', params=params)


if __name__ == '__main__':
    Path('images').mkdir(exist_ok=True)
    load_dotenv()
    token = os.environ['NASA_TOKEN']
    fetch_nasa_epic(token)