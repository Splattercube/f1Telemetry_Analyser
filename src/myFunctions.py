import fastf1
from scipy.stats import linregress
import matplotlib.pyplot as plt
def my_averageLaptime(laps):
    return laps["LapTime"].mean()



def my_averageRacePace(laps, stint:int | None = None):
    cleanLaps = myCleanRaceLaps(laps, stint)

    return cleanLaps["LapTime"].mean()

def my_calculateDegredation(laps, stint:int | None = None):
    degredation = 0
    cleanLaps = myCleanRaceLaps(laps, stint)
    tyreAge = cleanLaps["TyreLife"]
    lapTime = cleanLaps["LapTime"].dt.total_seconds()


    degredation = linregress(tyreAge, lapTime)

    return degredation


def myPlotDegredation(laps, stint:int | None = None):
    degredation = 0
    cleanLaps = myCleanRaceLaps(laps, stint)
    # print(cleanLaps[["LapNumber", "Stint", "TyreLife", "LapTime"]])
    # print("Number of laps:", len(cleanLaps))
    
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


def my_compoundAnalysis(laps, stint: int | None = None, compound:str | None = None):
    cleanLaps = myCleanRaceLaps(laps,stint)
    compoundUsed = cleanLaps["Compound"].iloc[0]

    if stint is not None:
        cleanLaps = cleanLaps[cleanLaps["Stint"] == stint]

    if compound is not None:
        cleanLaps = cleanLaps[cleanLaps["Compound"] == compound]
    
    
    pace = my_averageRacePace(cleanLaps)
    deg = my_calculateDegredation(cleanLaps)
    return pace, deg.slope, compoundUsed

    