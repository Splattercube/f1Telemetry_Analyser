import fastf1
from myFunctions import my_averageLaptime, my_averageRacePace, my_calculateDegredation 


session = fastf1.get_session(2026, "Monza", "R")
session.load()

##hamilton = session.drivers[4]
driver_laps = session.laps.pick_drivers("HAM")
# print(session.laps.columns)


# print(
#     driver_laps[
#         ["Driver", "LapNumber", "LapTime", "Compound", "Stint"]
#     ]
# )
# print(driver_laps["Stint"].dtype)

print(driver_laps["Driver"].iloc[0])
avg = my_averageLaptime(driver_laps)
print("Avg laptime: ", avg)
avgP = my_averageRacePace(driver_laps)
print("Avg pace: ", avgP)
avgS1 = my_averageRacePace(driver_laps, 2)
print("Avg pace 2nd stint: ", avgS1)
degredation = my_calculateDegredation(driver_laps)
print(f"Tyre deg is {degredation.slope:.3f}s per lap")





