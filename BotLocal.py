import Bot

# RUN
if __name__ == "__main__":
    Bot.bot.remove_webhook()
    Bot.bot.polling(none_stop=True)
