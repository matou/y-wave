# Copyright (c) 2011 Matthias Matousek <matou@taunusstein.net>
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

from UserList import UserList
import logging

class Wave(UserList):
    "A wave has information about buddies who are part of the wave and "\
    "methods to communicate with those buddies."

    def __init__(self):
        UserList.__init__(self)
        import dbusconnection
        logging.debug("wave initialized")

    def add_participant(self, participant):
        self.append(participant)

    def wave(self, message):
        for participant in self:
            dbusconnection.send_msg(
                    participant.account, 
                    participant.name, 
                    message)

    def is_participant(self, name):
        for participant in self:
            if participant.name == name:
                return True
        return False

def init(message_handler):
    wave.w = Wave()
    logging.debug("wave created")
    msg_handler = message_handler
    logging.debug("handler: %s" % str(msg_handler))

def msg_rcv(account, sender, message, conversation, flags):
    logging.debug("received message: %s" % message)
    sender = sender.split("/")[0]
    if wave.w.is_participant(sender):
        msg_handler("%s: %s" % (sender, message))

def wave(message):
    wave.w.wave(message)

def add_participant(participant):
    wave.w.add_participant(participant)

