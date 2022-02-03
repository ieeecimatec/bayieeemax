#!/usr/bin/env python
from cmath import sqrt
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed_x = float(input("Input your X speed:"))
    speed_y = float(input("Input your Y speed:"))
    distance = float(input("Type your distance:"))

    #Since we are moving just in x-axis
    vel_msg.linear.x = speed_x
    vel_msg.linear.y = speed_y
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    t0 = rospy.Time.now().to_sec()
    finishMove = False

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        
        current_distance = 0

        #Loop to move the turtle in an specified distance
        
        while(not finishMove):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            speed_vector = sqrt(speed_x**2 + speed_y**2)
            current_distance= abs(speed_vector)*(t1-t0)
            print(f'{current_distance}\t{distance}')
            if(current_distance >= distance):
                finishMove = True 
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass