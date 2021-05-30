import telebot
import ConfigBot
import os

from telebot import types
from flask import Flask, request

bot = telebot.TeleBot(ConfigBot.TOKEN)
server = Flask(__name__)


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=ConfigBot.HOST + ConfigBot.TOKEN)
    return "Нихуя се", 200


@server.route('/' + ConfigBot.TOKEN, methods=['POST'])
def updater():
    response = request.stream.read().decode("utf-8")
    bot.process_new_updates([telebot.types.Update.de_json(response)])
    return "!", 200


def keyboard(where_call):
    if where_call == 'Categories':
        markup = types.InlineKeyboardMarkup(row_width=1)
        BalanceButton = types.InlineKeyboardButton("Qiwi с балансом", callback_data='Balance')
        CloseButton = types.InlineKeyboardButton("Закрыть", callback_data='Close')
        markup.add(BalanceButton, CloseButton)

        return markup
    elif where_call == 'Profile':
        markup = types.InlineKeyboardMarkup(row_width=1)
        History = types.InlineKeyboardButton("История заказов", callback_data='History')

        markup.add(History)

        return markup
    elif where_call == 'Accounts':
        markup = types.InlineKeyboardMarkup(row_width=1)
        MinimumAccount = types.InlineKeyboardButton("Минимальный аккаунт | 300 ₽ | Кол-во: 44 шт.",callback_data='MinimumAccount')
        AverageAccount = types.InlineKeyboardButton("Средний аккаунт | 1000 ₽ | Кол-во: 21 шт.", callback_data='AverageAccount')
        ProfessionalAccount = types.InlineKeyboardButton("Профессиональный аккаунт | 2400 ₽ | Кол-во: 14 шт.",callback_data='ProfessionalAccount')
        Back1 = types.InlineKeyboardButton("Назад", callback_data='Back1')

        markup.add(MinimumAccount, AverageAccount, ProfessionalAccount, Back1)

        return markup
    elif where_call == 'MiniAccount':
        markup = types.InlineKeyboardMarkup(row_width=5)

        Value1 = types.InlineKeyboardButton("1", callback_data='One1')
        Value2 = types.InlineKeyboardButton("2", callback_data='Two1')
        Value3 = types.InlineKeyboardButton("3", callback_data='Three1')
        Value4 = types.InlineKeyboardButton("4", callback_data='Four1')
        Value5 = types.InlineKeyboardButton("5", callback_data='Five1')
        Value6 = types.InlineKeyboardButton("6", callback_data='Six1')
        Value7 = types.InlineKeyboardButton("7", callback_data='Seven1')
        Value8 = types.InlineKeyboardButton("8", callback_data='Eight1')
        Value9 = types.InlineKeyboardButton("9", callback_data='Nine1')
        Value10 = types.InlineKeyboardButton("10", callback_data='Ten1')

        Back2 = types.InlineKeyboardButton("Назад", callback_data='Back2')
        BackCategories1 = types.InlineKeyboardButton("Назад ко всем категориям", callback_data='BackCategories1')

        markup.row(Value1, Value2, Value3, Value4, Value5)
        markup.row(Value6, Value7, Value8, Value9, Value10)
        markup.row(Back2)
        markup.row(BackCategories1)

        return markup
    elif where_call == 'MidlAccount':
        markup = types.InlineKeyboardMarkup(row_width=5)

        Value1 = types.InlineKeyboardButton("1", callback_data='One2')
        Value2 = types.InlineKeyboardButton("2", callback_data='Two2')
        Value3 = types.InlineKeyboardButton("3", callback_data='Three2')
        Value4 = types.InlineKeyboardButton("4", callback_data='Four2')
        Value5 = types.InlineKeyboardButton("5", callback_data='Five2')
        Value6 = types.InlineKeyboardButton("6", callback_data='Six2')
        Value7 = types.InlineKeyboardButton("7", callback_data='Seven2')
        Value8 = types.InlineKeyboardButton("8", callback_data='Eight2')
        Value9 = types.InlineKeyboardButton("9", callback_data='Nine2')
        Value10 = types.InlineKeyboardButton("10", callback_data='Ten2')

        Back2 = types.InlineKeyboardButton("Назад", callback_data='Back2')
        BackCategories1 = types.InlineKeyboardButton("Назад ко всем категориям", callback_data='BackCategories1')

        markup.row(Value1, Value2, Value3, Value4, Value5)
        markup.row(Value6, Value7, Value8, Value9, Value10)
        markup.row(Back2)
        markup.row(BackCategories1)

        return markup
    elif where_call == 'ProfAccount':
        markup = types.InlineKeyboardMarkup(row_width=5)

        Value1 = types.InlineKeyboardButton("1", callback_data='One3')
        Value2 = types.InlineKeyboardButton("2", callback_data='Two3')
        Value3 = types.InlineKeyboardButton("3", callback_data='Three3')
        Value4 = types.InlineKeyboardButton("4", callback_data='Four3')
        Value5 = types.InlineKeyboardButton("5", callback_data='Five3')
        Value6 = types.InlineKeyboardButton("6", callback_data='Six3')
        Value7 = types.InlineKeyboardButton("7", callback_data='Seven3')
        Value8 = types.InlineKeyboardButton("8", callback_data='Eight3')
        Value9 = types.InlineKeyboardButton("9", callback_data='Nine3')
        Value10 = types.InlineKeyboardButton("10", callback_data='Ten3')

        Back2 = types.InlineKeyboardButton("Назад", callback_data='Back2')
        BackCategories1 = types.InlineKeyboardButton("Назад ко всем категориям", callback_data='BackCategories1')

        markup.row(Value1, Value2, Value3, Value4, Value5)
        markup.row(Value6, Value7, Value8, Value9, Value10)
        markup.row(Back2)
        markup.row(BackCategories1)

        return markup
    elif where_call == 'Order':
        markup = types.InlineKeyboardMarkup(row_width=1)

        Payment = types.InlineKeyboardButton(text='Перейти к оплате', callback_data='Payment')
        PaymentVerification = types.InlineKeyboardButton(text='Проверить оплату', callback_data='PaymentVer')
        Cancellation = types.InlineKeyboardButton(text='⛔Отменить заказ', callback_data='Cancellation')

        markup.add(Payment, PaymentVerification, Cancellation)

        return markup


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Купить Qiwi аккаунт🥝', 'Наличие товара🧰')
    markup.row('Профиль🤴', 'О магазине🛠')
    markup.row('Помощь📫')

    bot.send_message(message.chat.id, "Меню обновлено", parse_mode='html')
    bot.send_message(message.chat.id, "Здравствуйте✌\n"
                                      "Для покупки Qiwi кошелька подпишитесь на канал"
                                      "\n\n"
                                      "https://t.me/joinchat/NmNWc8fjI8U4MDYy\n"
                                      "И воспользуйтесь меню👇", parse_mode='html',disable_web_page_preview=True ,reply_markup=markup)


