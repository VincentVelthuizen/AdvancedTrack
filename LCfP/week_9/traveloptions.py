from LCfP.week_9.Settings import Settings

settings = Settings("travel_options.txt")
print(settings.read_settings(["walking_speed", "walking_extra_time", "biking_speed", "biking_extra_time",
                              "driving_speed", "driving_extra_time"], (["float"] * 6)))

# walking_speed = 5   # km/h
# biking_speed = 15   # km/h
# driving_speed = 50  # km/h
#
# walking_extra_time = 5      # minutes
# biking_extra_time = 10      # minutes
# driving_extra_time = 20     # minutes

travel_distance = int(input("How far will you travel today in km "))  # km

walking_time = (travel_distance / settings.get("walking_speed")) * 60 + settings.get("walking_extra_time")  # minutes
biking_time = (travel_distance / settings.get("biking_speed")) * 60 + settings.get("biking_extra_time")  # minutes
driving_time = (travel_distance / settings.get("driving_speed")) * 60 + settings.get("driving_extra_time")  # minutes

print("Walking", int(walking_time // 60), "hours and", int(walking_time % 60), "minutes")
print("Biking", int(biking_time // 60), "hours and", int(biking_time % 60), "minutes")
print("Driving", int(driving_time // 60), "hours and", int(driving_time % 60), "minutes")
