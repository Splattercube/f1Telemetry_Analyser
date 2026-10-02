import fastf1
from scipy.stats import linregress

def my_averageLaptime(laps):
    return laps["LapTime"].mean()

def my_averageRacePace(laps, stint:int | None = None):
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

    return cleanLaps["LapTime"].mean()

def my_calculateDegredation(laps, stint:int | None = None):
    degredation = 0
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
    tyreAge = cleanLaps["TyreLife"]
    lapTime = cleanLaps["LapTime"].dt.total_seconds()
    degredation = linregress(tyreAge, lapTime)

    return degredation
