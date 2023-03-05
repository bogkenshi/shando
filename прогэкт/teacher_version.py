import wconfig
import telebot
from telebot import types 


bot = telebot.TeleBot(wconfig.token)

us_n1 = ''
us_n2 = ''
us_proc = ''
us_res = None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    #прибирання клавіатури
    markup = types.ReplyKeyboardRemove(selective=False)

    msg = bot.send_message(message.chat.id, 'Йоу, ' + message.from_user.first_name + ', я, типу, бот-калькулятор, радий буду допомогти! \nМаєш що на думці?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_num1_step)

#перше/подальші числа
@bot.message_handler()
def process_num1_step(message):
    # answer = f"{message.text} = {eval(message.text)}"
    if message.text == 'Привіт':
        bot.reply_to(message, "Привіт, як справи?")
    elif message.text == 'Все добре':
        bot.reply_to(message, "Вослухай цю музику: https://www.youtube.com/watch?v=EH1I-8KyI9Y")

if __name__ == '__main__':
    bot.polling(none_stop=True)