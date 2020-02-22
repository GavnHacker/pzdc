import logging
import telebot


bot = telebot.TeleBot('927107270:AAEScmeElbidZLWqr9nv5Kh9xyBIouPjFiY')

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

@bot.message_handler(commands=['start'])
def star_message(message):
	bot.send_message(message.chat.id, 'Напиши день недели')

@bot.message_handler(content_types=['text'])
def send_text(message):
	if message.text == 'пн':
		bot.send_message(message.chat.id, '1 НЕДЕЛЯ\n1. Вышка, Пр, 304 ГАК, 08:30-10:05\n2. Осн. безопасного програмирования, Лк, 302 ВК, 10:25-12:00\n3. Философия, Лк, 507 У1, 12:35-14:10')
		bot.send_message(message.chat.id, '2 НЕДЕЛЯ\n1. Философия, Пр, Каф. Филос-и, 08:30-10:05\n2. Осн. безопасного програмирования, Лк, 302 ВК, 10:25-12:00\n3. Философия, Лк, 507 У1, 12:35-14:10')
	elif message.text == 'вт':
		bot.send_message(message.chat.id, '1. Вышка, Пр, 304 ГАК, 10:25-12:00\n2.-3. Алгоритм защиты данных, Лк-Пр, 21 ВК, 12:35-16:05')
	elif message.text == 'ср':
		bot.send_message(message.chat.id, '1. Инглиш, Пр, 510/511 У1, 08:30-10:05\n2. Вышка, Лк, 301 ГАК, 10:25-12:00')
	elif message.text == 'чт':
		bot.send_message(message.chat.id, '1 НЕДЕЛЯ\n1. Дискретная математика, Лк, 302 ЕК, 10:25-12:00\n2. Осн. безопасного програмирования, Пр, 22 ВК, 12:35-14:10')
		bot.send_message(message.chat.id, '2 НЕДЕЛЯ\n1. Осн. безопасного програмирования, Лб, 308 ВК, 10:25-12:00\n2. Дискретная математика, Пр, Каф. ОТП, 12:35-14:10')
	elif message.text == 'пт':
		bot.send_message(message.chat.id, '1 НЕДЕЛЯ\n1. Осн. безопасного програмирования, Лб, 20 ВК, 10:25-12:00\n2. Архитектура ОС, Лк, 104 ЕК, 12:35-14:10\n3. Укр. язык, Пр, Каф. УРМПЛ, 14:30-16:05')
		bot.send_message(message.chat.id, '2 НЕДЕЛЯ\n1. Архитектура ОС, Пр, 20 ВК, 10:25-12:00\n2. Архитектура ОС, Лк, 104 ЕК, 12:35-14:10\n3. Укр. язык, Пр, Каф. УРМПЛ, 14:30-16:05')
	elif message.text == 'сб':
		bot.send_message(message.chat.id, 'Нахрена тебе расписание в выходной?')
	elif message.text == 'вс':
		bot.send_message(message.chat.id, 'Нахрена тебе расписание в выходной?')
	else:
		bot.send_message(message.chat.id, 'Нэ понэл')


bot.polling(none_stop=True, interval=0)