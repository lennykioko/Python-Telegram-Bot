from bot import TelegramBot

my_bot = TelegramBot()

msg = """
*JUST CREATED A TELEGRAM BOT*

*AUTHOR:* LENNY
*LANGUAGE:* PYTHON
*MESSAGE:* I AM AWESOME

"""

my_bot.send_message(msg=msg, chat_id=681966513)
