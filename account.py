import dbus

bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService",
"/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

def get_account_id(name):
    "returns the id of the specified account"
    for id in purple.PurpleAccountsGetAllActive():
        # i know this is ugly. but it's late and i want this to work.
        if name == str(purple.PurpleAccountGetNameForDisplay(id)).split("/")[0]:
            return id
    return -1
