#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState

def pub():
	rospy.init_node('pub', anonymous=True)
	pub_name=rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=100)
	rate = rospy.Rate(60) 
	na=ModelState()
	#a=na.pose.position.x
	while not rospy.is_shutdown():
		na.model_name="drone"
		na.pose.position.z=1
		na.pose.position.x+=0.005
		na.pose.position.y+=0.005
		pub_name.publish(na)
		rate.sleep()

if __name__ == '__main__':
	try:
	 pub()
	except rospy.ROSInterruptException:
	 pass
