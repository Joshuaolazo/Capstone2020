#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import Twist
PI = 3.1415926535897

if __name__ == '__main__':
    count = 0

    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while(True):
        try:
            fo = open("../mediapipe/Gouts.txt", "r")
        except (OSError, IOError) as e:
            print("Race Con")
        fo.seek(count)
        line = fo.readline()
        if(line):
            print (line)
            if(line =='ROCK'):
                vel_msg.linear.x = 0
                vel_msg.angular.z = 0
            if (line == 'ONE'):
                vel_msg.linear.x = 1
            if (line == 'TWO'):
                vel_msg.linear.x = 2
            if (line == 'THREE'):
                vel_msg.linear.x = 3
            if (line == 'FOUR'):
                vel_msg.linear.x = 4
            if (line == 'FIVE'):
                vel_msg.linear.x = 5
            if (line == 'HANG LOOSE'):
                vel_msg.angular.z = 1*2*PI/360
            if (line == 'SPIDERMAN'):
                vel_msg.angular.z = -1*2*PI/360

        count=count+len(line)

        try:
            velocity_publisher.publish(vel_msg)
        except rospy.ROSInterruptException:
            print('ros exception')
            pass

        time.sleep(.05)

