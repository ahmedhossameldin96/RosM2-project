# ROS kinetics project implementation tutorial
In this repository, the provided package establishes a variety of challenging tasks. These tasks, provide basic functionalities of the Turtlebot3 robot in a given map.

## Tasks

- Create a script that moves the robot around with simple /cmd_vel topic publishing. 
- Generate the full map of the cafeteria and then localize the Turtlebot3 robot.
- Set up an automatic system that provides the robot to move from its position to a goal without colliding with any object.
- Set up an automatic system that provides the robot to move from its position to a set of waypoints.

### Prerequisites

This repository works in [The Construct](https://www.theconstructsim.com/robotigniteacademy_learnros/ros-courses-library/) site. Place the **project_robotics_1** package inside **/catkin_ws/src**.

```
Specific course: ** Mastering with ROS: Turtlebot3 -> 8-Project Part 1 **
```

## Task1 : Create a script that moves the robot around with simple /cmd_vel topic publishing.

<p align="center">
<img  src = "resources/task_1.png" width=400> <br>
<em> Task 1 results.</em>

As you can see in the above figure. These files are essential for moving the robot in circles and printing its current location.

### Terminal commands

-  In Terminal#1 write this specific command:
```
roslaunch project_robotics_1 task_1_move.launch
```
-	Now, you see in the **Simulation** windows the Turtlebot3 moving in circles and printing its position and orientation!

 
## Task2 : Generate the full map of the cafeteria and then localize the Turtlebot3 robot.

In this task, we can divide the process into two subtasks to observe the different results.
### Mapping

First step is to generate a map using the Turtlbot3’s laser. This laser will scan its area with a combination of tools/steps.

#### Tools - Steps

- In Terminal#2 write this specific command (Robot movement keyboard):
```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
- In Terminal#3 write this specific command (Robot’s GUI):
```
rosrun rviz rviz
```






