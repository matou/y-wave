from UserList import UserList
import transmitter

class Wave(UserList):
    "A wave has information about buddies who are part of the wave and "\
    "methods to communicate with those buddies."

    def add_participant(self, participant):
        self.append(participant)

    def wave(self, message):
        for participant in self:
            transmitter.send_msg(
                    participant.account, 
                    participant.name, 
                    message)

# the list of all waves
waves = []
