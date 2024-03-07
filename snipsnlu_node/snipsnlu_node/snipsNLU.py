import io
import json
from os.path import exists as file_exists

from snips_nlu import SnipsNLUEngine
#from snips_nlu.default_configs import CONFIG_DE


#modelpath= "models/snipsmodels/models/snips-model-all"
#modelpath= "/opt/dev/DL_Models/snips/snips-model-all"
modelpath= "/opt/dev/DL_Models/snips/snips-model-english"

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




def main(args=None):
    snipper = SnipsNLU()

    snipper.parse("how is the weather in Bielefeld?")
    snipper.parse("could you play Fix you from Coldplay")
    snipper.parse("i would like to hear scooter")
    #snipper.parse(" Gibt es heute etwas angebot in der Mensa?")


if __name__ == '__main__':
    main()
