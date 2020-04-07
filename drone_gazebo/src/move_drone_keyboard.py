#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
#from itertools import count
from pynput.keyboard import Key, Listener
u=0
w=0
o=0
#import tkinter as tk
#index=count(start=0.2,step=0)
#HEIGHT = 700
#WIDTH = 1000
#root=tk.Tk()
#t=[]
#def close():
#	root.destroy()
#rospy.init_node('up', anonymous=True)
def on_press(key):
    #print('{0} pressed'.format(
        #key))
	up(key)
		
def on_release(key):
    #print('{0} release'.format(
       # key))
    if key == Key.esc:
        # Stop listener
        return False
pub_name=rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=100)
na=ModelState()
na.model_name="drone"
#na.pose.position.z=1
#pub_name.publish(na)
def up(key):
	if key == Key.up:
		u=0.1
		i=float(na.pose.position.y)
		na.pose.position.y=i+u
	elif key == Key.down:
		u=-0.1
		i=float(na.pose.position.y)
		na.pose.position.y=i+u
	elif key == Key.insert:
		o=0.1
		t=float(na.pose.position.z)
		na.pose.position.z=t+o
	elif key == Key.delete:
		o=-0.1
		t=float(na.pose.position.z)
		na.pose.position.z=t+o
	elif key == Key.left:
		w=0.1
		b=float(na.pose.position.x)
		na.pose.position.x=b+w
	elif key == Key.right:
		w=-0.1
		b=float(na.pose.position.x)
		na.pose.position.x=b+w
	#pub_name.publish(na)	
	
	#t.append(next(index))
	#c=t[-1]
	
	#pub_name.publish(na)
#def side(key):
	
	
#def NorthEast(key):
	elif key == Key.page_up:
		w=0.1
		b=float(na.pose.position.x)
		p=float(na.pose.position.y)
		na.pose.position.x=b+w
		na.pose.position.y=p+w
	elif key == Key.end:
		w=-0.1
		b=float(na.pose.position.x)
		p=float(na.pose.position.y)
		na.pose.position.x=b+w
		na.pose.position.y=p+w
	elif key == Key.home:
		w=0.1
		t=-0.1
		b=float(na.pose.position.x)
		p=float(na.pose.position.y)
		na.pose.position.x=b+t
		na.pose.position.y=p+w
	elif key == Key.page_down:
		w=-0.1
		t=0.1
		b=float(na.pose.position.x)
		p=float(na.pose.position.y)
		na.pose.position.x=b+t
		na.pose.position.y=p+w
	pub_name.publish(na)
	pub_name.publish(na)

#def front(key):
	
	#pub_name=rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=100)
	#na=ModelState()
	#na.model_name="drone"
	#na.pose.position.z=1
	#r=float(a)
	
	#t.append(next(index))
	#c=t[-1]
	
	#pub_name.publish(na)




rospy.init_node('side', anonymous=True) 
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
#rospy.init_node('front', anonymous=True)
if __name__ == '__main__':
	#root.mainloop()
	rospy.spin()

