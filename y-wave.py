#!/usr/bin/python2

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

from threading import Thread
import dbus, gobject
from dbus.mainloop.glib import DBusGMainLoop

def msg_rcv(account, sender, message, conversation, flags):
    print sender, "said:", message

class Listener(Thread):
    def __init__(self):
        Thread.__init__(self)
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()

        bus.add_signal_receiver(
                msg_rcv, 
                dbus_interface="im.pidgin.purple.PurpleInterface", 
                signal_name="ReceivedImMsg")

        self.loop = gobject.MainLoop()

    def run(self):
        self.loop.run()

l = Listener()

# this is the main program

# first, we need a wave
import wave
wave = wave.Wave()

# finally start listening
l.start()
