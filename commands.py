import fn
import numexpr
from telegram import (ParseMode, ReplyKeyboardMarkup)
import threading


def cmd_alert(update, context):
    def send_alert(msg):
        update.message.reply_text(msg)
    segundos = float(context.args[0])
    msg = ' '.join(context.args[1:])
    timer = threading.Timer(segundos, send_alert, [msg])
    timer.start()


def cmd_roll_dice(update, context):
    teclado = [
        ["d4", "d6"],
        ["d8", "d10", "d12"],
        ["d20", "d50", "d100"],
    ]

    teclado_telegram = ReplyKeyboardMarkup(
        teclado,
        one_time_keyboard=True,
        resize_keyboard=True
    )

    update.message.reply_text("Elige un dado", reply_markup=teclado_telegram)


def message_handler(update, context):
    msg = update.message.text

    if msg[0] == '=':
        cuenta = msg[1:]
        resultado = str(numexpr.evaluate(cuenta))
        update.message.reply_text(resultado)
    elif msg in ["d4", "d6", "d8", "d10", "d12", "d20", "d50", "d100"]:
        n = msg[1:]
        tirada = fn.roll_dice(int(n))
        update.message.reply_text(str(tirada))
    elif msg.find('chiste') != -1:
        chiste = fn.cuenta_chiste()
        update.message.reply_text(chiste)
    else:
        update.message.reply_text(msg)


def cmd_start(update, context):
    msg = """
Bienvenido a templateBor, un bot programado para aprender a programar bots :)
        """
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg)


def cmd_help(update, context):
    msg = """
Los comandos de templatebor son:
    <b>rolld6</b> --> lanza un dado
    <b>animatedd6</b> --> lanza un dado mediante una animación
    <b>flag X</b> --> mostrar la bandera del país X
    <b>rolldice X</b> --> lanza un dado de X caras
    <b>alert t X</b> --> lanza una alerta con el mensaje X tras t segundos
    """
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id, msg, parse_mode='HTML')


def cmd_roll_d6(update, context):
    result = fn.roll_d6()
    context.bot.send_message(update.message.chat_id, str(result))


def cmd_animated_d6(update, context):
    result = fn.roll_d6()
    animation = fn.get_d6_img(result)
    chat_id = update.message.chat_id
    context.bot.send_animation(chat_id, animation)


def cmd_get_flag(update, context):
    url = fn.get_url_flag(context.args[0])
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id, url)
