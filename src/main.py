# import fastf1
# from myFunctions import (my_averageLaptime, my_averageRacePace, my_calculateDegredation
#                          , myPlotDegredation, my_compoundAnalysis, my_compareStints, myCleanRaceLaps
#                          , my_raceAnalysis, my_multiRegression, my_regressionAccuracy)

# from myFunctions import my_plotAnalysis
# session = fastf1.get_session(2026, "Spa", "R")
# stint = 2
# session.load(telemetry=False, weather=False, messages=False)

# ##hamilton = session.drivers[4]
# driver_laps = session.laps.pick_drivers("HAM")
# # print(session.laps.columns)




# raceData = my_raceAnalysis(driver_laps)
# # print(raceData)
# my_plotAnalysis(raceData)

# intercept, tEffect, raceEffect = my_multiRegression(raceData)

# error = my_regressionAccuracy(raceData, intercept, tEffect, raceEffect)
# print(error)

import fastf1

session = fastf1.get_session(2024, "Belgian Grand Prix", "R")

print("API path:", session.api_path)

session.load(telemetry=False, weather=False, messages=False)

print("Lap count:", len(session.laps))