@bot.message_handler(content_types=['text'])
def menu(message):
    if message.chat.type == 'private':
        if message.text == 'Купить Qiwi аккаунт🥝':
            bot.send_message(message.chat.id, "Активные категории в магазине:", parse_mode='html', reply_markup=keyboard('Categories'))
        elif message.text == 'Наличие товара🧰':
            bot.send_message(message.chat.id, '🥝Qiwi c балансом🥝\n'
                                              'Минимальный аккаунт | 300 ₽ | Кол-во: 44 шт.\n'
                                              'Средний аккаунт | 1000 ₽ | Кол-во: 21 шт.\n'
                                              'Профессиональный аккаунт | 2400 ₽ | Кол-во: 14 шт.')

        elif message.text == 'Профиль🤴':
            IDUser = message.from_user.id
            UserName = message.from_user.username
            bot.send_message(message.chat.id, '🔐 ID: {id}\n'
                                              '💰 Ваш баланс: 0\n'
                                              '👤 Пользователь: @{nameuser}\n'
                                              '💸 Количество покупок: 0'.format(id=IDUser, nameuser=UserName), parse_mode='html',reply_markup=keyboard('Profile'))
        elif message.text == 'О магазине🛠':
            text1 = '[Посмотреть](https://t.me/joinchat/NmNWc8fjI8U4MDYy)'
            bot.send_message(message.chat.id, '🏠 Магазин: 🥝WalletsQiwiPocket💳\n'
                                              '⏰ Дата создания: 2021-05-19\n'
                                              '📢 Канал:  {Text}'.format(Text=text1),disable_web_page_preview=True ,parse_mode='Markdown')
        elif message.text == 'Помощь📫':
            bot.send_message(message.chat.id,'Если у вас возникли вопросы обращайтесь: @QiwiSaportService\n'
                                             'Либо пишите нам на почту: sluzhba.podderzhkiqiwi18@list.ru\n\n'
                                             'Ответы на часто задаваемые вопросы⁉\n\n'
                                             '✔️Все кошельки не используется больше полу года, смс\n'
                                             'подтверждение отключено, вывод мгновенный.\n\n'
                                             '🔉Вопрос: Куда могу вывести деньги?\n'
                                             '🔊Ответ: На Qiwi кошелёк, банковскую карту, а так же оплатить \n'
                                             'почти любой товар из интернета.\n\n'
                                             '🔉Вопрос: Заходить в кошельки безопасно?\n'
                                             '🔊Ответ: Владельцы не проявляли активность более года. Мы\n'
                                             'рекомендуем делать перевод Qiwi ваучером.\n\n'
                                             '🔉Вопрос: Что я получу после покупки?\n'
                                             '🔊Ответ: Логин, пароль от кошелька, логин пароль от почты,\n'
                                             'привязанной к кошельку.\n\n'
                                             '🔉Вопрос: Почему так дёшево?\n'
                                             '🔊Ответ: Цена сформирована из-за невысокого доверия к\n'
                                             'товару. 25% от суммы кошелька самый оптимальный вариант.\n\n'
                                             '🔉Вопрос: Почему вы сами не обналичиваете кошельки?\n'
                                             '🔊Ответ: Заходить с одного ip и переводить на свой Qiwi со\n'
                                             'всех кошельков, что есть у нас опасно, так были\n'
                                             'заблокированы многие кошельки, поэтому мы приняли\n'
                                             'решение продавать аккаунты в одни руки.')
        else:
            bot.send_message(message.chat.id, "Ваш запрос не понятен, воспользуйтесь меню", parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def MenuBalance(call):
    try:
        if call.message:
            if call.data == 'Balance':
                Photo2 = open('photo_2021-05-28_13-52-15.jpg')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='{Pic}\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '🥝Вы выбрали: Qiwi c балансом\n\n'
                                           '💵В наличии у бота💵\n'
                                           '💳WalletsQiwiPocket💳\n\n'
                                           'Имеются кошельки:\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖'.format(Pic=Photo2), reply_markup=keyboard('Accounts'))
            elif call.data == 'MinimumAccount':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                           "Вы выбрали минимальный Qiwi кошелёк\n\n"
                                           " ✅ Qiwi кошелёк, цена: 300₽.\n"
                                           " 💰 Баланс кошелька: 800-1500₽.\n\n"
                                           "При покупки кошелька, вы получаете:\n"
                                           "🔑 Логин и пароль\n\n"
                                           " ☑ Смс код выключен!\n"
                                           "🔥 Статус кошелька: Основной\n\n"
                                           "Выберите количество товара, которое хотите купить:\n"
                                           "➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard('MiniAccount'))
            elif call.data == 'AverageAccount':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                           "Вы выбрали средний кошелёк\n\n"
                                           "✅Qiwi кошелёк, цена: 1000₽.\n"
                                           "💰 Баланс кошелька: 2200-4000₽.\n\n"
                                           "При покупки кошелька, вы получаете:\n"
                                           "🔑Логин и пароль\n\n"
                                           "☑ Смс код выключен!\n"
                                           "🔥Статус кошелька: Основной\n\n"
                                           "Выберите количество товара, которое хотите купить:\n"
                                           "➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard('MidlAccount'))
            elif call.data == 'ProfessionalAccount':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                           "Вы выбрали максимальный кошелёк\n\n"
                                           "✅Qiwi кошелёк, цена: 2400₽.\n"
                                           "💰 Баланс кошелька: 6200-12800₽.\n\n"
                                           "При покупки кошелька, вы получаете:\n"
                                           "🔑Логин и пароль\n\n"
                                           "☑ Смс код выключен!\n"
                                           "🔥Статус кошелька: Профессиональный\n\n"
                                           "Выберите количество товара, которое хотите купить:\n"
                                           "➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=keyboard('ProfAccount'))
            elif call.data == 'Back2':
                Picture = 'Фото'  # open('photo_2021-05-28_13-52-15.jpg')
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='{Pic}\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '🥝Вы выбрали: Qiwi c балансом\n\n'
                                           '💵В наличии у бота💵\n'
                                           '💳WalletsQiwiPocket💳\n\n'
                                           'Имеются кошельки:\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖'.format(Pic=Picture), reply_markup=keyboard('Accounts'))
            elif call.data == 'BackCategories1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Активные категории в магазине:",
                                      reply_markup=keyboard('Categories'))
            elif call.data == 'Back1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Активные категории в магазине:",
                                      reply_markup=keyboard('Categories'))
            elif call.data == 'Close':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Отменено",reply_markup=None)
            elif call.data == 'History':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Всего у Вас заказов: 0", reply_markup=None)
            elif call.data == 'One1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text= 'Вы выбрали минимальный Qiwi кошелёк\n\n'
                                            '✅ Qiwi кошелёк, цена: 300₽.\n'
                                            '💰 Баланс кошелька: 800-1500₽.\n\n'
                                            'При покупки кошелька, вы получаете:\n'
                                            '🔑 Логин и пароль\n\n'
                                            '☑ Смс код выключен!\n'
                                            '🔥 Статус кошелька: Основной\n\n'
                                            '📦 Кол-во: 1 шт.\n'
                                            '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                            '💡 Заказ #1345531\n'
                                            '🕐 Время заказа: Дата\n\n'
                                            '🕐 Итоговая сумма: 300 ₽\n'
                                            '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                            'Перейдите по кнопке для оплаты\n'
                                            '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                            '⏰ Время на оплату: 20 минут\n'
                                            '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Two1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 2 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1346501\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 600 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Three1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 3 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1344123\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 900 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Four1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 4 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1347583\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 1200 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Five1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 5 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1333312\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 1500 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Six1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 6 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1341340\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 1800 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Seven1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 7 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1347734\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 2100 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Eight1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 8 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1349133\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 2400 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Nine1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 9 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1340015\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 2700 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Ten1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали минимальный Qiwi кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 300₽.\n'
                                           '💰 Баланс кошелька: 800-1500₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 10 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1334451\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 3000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'One2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 1 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1330007\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 1000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Two2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 2 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1344432\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 2000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Three2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 3 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1350031\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 3000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Four2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 4 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1337702\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 4000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Five2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 5 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1332209\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 5000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Six2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 6 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1347603\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 6000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Seven2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 7 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1349001\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 7000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Eight2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 8 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1340012\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 8000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Nine2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 9 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1312210\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 9000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Ten2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали средний кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 1000₽.\n'
                                           '💰 Баланс кошелька: 2200-4000₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Основной\n\n'
                                           '📦 Кол-во: 10 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1334410\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 10000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'One3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 1 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1344901\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 2400 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Two3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 2 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1347123\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 4800 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Three3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 7200₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 3 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1343321\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 7200 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Four3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 4 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1344566\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 96000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Five3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 5 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1347711\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 12000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Six3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 6 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1341321\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 14400 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Seven3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 7 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1348891\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 16800 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Eight3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 8 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1342431\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 19200 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Nine3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 9 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1343947\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 21600 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'Ten3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Вы выбрали максимальный кошелёк\n\n'
                                           '✅ Qiwi кошелёк, цена: 2400₽.\n'
                                           '💰 Баланс кошелька: 6200-12800₽.\n\n'
                                           'При покупки кошелька, вы получаете:\n'
                                           '🔑 Логин и пароль\n\n'
                                           '☑ Смс код выключен!\n'
                                           '🔥 Статус кошелька: Профессиональный\n\n'
                                           '📦 Кол-во: 10 шт.\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '💡 Заказ #1344758\n'
                                           '🕐 Время заказа: Дата\n\n'
                                           '🕐 Итоговая сумма: 24000 ₽\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           'Перейдите по кнопке для оплаты\n'
                                           '➖➖➖➖➖➖➖➖➖➖➖➖\n'
                                           '⏰ Время на оплату: 20 минут\n'
                                           '🕜 Необходимо оплатить до Время', reply_markup=keyboard('Order'))
            elif call.data == 'PaymentVer':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Ожидание оплаты")
            elif call.data == 'Cancellation':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Заказ отменен", reply_markup=None)
    except Exception as e:
        print(repr(e))

# RUN
if __name__ == "__main__":
    if ConfigBot.RUN_MODE == 'LOCAL':
        bot.polling(none_stop=True)
    elif ConfigBot.RUN_MODE == 'PROD':
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    else:
        print('ОШИБКА ЗАПУСКА БОТА')