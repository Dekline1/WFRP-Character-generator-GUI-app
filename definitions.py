def help_me():
    help_text = "\n"
    for userCommand in commandDictionary:
        help_text += commandDictionary[userCommand][1] + "\n"
    return help_text


def clear():
    return "clear"


def exit_app():
    return "exit"


def back_log():
    return "[sample text] This is back log output"



def send_report():
    return "[sample text] This is the send report function"


def save_data():
    return "[sample text] This is the save data function"


def load_data():
    return "[sample text] This is the load data function"


def update_data():
    return "[sample text] This is the update data function"


def delete_data():
    return "[sample text] This is the delete data function"


def backup_data():
    return "[sample text] This is the backup data function"


# command list, use # if not in use

commandDictionary = {
    "h": [help_me, "[h]elp - display list of usable commands"],
    "c": [clear, "[c]lear - clean output data box"],
    "e": [exit_app, "[e]xit the application"],

    # sample functions:

    "1": [send_report, "[1] - [sample text] Send Report"],
    "2": [save_data, "[2] - [sample text] Save Data"],
    "3": [load_data, "[3] - [sample text] Load Data"],
    "4": [update_data, "[4] - [sample text] Update Data"],
    "5": [delete_data, "[5] - [sample text] Delete Data"],
    "6": [backup_data, "[6] - [sample text] Backup Data"]
}
