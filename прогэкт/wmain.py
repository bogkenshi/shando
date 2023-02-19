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
def process_num1_step(message, us_res = None):
    try:
        global us_n1
        
        #якщо це перший запуск
        if us_res == None:
            us_n1 = int(message.text)
        #якщо передається результат(далі буде def який дозволяє провести ще одну операцію)
        else:
            us_n1 = str(us_res)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        ibtn1 = types.KeyboardButton('+')
        ibtn2 = types.KeyboardButton('-')
        ibtn3 = types.KeyboardButton('*')
        ibtn4 = types.KeyboardButton('/')
        markup.add(ibtn1, ibtn2, ibtn3, ibtn4)

        msg = bot.send_message(message.chat.id, 'Тоож що в нас тут..', reply_markup=markup)
        bot.register_next_step_handler(msg, process_proc_step)
    except Exception as e:
        bot.reply_to(message, 'Упс, здається це не число!')

#вибір операції
def process_proc_step(message):
    try:
        global us_proc

        user_proc = message.text

        markup = types.ReplyKeyboardRemove(Selective=False)

        msg = bot.send_message(message.chat.id, 'Наступне число...', reply_markup=markup)
        bot.register_next_step_handler(msg, process_num2_step)
    except Exception as e:
        bot.reply_to(message, e)

#друге число
def process_num2_step(message):
    try:
        global us_n2
        us_n2 = int(message.text)

        markup = types.ReplykeyboardMarkup(resize_keyboard=True, row_width=2)
        ibtn1 = types.KeyboardButton('Результат')
        ibtn2 = types.KeyboardButton('Продовжити вираховування')
        markup.add(ibtn1, ibtn2)

        msg = bot.send_message(message.chat.id, 'Що далі?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_alternative_step)
    except Exception as e:
        bot.reply_to(message, 'Упс, здається це не число!')

#вибір між результатом та продовженням вираховуваннь
def process_alternative_step(message):
    try:
        calc()

        markup = types.ReplyKeyboardRemove(selective=False)
        #автоматично видає результат
        if message.text.lower() == 'результат':
          bot.send_message(message.chat.id, calcResultPrint(), reply_markup=markup)
        #рахує, виставляє данне число як process_num1_step та переводить нас назад до process_proc_step
        elif message.text.lower() == 'продовжити вираховування':
            process_num1_step(message, us_res)
    except Exception as e:
        bot.reply_to(message, 'Упс, здається щось не так...')
#зовнішній рахунок
def calcResultPrint():
    global us_n1, us_n2, us_proc, us_res
    return 'Отже, результат:' + str(us_n1) + ' '+ us_proc + ' ' + str(us_n2) + ' = ' + str(us_res)
#внутрішній рахунок
def calc():
    global us_n1, us_n2, us_proc, us_res

    us_res = eval(str(us_n1) + us_proc + str(us_n2))

    return us_res


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == '__main__':
    bot.polling(none_stop=True)