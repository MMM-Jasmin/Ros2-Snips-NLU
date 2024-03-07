import io
import json
from os.path import exists as file_exists
import time
    
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN as CONFIG

def trainer(datasetpath, modelpath):

    engine = SnipsNLUEngine(config=CONFIG)

    with io.open(datasetpath) as f:
        dataset = json.load(f)

    engine.fit(dataset)

    engine.persist(modelpath)
    return engine

print("Start Training")
start = time.time()
trainer("datasets/dataset_english.json" , "/opt/dev/DL_Models/snips/snips-model-english")
end = time.time()
timer = end -start
print(f"Finished. Elapsed Time: {timer}")