from douyu.chat.room import ChatRoom
def on_chat_message(msg):
    print('%s:%s' % (msg.attr('nn'), msg.attr('txt')))#输出弹幕消息

def run():
    room = ChatRoom('134000')
    room.on('chatmsg', on_chat_message)#chatmsg指的是弹幕消息 类型的信息
    #callback_list.append(on_chat_message)
    #callback_list=[<function on_chat_message at 0x0065E2B8>]
    #callbacks={'chatmsg': [on_chat_message]}
    room.knock()

if __name__ == '__main__':
     run()