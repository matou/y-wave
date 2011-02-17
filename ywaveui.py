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

import sys, participant, logging

logging.basicConfig(level=logging.DEBUG)

def display(message):
    print(message)

def cmd(cmd):
    logging.debug("I think this is a command: %s" % cmd)
    cmd = cmd.strip()
    if cmd == ":exit" or cmd == ":quit" or cmd == ":q":
        print("exiting")
        sys.exit(0)

    if cmd.startswith(":add"):
        # add a participant
        # the command must look as follows:
        # :add <participant> <my account>
        name = cmd.split(" ")[1]
        account = cmd.split(" ")[2]
        wave.add_participant(participant.Participant(name, account))
        logging.debug("added %s to account %s" % (name, account))
        return 

    print "command not recognized"

import wave
wave.init(display)

import dbusconnection
dbusconnection.init()
dbusconnection.start_listening()

logging.debug("starting main loop")
while(True):
    logging.debug("main loop started")
    mymessage = sys.stdin.readline()
    logging.debug("read message: %s" % mymessage)
    if mymessage.startswith(":"):
        cmd(mymessage)
    else: 
        logging.debug("waving %s" % mymessage)
        wave.wave(mymessage)
        display(mymessage)

