#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

print("let's go")
cap = cv2.VideoCapture(0)
print(cap.isOpened())
bridge = CvBridge()
print('works')

def talker():
    pub = rospy.Publisher('/camera', Image, queue_size = 10)
    rospy.init_node('video', anonymous = False)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            print('ret problam')
            break

        msg = bridge.cv2_to_imgmsg(frame, 'bgr8')
        pub.publish(msg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("I think that's enough")
            break

        if rospy.is_shutdown():
            cap.release()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass