import BotConfig
import Bot
import os

from flask import Flask, request

server = Flask(__name__)

@server.route("/")
def webhook():
    Bot.bot.remove_webhook()
    Bot.bot.set_webhook(url=BotConfig.HOST + BotConfig.TOKEN)
    return "Нихуя се", 200


@server.route('/' + BotConfig.TOKEN, methods=['POST'])
def updater():
    response = request.stream.read().decode("utf-8")
    Bot.bot.process_new_updates([Bot.telebot.types.Update.de_json(response)])
    return "!", 200


# RUN
if __name__ == "__main__":
    Bot.server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
