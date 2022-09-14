#!/usr/bin/env python

from __future__ import print_function
from beginner_tutorials.srv import Matrix
import rospy

def matrix_client():
    print('Testing Matrix Service')
    rospy.wait_for_service('matrix')
    modes = ['sum','max','min','det']
    a11 = 1; a12 = 2; a21 = 3; a22 = 4
    print("Inputs: a11 =",a11, "a12 =",a12, "a21 =",a21, "a22 =", a22)
    for mode in modes:
        rospy.set_param('mode', mode)
        try:
            matrix = rospy.ServiceProxy('matrix', Matrix)
            response = matrix(a11,a12,a21,a22)
            print("Mode Parameter:",mode)
            print("Result:",response.result)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)

if __name__ == "__main__":
    matrix_client()

