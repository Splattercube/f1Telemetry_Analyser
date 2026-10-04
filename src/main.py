import fastf1
from myFunctions import (my_averageLaptime, my_averageRacePace, my_calculateDegredation
                         , myPlotDegredation, my_compoundAnalysis, my_compareStints, myCleanRaceLaps
                         , my_raceAnalysis, my_multiRegression)

from myFunctions import my_plotAnalysis
session = fastf1.get_session(2026, "Spa", "R")
stint = 2
session.load()

##hamilton = session.drivers[4]
driver_laps = session.laps.pick_drivers("PIA")
# print(session.laps.columns)


# print(
#     driver_laps[
#         ["Driver", "LapNumber", "LapTime", "Compound", "Stint"]
#     ]
# 
# print(driver_laps["Stint"].dtype)

# print(driver_laps["Driver"].iloc[0])
# avg = my_averageLaptime(driver_laps)
# print(f"Avg laptime: {avg.round('1ms')}")
# avgP = my_averageRacePace(driver_laps)
# print(f"Avg pace: {avgP.round('1ms')}")
# avgS1 = my_averageRacePace(driver_laps, stint)
# print(f"Avg pace 2nd stint: {avgS1.round('1ms')}")
# degredation = my_calculateDegredation(driver_laps, stint)
# print(f"Tyre deg is {degredation.slope:.3f}s per lap")

# myPlotDegredation(driver_laps, stint)

# avgPace, deg, compound = my_compoundAnalysis(driver_laps, stint)
# print(f"Compound: {compound}")
# print(f"Average Pace: {avgPace.round('1ms')}")
# print(f"Degredation per lap: {deg:.3f}s")



# cleanLaps= myCleanRaceLaps(driver_laps, 1)
# print(cleanLaps[
#     ["LapNumber", "Stint", "Compound", "TyreLife", "LapTime"]
# ])

# stintInfo = my_compareStints(driver_laps)
# print(stintInfo)

raceData = my_raceAnalysis(driver_laps)
# print(raceData)
my_plotAnalysis(raceData)

intercept, tEffect, raceEffect = my_multiRegression(raceData)






