def msg_rcv(account, sender, message, conversation, flags):
    "will be invoked when a messages is received"


def listen():
    "start listening to pidgin"
    import dbus, gobject
    from dbus.mainloop.glib import DBusGMainLoop
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    bus.add_signal_receiver(msg_rcv,
            dbus_interface="im.pidgin.purple.PurpleInterface",
            signal_name="ReceivedImMsg")
    loop = gobject.MainLoop()
    loop.run()

listen()
