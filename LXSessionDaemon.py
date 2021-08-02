import dbus

session_bus = dbus.SessionBus()
session_manager_raw = session_bus.get_object("org.lxde.SessionManager", "/org/lxde/SessionManager")
session_manager = dbus.Interface(session_manager_raw, dbus_interface = "org.lxde.SessionManager")

def print_keys(groupname: str):
    for key1 in getattr(session_manager, groupname + "Support")():
        for key2 in getattr(session_manager, groupname + "SupportDetail")(key1):
            if key2 != "":
                print("[" + groupname + "] " + key1 + "/" + key2)
            else:
                print("[" + groupname + "] " + key1)

def print_keys_and_values(groupname: str):
    for key1 in getattr(session_manager, groupname + "Support")():
        for key2 in getattr(session_manager, groupname + "SupportDetail")(key1):
            value = getattr(session_manager, groupname + "Get")(key1, key2)
            if key2 != "":
                print("[" + groupname + "] " + key1 + "/" + key2 + " = " + value)
            else:
                print("[" + groupname + "] " + key1 + " = " + value)

groups = [
    "Session",
    "Dbus",
    "Environment",
    "Keymap",
    # "Proxy",
    # "Security",
    "State",
    # "Updates",
    # "XRandr",
    "Xsettings",
    # "a11y",
]

for groupname in groups:
    print_keys_and_values(groupname)