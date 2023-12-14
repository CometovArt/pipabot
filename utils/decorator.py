from telegram.ext import filters, MessageHandler, CommandHandler
from config import application



def on_message(filters=filters.ALL, group=0):
    def decorator(func):
        handler = MessageHandler(filters, func)
        application.add_handler(handler, group)
        return func
    return decorator


def on_command(command, filters=None, group=0):
    def decorator(func):
        handler = CommandHandler(command, func, filters)
        application.add_handler(handler, group)
        return func
    return decorator