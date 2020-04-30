def read_file(file_name):
    settings = {}
    try:
        with open(file_name, "r") as settings_file:
            lines = settings_file.readlines()
    except FileNotFoundError:
        return settings

    for line in lines:
        setting_name, value = line.split(" ", 1)
        settings[setting_name] = value

    return settings


class Settings:

    def __init__(self, file_name="settings.txt"):
        self.file_name = file_name
        self.settings = read_file(file_name)

    def read_settings(self, setting_names):

        for setting_name in setting_names:
            if setting_name not in self.settings.keys():
                setting_value = input("Please provide a value for " + setting_name + ": ")
                self.settings[setting_name] = setting_value

        self.write_settings()

        return self.settings

    def write_settings(self):
        with open(self.file_name, "w+") as settings_file:
            for setting_name, setting_value in self.settings.items():
                settings_file.write("{} {}\n".format(setting_name, setting_value))