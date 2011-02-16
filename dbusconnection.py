# Copyright (c) 2011 Matthias Matouesk <matou@taunusstein.net>
# 
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# 

import dbus, gobject, wave
from dbus.mainloop.glib import DBusGMainLoop
from threading import Thread

DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
loop = gobject.MainLoop()

obj = bus.get_object(
        "im.pidgin.purple.PurpleService",
        "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

bus.add_signal_receiver(
        wave.msg_rcv,
        dbus_interface="im.pidgin.purple.PurpleInterface",
        signal_name="ReceivedImMsg")

class Listener(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        loop = gobject.MainLoop()
        loop.run()

listener = Listener()
listener.start()

def get_account_id(name):
    "returns the id of the specified account"
    for id in purple.PurpleAccountsGetAllActive():
        # i know this is ugly. but it's late and i want this to work.
        # PurpleAccountsFind(name, protocol) didn't work
        if name == str(purple.PurpleAccountGetUsername(id)).split("/")[0]:
            return id
    return -1

def send_msg(self, acc, receiver, message):
    conv = self.purple.PurpleConversationNew(
            1,
            get_account_id(acc),
            receiver)
    purple.PurpleConvImSend(purple.PurpleConvIm(conv), message)

