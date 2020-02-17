#!/usr/bin/env python

import rospy
from std_msgs.msg import String

varS = None

def callback(data):
    global varS
    varS = data.data


def talker():
    rospy.init_node('Obj_test', anonymous=True)  #Init a unique node
    rospy.Subscriber('chatter_1', String, callback) #create a subscriber
    
    pub = rospy.Publisher('chatter', String, queue_size=10) #create a publisher
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
     
        if varS == "hi":
            sm = "HOLA"
            print("Miguel")
            print("ECUADOR")
            rospy.loginfo(sm)
            pub.publish(sm)
            rate.sleep()
        else:
            sm = "NO HOLA"
        
        
    rospy.spin()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
