from model import *
import json

#setattr(obj, name, val)


def load_config(fname):
    j = json.load(open(fname))
    pprint(j)

def write_to_file(data):
    with open("./generated_config.json", "w") as file:
        file.write(json.dumps(data, indent=4))

#load_config("./config.json")

data = {
    "InstructionFile": "Instructions.xml",
    "WallHeight": 3,
    "CharacterData": {
        "CamRotation": 10.0,
        "Height": 0.5,
        "MovementSpeed": 10.0,
        "RotationSpeed": 100.0,
        "TimeToRotate": 1,
        "OutputFile": "out.csv",
        "CharacterBound": 0.5,
        "DistancePickup": 2,
        "PickupRotationSpeed": 1,
        "CharacterStartPos": {"X": 0, "Y": 0}
    },

    "BlockOrder": [],

    "BlockList": [
        {
            "BlockName": "TEST1",
            "Notes": "TEST NOTE",

            "EndFunction": "CheckFoodThresholdPercentage",
            "EndGoal": "0 5",

            "TrialOrder": []
        }
    ],

    "TrialData": [
        {
            "FileLocation": "Test.jpg",
            "TimeAllotted": 1
        },
        {
            "FileLocation": "Test2.jpg",
            "TimeAllotted": -1
        },
        {
            "Index": 4,
            "EnvironmentType": 2,
            "Sides": 40,
            "Color": "00ff00",
            "PillarColor": "00ff00",
            "Radius": 10,
            "InitialAngle": 0,
            "PickupType": 1,
            "TimeAllotted": 10,
            "PickupVisible": 1,
            "RandomLoc": 0,
            "Pickups": [1]
        },
         {
            "TwoDimensional": 1,
            "EnvironmentType": 4,
            "TimeAllotted": 10
        },
        {
            "Index": 2,
            "EnvironmentType": 0,
            "Sides": 5,
            "Color": "ff0000",
            "PillarColor": "00ff00",
            "Radius": 10,
            "InitialAngle": 0,
            "PickupType": 2,
            "TimeAllotted": 10,
            "PickupVisible": 0,
            "RandomLoc": 0
        }

    ],
    "PickupItems": [
        {
            "Tag": "Food",
            "Color": "ff0000",
            "SoundLocation": "eat",
            "PythonFile": "Example.py",
            "Size": 1.0,
            "PrefabName": "Pickup",
            "Loc": [5, 5]
        },
        {
            "Tag": "Water",
            "Color": "0000ff",
            "SoundLocation": "drink",
            "PythonFile": "Example.py",
            "Size": 1.0,
            "PrefabName": "Pickup",
            "Loc": [5, -5]
        },
        {
            "Tag": "Money",
            "Color": "00ff00",
            "SoundLocation": "money",
            "PythonFile": "Example.py",
            "Size": 1.0,
            "PrefabName": "Pickup",
            "Loc": [-5, 5]

        }
    ],
    "Pillars": [
        {
            "X": 0.0,
            "Y": 10.0,
            "Radius": 1.0,
            "Height": 10.0
        },
        {
            "X": 0.0,
            "Y": -10.0,
            "Radius": 1.0,
            "Height": 10.0
        }
    ]
}

write_to_file(data)