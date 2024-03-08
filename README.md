# Ros2-Snips-NLU

To extract the user's intention in the transcript of the spoken word, this ROS2 node is developed.
It uses spacy to splitt multiple sentences and gets the intent of each.

## Ros topics
Listens to '/speech/stt' topic and publishes on '/speech/nlu'

## Requirements and installation

pip3 install spacy
python3 -m spacy download en_core_web_sm
pip3 install snips-nlu
python3 -m snips_nlu download en

Download git into ros2 workspace and colcon build as usual.
The model path needs to be changed
