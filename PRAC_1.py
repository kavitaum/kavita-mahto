
Code:1
import telepot
token = '1318772592:AAHXqIvSKWb13mLbLQJUfiLzpHoTpbWs3B8'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())


Code:2
import telepot
token = '1320252244:AAHx6ssGPVmaLZaTgQo7bYNPmLSQg0bZbcQ'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))

TelegramBot.message_loop(handle)


1.https://api.telegram.org/bot1320252244:AAHx6ssGPVmaLZaTgQo7bYNPmLSQg0bZbcQ/sendMessage?chat_id=1336458104&text=TestReply 
2.Getme: https://api.telegram.org/bot1320252244:AAHx6ssGPVmaLZaTgQo7bYNPmLSQg0bZbcQ/getMe
3.getupdates
https://api.telegram.org/bot1320252244:AAHx6ssGPVmaLZaTgQo7bYNPmLSQg0bZbcQ/getUpdates
