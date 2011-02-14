import dbus, account

bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService",
"/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

def send_msg(acc, receiver, message):
    "send a message to a buddy"

    # create new conversation:
    conv = purple.PurpleConversationNew(
            1, 
            account.get_account_id(acc), 
            receiver)

    # send message:
    purple.PurpleConvImSend(purple.PurpleConvIm(conv), message)

