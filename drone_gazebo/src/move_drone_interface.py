#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import String
from gazebo_msgs.msg import ModelState
from itertools import count

import tkinter as tk
index=count(start=0.2,step=0)
HEIGHT = 700
WIDTH = 1000
root=tk.Tk()
t=[]
def close():
	root.destroy()
#rospy.init_node('up', anonymous=True)
pub_name=rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=100)
na=ModelState()
na.model_name="drone"
#na.pose.position.z=1
#pub_name.publish(na)
def up(a):
	u=float(a)
	i=float(na.pose.position.z)
	#t.append(next(index))
	#c=t[-1]
	na.pose.position.z=u+i
	pub_name.publish(na)
def side(a):
	
	#pub_name=rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=100)
	#na=ModelState()
	#na.model_name="drone"
	#na.pose.position.z=1
	a=float(a)
	b=float(na.pose.position.x)
	#t.append(next(index))
	#c=t[-1]
	na.pose.position.x=a+b
	pub_name.publish(na)
	
def front(a):
	
	#pub_name=rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=100)
	#na=ModelState()
	#na.model_name="drone"
	#na.pose.position.z=1
	r=float(a)
	t=float(na.pose.position.y)
	#t.append(next(index))
	#c=t[-1]
	na.pose.position.y=r+t
	pub_name.publish(na)
def NorthWest(a):
	w=float(a)
	b=float(na.pose.position.x)
	p=float(na.pose.position.y)
	na.pose.position.x=b+w
	na.pose.position.y=p+w
	pub_name.publish(na)
def SouthWest(a):
	w=float(a)
	b=float(na.pose.position.x)
	p=float(na.pose.position.y)
	na.pose.position.x=b+w
	na.pose.position.y=p-w
	pub_name.publish(na)
def NorthEast(a):
	w=float(a)
	b=float(na.pose.position.x)
	p=float(na.pose.position.y)
	na.pose.position.x=b-w
	na.pose.position.y=p+w
	pub_name.publish(na)
def SouthEast(a):
	w=float(a)
	b=float(na.pose.position.x)
	p=float(na.pose.position.y)
	na.pose.position.x=b-w
	na.pose.position.y=p-w
	pub_name.publish(na)



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#11d6f0') 
frame.place(relx= 0.1, rely=0.1, relwidth= 0.8, relheight = 0.8)

button = tk.Button(root, text="Close", bg='gray', fg='red', command=lambda: close())
button.place(relx=0, rely=0 , relwidth=0.15, relheight=0.05)

button = tk.Button(frame, text="Taking off", bg='gray', fg='red', command=lambda: up(0.05))
button.place(relx=0.1, rely=0.1 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="Landing", bg='gray', fg='red', command=lambda: up(-0.05))
button.place(relx=0.1, rely=0.31 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="Forward", bg='gray', fg='red', command=lambda: front(0.05))
button.place(relx=0.6, rely=0.15 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="Backward", bg='gray', fg='red', command=lambda: front(-0.05))
button.place(relx=0.6, rely=0.55 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="Left", bg='gray', fg='red', command=lambda: side(-0.05))
button.place(relx=0.4, rely=0.35 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="Right", bg='gray', fg='red',command=lambda: side(0.05))
button.place(relx=0.8, rely=0.35 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="North West", bg='gray', fg='red',command=lambda: NorthWest(0.05))
button.place(relx=0.8, rely=0.15 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="South West", bg='gray', fg='red',command=lambda: SouthWest(0.05))
button.place(relx=0.8, rely=0.55 , relwidth=0.2, relheight=0.2)

button = tk.Button(frame, text="North East", bg='gray', fg='red',command=lambda: NorthEast(0.05))
button.place(relx=0.4, rely=0.15 , relwidth=0.2, relheight=0.2)
button = tk.Button(frame, text="South East ", bg='gray', fg='red',command=lambda: SouthEast(0.05))
button.place(relx=0.4, rely=0.55 , relwidth=0.2, relheight=0.2)


rospy.init_node('side', anonymous=True) 
#rospy.init_node('front', anonymous=True)
if __name__ == '__main__':
	root.mainloop()
	rospy.spin()

