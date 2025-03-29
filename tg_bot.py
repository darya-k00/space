import argparse
import random
from time import sleep
from dotenv import load_dotenv
import os
import telegram


def publish_all_photos(directory, frequency, chat_id):
    while True:
        images = os.listdir(directory)
        random.shuffle(images)
        

def publish_one_photo(directory, photo, chat_id):
    for image in images:
            with open(f'{directory}/{image}', 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            frequency = 4
            sleep(frequency * 3600)

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=tg_token)
    chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser(
        description='This program allows to start publishing '
                    'photos on telegram channel.')
    parser.add_argument('chat_id', help="enter your chat ID")
    parser.add_argument('-p', '--photo',
                        help='enter the name of the photo to publish',
                        type=str,
                        default=f'{random.choice(os.listdir("images"))}')
    parser.add_argument('-f', '--frequency',
                        help='type how often you want to publish in hours',
                        type=int, default=4)
    parser.add_argument('-a', '--all',
                        help='use if you want all images to be posted',
                        action='store_true')
    args = parser.parse_args()
    chat_id = args.chat_id

    if args.all:
        publish_all_photos('images', args.frequency, args.chat_id)
    else:
        publish_one_photo('images', args.photo, args.chat_id)
