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

from rclpy.node import Node
import json

from std_msgs.msg import String


topic = "/speech/nlu"

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, topic, 10)

    def data_callback(self, data):
        #self.get_logger().info(type(data))
        #self.get_logger().info(data)
        msg = String()
        msg.data = json.dumps(data)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
