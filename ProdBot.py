import Bot
import os

# RUN
if __name__ == "__main__":
    Bot.server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
