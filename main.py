import settings
import telebot, datetime, time, threading


bot = telebot.TeleBot(settings.TOKEN)



def th(target):
    threading_thread = threading.Thread(target=target)
    threading_thread.deamon = True
    threading_thread.start()


def u():
    
    while settings.tester != None:
        try:
            bot.send_message(settings.tester, str(datetime.datetime.now())[:16], disable_notification=True)
        
        except:
            print('auto')
        time.sleep(settings.minutes*60)


@bot.message_handler(commands=['run'])
def runCom(message):
    if message.chat.type != "private":
        settings.tester = message.chat.id
        try:
            bot.send_message(settings.tester, "started", disable_notification=True)
        except:
            print('run')
        th(u)
        
        
        
@bot.message_handler(commands=['stop'])
def runCom(message):
    if message.chat.type != "private":
        try:
            bot.send_message(settings.tester, "stopped", disable_notification=True)
        except:
            print('stop')
        settings.tester = None
        

        

bot.polling()
