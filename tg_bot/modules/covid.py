from telegram import ParseMode, Update, Bot, Chat
from telegram.ext import CommandHandler, MessageHandler, BaseFilter, run_async

from tg_bot import dispatcher

from covid19_data import JHU



@run_async
def covid(bot: Bot, update: Update):
    message = update.effective_message
    device = message.text[len('/covid '):]
    total_confirmed_global = JHU.Total.confirmed
    total_deaths_global = JHU.Total.deaths
    total_recovered_global = JHU.Total.recovered
    active_cases_covid19 = total_confirmed_global - total_deaths_global - total_recovered_global
    reply_text = ("*🦠 COVID-19 Stats 🦠:*\n\n"
    "➥ *Total Confirmed* \nㅤㅤ╚» `" + str(total_confirmed_global) + "`\n"
    "➥ *Total Deaths* \nㅤㅤ╚» `" + str(total_deaths_global) + "`\n"
    "➥ *Total Recovered* \nㅤㅤ╚» `" + str(total_recovered_global) +"`\n"
    "➥ *Active Cases* \nㅤㅤ╚» `"+ str(active_cases_covid19) + "`\n\n"
    "➥ *Tips*\n☞ 😷 Wear A Mask.\n☞ 🧻 Use Tissue When Sneezing Or Blowing Nose.\n☞ 🧼 Wash Your Hands Frequently.\n☞︎︎︎ 👬 Avoid Contact With Others.\n☞︎︎︎ 🍎 Wash Foods After buying it.")
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)


__help__ = """
 
 - /covid get worldwide corona status
"""

__mod_name__ = 'Covid-19'

COVID_HANDLER = CommandHandler("covid", covid, admin_ok=True)
dispatcher.add_handler(COVID_HANDLER)


