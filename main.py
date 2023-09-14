import telebot

bot_token = '6572020764:AAFLbXAGt58mZXRgj0ObItC0xsKUH4qNmA8' #токен от бота
chat_id = '5237273350'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'Start']) # Ждём команды Start / start
def send_message(command): # Если команду выполнили
    bot.send_message(chat_id, "PROMOCOD" +
                     "\n\nЧтобы узнать команды введи команду /commands" +
                     "\nCoded by 3xpl01t | @darkside_team") # Посылаем сообщение

@bot.message_handler(commands=['help', 'commands', 'Help', 'Commands']) # КОМАНДЫ
def send_message(command):
    bot.send_message(chat_id, "Команды: \n /NAME - Показать имя админа \n /PERSONAL - Личный кабинет  \n /PRODUCTS - Товары")


@bot.message_handler(commands=['personal','PERSONAL']) # Ждём команды
def send_personal(command):
    bot.send_message(chat_id,'Баланс - 0руб \n Промокодов - 0 \n Статус - Обычный пользователь')

@bot.message_handler(commands=['products', 'PRODUCTS']) # Ждём команды Start / start
def send_message(command): # Если команду выполнили
    bot.send_message(chat_id, "PRODUCTS:" +
                     "\n\nЧтобы узнать промокоды СберМаркет,введите команду /CBERMARKET" +
                     "\n\nЧтобы узнать промокоды ЯНДЕКС ЕДА,введите команду /YANDEX_EDA")

@bot.message_handler(commands=['cbermarket','CBERMARKET']) # КОМАНДЫ
def send_message(command):
    bot.send_message(chat_id, "🛒Сбер Маркет: \n ody59fne - Скидка 650₽ на первый заказ от 1500₽ \n ez9td93w — Скидка 30% на первый заказ от 2000₽ \n zwp2bhca — Скидка 150₽ на первый заказ от 400₽ ")

@bot.message_handler(commands=['yandex_eda','YANDEX_EDA']) # КОМАНДЫ
def send_message(command):
    bot.send_message(chat_id, "🍽️Рестораны: \n ➡️ qkrqaj25 - Скидка 20% при заказе от 900 руб \n ➡️ qfgz58w8 - Скидка 300 руб при заказе от 900 рублей 🛒Магазины: \n ➡️ kcgl09tm - Скидка 37% на товары для школы в Комус \n ➡️ kbxd2ei9 - Скидка 35% на заказ от 900 руб \n ➡️ nha0scnf - Скидка 500 руб. при заказе от 1500")

bot.polling()




























































