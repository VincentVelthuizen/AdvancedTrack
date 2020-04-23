class SMS_store:
    """ Stores SMS messages and keeps track which are viewed and which aren't. """

    def __init__(self):
        self.messages = list()

    def __str__(self):
        text = ""
        for number, (_, from_number, time_arrived, text_of_SMS) in enumerate(self.messages):
            text += "{0}: {1} ({2})\n{3}\n".format(number, from_number, time_arrived, text_of_SMS)
        return text

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.messages.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.messages)
