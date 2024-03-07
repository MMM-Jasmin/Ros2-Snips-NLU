import io
import json
import random
from os.path import exists as file_exists
import csv
#from yaml import parse

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_DE


modelpath= "models/snips-model-jonas"


class SnipsNLU():

    def __init__(self):
        print("Init Snips")
        if(file_exists(modelpath)):
            print("Model exists, loading...")
            self.engine = SnipsNLUEngine.from_path(modelpath)
        else:
            print("Model doesn't exist, training...")
            raise FileNotFoundError("No model found at: " + modelpath)

    def parse(self, utterance):
        parsing = self.engine.parse(utterance)
        #print(json.dumps(parsing, indent=2))
        return parsing




utterances  = []
intents = []
entitys = []

### Load SnipsNLU ### 
snips = SnipsNLU()

### Read in test file ###
with open("test_all-mal_vier.csv") as file :
    csvData = csv.reader(file, delimiter=';')
    for row in csvData:
        parsed = snips.parse(row[0])
        intentName= parsed["intent"]["intentName"]
        #print(parsed)
        slots = parsed["slots"]
        slotnames = []
        slotValues = []
        slotRawValues= []
        entities = []
        for slot in slots:
            slotname = slot["slotName"]
            slotnames.append(slot["slotName"])
            try:
                slotValue = slot["value"]["value"]
                slotValues.append(slot["value"]["value"])
            except:
                slotValue = slot["value"]
                slotValues.append(slot["value"])
            slotRawValue = slot["rawValue"]
            slotRawValues.append(slot["rawValue"])
            entities.append(f"{slotname}: {slotValue} erkannt aus: {slotRawValue}")

        #print("---------------------------------------------------------------")
        #print(f"Gegeben: {row[1]} und bekommen: {intentName}" )
        #if(row[1] != intentName):
        #   print(parsed)
        #print(row[2:])
        #print(parsed["slots"])
        #print(parsed["slots"] in row[2:])
        #utterances.append(row[0])
        #intents.append(row[1])
        #entitys.append(row[2:])
        if(slots):
            #print(f"{intentName} + {slotnames} + {slotValues} + {slotRawValues}" )
            print(f"{intentName}, {entities} " )
        else:
            print(f"{intentName}")




#print(utterances)
#print(intents)
#print(entitys)
