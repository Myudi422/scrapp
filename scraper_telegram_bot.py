from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

def events(bot, update):
    page = requests.get ("https://kashanu.ac.ir/en", verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    events = soup.find_all(class_="title-events")
    event_str = ""
    for i in range(5):
        event_str += events[i].get_text()
        event_str += "\n"

    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=event_str)
    
def main():
    token : '1811863530:AAFFYY_EqvKapAYf93HiO2j3qD-pGKNHgLg'
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('events',events))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
