#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import Matrix, MatrixResponse
import rospy
import numpy as np

def handle_matrix(req):
    mode = rospy.get_param('mode', 'sum')
    matrix = np.array([[req.a11,req.a12],
                       [req.a21,req.a22]])
    if mode == 'sum':
        return MatrixResponse(np.sum(matrix))
    elif mode == 'max':
        return MatrixResponse(np.amax(matrix))
    elif mode == 'min':
        return MatrixResponse(np.amin(matrix))
    elif mode == 'det':
        return MatrixResponse(np.linalg.det(matrix))
    else:
        return MatrixResponse(-1)

def matrix_server():
    rospy.init_node('matrix_server')
    s = rospy.Service('matrix', Matrix, handle_matrix)
    print("Matrix Serivce is ready")
    rospy.spin()

if __name__ == "__main__":
    matrix_server()