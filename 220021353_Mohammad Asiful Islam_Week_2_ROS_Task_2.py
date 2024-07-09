#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

turtle_pose = Pose()

def pose_callback(data):
    global turtle_pose
    turtle_pose = data

def move_circle():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    twist = Twist()
    twist.linear.x = 2.0
    twist.angular.z = 1.0

    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()

def move_square():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(0.5)

    for _ in range(4):
        twist = Twist()
        twist.linear.x = 2.0
        pub.publish(twist)
        rospy.sleep(2.0)

        twist = Twist()
        twist.angular.z = math.pi / 2
        pub.publish(twist)
        rospy.sleep(1.5)

def move_spiral():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)

    radius = 1.0
    omega = 0.5
    vel_forward = 1.0

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = vel_forward
        twist.angular.z = omega
        pub.publish(twist)
        rospy.sleep(1.0)

        radius += 0.5
        vel_forward += 0.2

def main():
    rospy.init_node('turtle_controller', anonymous=True)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    user_input = input("Enter movement type (A for circle, B for square, C for spiral): ").upper()

    if user_input == 'A':
        move_circle()
    elif user_input == 'B':
        move_square()
    elif user_input == 'C':
        move_spiral()
    else:
        rospy.logerr("Invalid input. Please enter A, B, or C.")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
