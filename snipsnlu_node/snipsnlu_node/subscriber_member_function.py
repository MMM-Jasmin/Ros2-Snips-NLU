# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import re
import spacy

from snipsnlu_node.snipsNLU import SnipsNLU
from snipsnlu_node.publisher_member_function import MinimalPublisher

topic = "/speech/stt"
intent_threshhold = 0.5


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            topic,
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.publisher = MinimalPublisher()
        self.snips_engine = SnipsNLU()
        self.nlp = spacy.load('en_core_web_sm')

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        msg.data = re.sub("[\(\[].*?[\)\]]", "", msg.data) # remove everything between brackets like [silence] or [music]
        msg.data = msg.data.replace("  ", " ")

        if (msg.data == ""):
            self.get_logger().info('Doing nothing! This message is empty!')
        else:
            doc = self.nlp(msg.data)
            for sentence in doc.sents:
                #print(type(sentence.text))
                ret = self.snips_engine.parse(sentence.text)
                #self.get_logger().info(f'Snips Ergebnis: {ret}')
                if(ret["intent"]["intentName"] is not None and ret["intent"]["probability"] > intent_threshhold):
                    self.publisher.data_callback(ret)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
