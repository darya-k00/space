import argparse
import random
from time import sleep
from dotenv import load_dotenv
import os
import telegram


def publish_all_photos(directory, chat_id):
     time_messages = 14400
     while True:
         images = os.listdir(directory)
         random.shuffle(images)
         
         for image in images:
            with open(f'{directory}/{image}', 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)
            time.sleep(time_messages)   
    

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
    parser.add_argument('-t', '--time',
                        help='type how often you want to publish in hours',
                        type=int, default=14400)
    args = parser.parse_args()
    chat_id = args.chat_id
    stop = args.time
    publish_all_photos('images',args.time, args.chat_id)
