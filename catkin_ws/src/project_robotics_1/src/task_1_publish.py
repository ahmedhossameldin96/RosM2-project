#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist


rospy.init_node('topict1')
pub = rospy.Publisher('/cmd_vel', Twist,queue_size=1)
rate = rospy.Rate(2)
move = Twist()
move.linear.x = 0.2
move.angular.z = 0.8



counter=0
while not rospy.is_shutdown(): 
  pub.publish(move)
  rate.sleep()
  counter=counter+1
  print(counter)
  if counter==30 :
    move.linear.x = 0
    move.angular.z = 0
    pub.publish(move)

    break