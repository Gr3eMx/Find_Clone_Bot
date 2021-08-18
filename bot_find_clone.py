import telebot
import os
import find_clone
#API сайта и его ссылка
APPID = "c64006911caba9ee0382b859b7488c98"

#токен бота
bot = telebot.TeleBot('1861311136:AAHvqm4QXhMUzV7VnhKCIZps0oQz3vJYWIM')


#получение и отправка сообщения в боте

@bot.message_handler(content_types=["photo"])
def handle_docs_document(message):
    try:
        if not os.path.exists("screenshots"):
            os.mkdir("screenshots")
        save_dir = os.path.abspath("screenshots")
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = f'{message.photo[1].file_id}.jpg'
        with open(save_dir+ '/' +src, 'wb') as new_file:
            new_file.write(downloaded_file)
        file = f'screenshots/{src}'
        bot.reply_to(message, "Ищем ваших клонов")
        find_clone.authorizate()
        get = find_clone.upload_foto(file)
        for i in range(len(get)):
            bot.send_message(message.from_user.id, get[i])
    except:
        bot.send_message(message.from_user.id, "Отправьте фотографию, где только одно лицо")




bot.polling(none_stop=True, interval=0)