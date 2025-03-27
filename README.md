# SPACE 
Этот проект предназначен для загрузки фотографий SpaceX и NASA и возможности публиковать их в Telegram-канале с помощью чат-бота.
## Как запустить 
Для начала нужно настроить переменные окружения:
- NASA_TOKEN - токен необходим для работы с фотографиями на сайте NASA, его можно получить [здесь](https://api.nasa.gov/)
- TG_TOKEN - токен для авторизации Telegram бота, его можно получить непосредвственно при создании бота
- TG_CHAT_ID - ID пользователя или Telegram канала, где буду публиковаться фотографии
Добавьте эти данные в файл .env

Прграмма разделена на несколько скриптов, каждый из которых запускается отдельно:
### SpaceX
```
  python3 fetch_spacex_images.py
```
Можно использовать с таким ID:
```
  python3 fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```
### NASA ADOP
```
python3 nasa_adop.py
```
### NASA EPIC
```
python3 nasa_epic.py
```
### TG
```
python3 tg_bot.py
```
У скрипта есть необязательный аргумент time, он определяет то, с какой переодичностью будут выкладываться фотографии ботом. Соответственно принимает он в себя число, обознаающее время паузы между фото в секундах. По умолчанию пауза равна 4 часа.

