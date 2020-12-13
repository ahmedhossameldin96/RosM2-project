#! /usr/bin/env python

import rospy
import time
from nav_msgs.msg import Odometry

def callback(msg1):
	
	x_position=msg1.pose.pose.position.x
	y_position=msg1.pose.pose.position.y
	z_orientation=msg1.pose.pose.orientation.z


	print ("--- Position X-> " + str(x_position) + " || Position Y-> " + str(y_position) + " || Orientation Z-> " + str(z_orientation) + " ---")
	time.sleep(1)


rospy.init_node('subscriber1')
sub = rospy.Subscriber('odom', Odometry, callback)
rospy.spin()
