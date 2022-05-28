from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

import json

# Opening JSON file
with open('talabalar.json') as json_file:
	data = json.load(json_file)

	# Print the type of data variable
	print("Type:", type(data))
#inline keybordni va knopkalarni chaqirdim
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, Filters, ConversationHandler, MessageHandler)
import json

def start(update, context):
    update.message.reply_html(
        "<b>Assalomu alaykum!</b>\n \n Ingliz tili II fakulteti talabalari botiga \n \n Ism-familiyani yuboring: ")
    name_checker(update, context)


def name_checker(update, context):
  text = update.message.text
  for i in data:
    if text.lower() in i["Toliq ismi"].lower():
      update.message.reply_html(f"👤 <b>To‘liq ismi:</> <i>  {i['Toliq ismi'].title()}</i> \n \n | 👥 <b>Guruh:</b> <i>{i['Guruh']}</i> \n | 📍 <b>Manzil: </b>  {i['Viloyat']} {i['Tuman']} \n | 🎂 <b>Tug‘ilgan sanasi:</b>  <i> {i['Tugilgan sana']}</i> \n | ℹ️ <b>Fuqaroligi: </b> {i['Fuqarolik']}, \n \n @faculty_cognitobot")


def checker():
  name = input("Ismni kiriting: ")
  son = 0
  for i in data:
    if name.lower() in i["Toliq ismi"].lower():
      print(f'\n {i["Toliq ismi"]} \n {i["Guruh"]} \n')

 
def main():
    updater = Updater("5566249534:AAFiMWFuADw5Xe50MOpv1DnTW97Hj-vNDLM", use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', name_checker))
    dispatcher.add_handler(MessageHandler(Filters.all, name_checker)) 

    updater.start_polling()
    updater.idle()


main()







# importing the module