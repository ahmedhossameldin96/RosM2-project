#!/usr/bin/env python
# license removed for brevity

import rospy
import time
# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
time.sleep(3)
def movebase_client():

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = -3.48043991147
     # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.y = -5.6414751419

   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.z = 0.996353092292

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()

#==========================Goal_2===========================================================

  # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = -11.4222366751
     # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.y = 1.22998199221

   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.z = 0.522209530364

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()

#==========================Goal_2_END===========================================================

#==========================Goal_3===========================================================

  # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = 8.70894392741
     # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.y = -1.6491300936

   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.z = 0.00723063986655

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()

#==========================Goal_3_END===========================================================





   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")