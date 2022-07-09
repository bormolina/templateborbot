import private
import commands
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)


def main():
    token = private.token
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start', commands.cmd_start))
    dp.add_handler(CommandHandler('help', commands.cmd_help))
    dp.add_handler(CommandHandler('rolld6', commands.cmd_roll_d6))
    dp.add_handler(CommandHandler('animatedd6', commands.cmd_animated_d6))
    dp.add_handler(CommandHandler('flag', commands.cmd_get_flag))
    dp.add_handler(CommandHandler('rolldice', commands.cmd_roll_dice))
    dp.add_handler(CommandHandler('alert', commands.cmd_alert))
    dp.add_handler(MessageHandler(Filters.text, commands.message_handler))

    # Iniciamos el bot
    updater.start_polling()
    # Lo dejamos a la escucha
    updater.idle()


if __name__ == '__main__':
    print(f'El bot está listo para servir ...')
    main()
