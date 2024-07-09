#publisher node code:

#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publisher():
    # Initialize the ROS node for the publisher
    rospy.init_node('publisher_node', anonymous=True)

    # Create a publisher with topic name 'chatter' and message type 'String'
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # Rate at which to publish (10 Hz)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # Message to be published
        message = "Hello world"
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

#subscriber node code:

#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard: %s", data.data)

def subscriber():
    # Initialize the ROS node for the subscriber
    rospy.init_node('subscriber_node', anonymous=True)

    # Subscribe to the 'chatter' topic and register a callback function
    rospy.Subscriber('chatter', String, callback)

    # Spin keeps Python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()

'''for launching, the following commands were used in the terminal:

    mkdir launch
    nano launch/demo.launch
    <launch>
  <!-- Start publisher_node -->
  <node name="publisher_node" pkg="publisher_subscriber_demo" type="publisher_node.py" output="screen" />

  <!-- Start subscriber_node -->
  <node name="subscriber_node" pkg="publisher_subscriber_demo" type="subscriber_node.py" output="screen" />
</launch>

'''

