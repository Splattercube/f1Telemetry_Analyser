import fastf1
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd
#avg laptime as panda datatype
def my_averageLaptime(laps):
    return laps["LapTime"].mean()


#avg pacefor valid laps pandaDT
def my_averageRacePace(laps, stint:int | None = None):
    cleanLaps = myCleanRaceLaps(laps, stint)

    return cleanLaps["LapTime"].mean()

#returns lineregression
def my_calculateDegredation(laps, stint:int | None = None):
    degredation = 0
    cleanLaps = myCleanRaceLaps(laps, stint)
    if len(cleanLaps) < 2:
            return None
    tyreAge = cleanLaps["TyreLife"]
    lapTime = cleanLaps["LapTime"].dt.total_seconds()


    degredation = linregress(tyreAge, lapTime)

    return degredation

#void shows scatterplot line regression
def myPlotDegredation(laps, stint:int | None = None):
    degredation = 0
    cleanLaps = myCleanRaceLaps(laps, stint)
    # print(cleanLaps[["LapNumber", "Stint", "TyreLife", "LapTime"]])
    # print("Number of laps:", len(cleanLaps))
    if len(cleanLaps) < 2:
        return None
    tyreAge = cleanLaps["TyreLife"]
    lapTime = cleanLaps["LapTime"].dt.total_seconds()

  
    degredation = linregress(tyreAge, lapTime)
    predictedLap = degredation.intercept + degredation.slope * tyreAge
    
    
    plt.scatter(tyreAge, lapTime, label="Actual Laps")
    plt.plot(tyreAge, predictedLap, label="Regression")
    plt.xlabel("Tyre age (Laps)")
    plt.ylabel("Lap Time (s)")
    plt.title("Tyre Degredation")
    plt.show()

#filter data returns valid raceLaps
def myCleanRaceLaps(laps, stint: int | None = None):
    cleanLaps = laps.dropna(subset=["LapTime"])#drop laps with no time associated
    cleanLaps = cleanLaps[
        cleanLaps["PitInTime"].isna() &
        cleanLaps["PitOutTime"].isna() 
    ]
    cleanLaps = cleanLaps[#keep accurate data
        cleanLaps["IsAccurate"] == True
    ]
        
    if stint is not None:#stint filter
        cleanLaps = cleanLaps[
            cleanLaps["Stint"] == stint
        ]
    return cleanLaps

#returns pace, degSlope, compoundUsed, numberof laps in stint
def my_compoundAnalysis(laps, stint: int | None = None, compound:str | None = None):
    cleanLaps = myCleanRaceLaps(laps,stint)
    compoundUsed = cleanLaps["Compound"].iloc[0]

    if stint is not None:
        cleanLaps = cleanLaps[cleanLaps["Stint"] == stint]

    if compound is not None:
        cleanLaps = cleanLaps[cleanLaps["Compound"] == compound]
    
    
    pace = my_averageRacePace(cleanLaps)
    deg = my_calculateDegredation(cleanLaps)
    numLaps = len(cleanLaps)

    if deg is None:
        degSlope = None
    else:
        degSlope = deg.slope
    
    return pace, degSlope, compoundUsed, numLaps

#returns DF of Stints
def my_compareStints(laps):
    stintRes = []
    stints = laps["Stint"].dropna().unique()
    for stint in stints:
        pace, deg, comp, numLaps = my_compoundAnalysis(laps, stint)
        stintRes.append((stint, pace, deg, comp, numLaps))
    stintDF = pd.DataFrame(
        stintRes,
        columns=["Stint", "AveragePace", "Degredation", "Compound", "NumberLaps"]
    )

    return stintDF

