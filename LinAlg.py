import numpy as np
import matplotlib.pyplot as pyplot
import math


# A function that geometrically translates a triangle.
# @param v: The vertices of the triangle as a numpy array
# @param trans: The amount to translate the triangle by, in python list e.g. [x, y]
def translate(v, trans):
    # Find the vertices of the translated triangle
    new_v1 = np.add(v[0], trans)
    new_v2 = np.add(v[1], trans)
    new_v3 = np.add(v[2], trans)
    new_v = np.array([new_v1, new_v2, new_v3])

    # Make the new triangle
    new_triangle = pyplot.Polygon(new_v, color='blue', fill=False)
    pyplot.gca().add_patch(new_triangle)

    # Print new vertices (for debugging)
    print("Translating triangle with vertices (", v[0], ",", v[1], ",", v[2], ") by", trans, "...")
    print("New v1:", new_v1)
    print("New v2:", new_v2)
    print("New v3:", new_v3)
    print("Finished translating.\n")

    return new_v


# A function that geometrically scales a triangle.
# @param v: The vertices of the triangle as a numpy array
# @param sf: The scale factor, in a python list e.g. [x_scale, y_scale]
def scale(v, sf):
    sf_np = np.array([[sf[0], 0],
                      [0, sf[1]]])
    # Find the vertices of the scaled triangle
    new_v1 = np.matmul(v[0], sf_np)
    new_v2 = np.matmul(v[1], sf_np)
    new_v3 = np.matmul(v[2], sf_np)
    new_v = np.array([new_v1, new_v2, new_v3])

    # Make the new triangle
    new_triangle = pyplot.Polygon(new_v, color='green', fill=False)
    pyplot.gca().add_patch(new_triangle)

    # Print new vertices (for debugging)
    print("Scaling triangle with vertices (", v[0], ",", v[1], ",", v[2], ") by x =", sf[0], "and y =", sf[1], "...")
    print("New v1:", new_v1)
    print("New v2:", new_v2)
    print("New v3:", new_v3)
    print("Finished scaling.\n")

    return new_v


# A function that geometrically rotates a triangle.
# @param v: The vertices of the triangle as a numpy array
# @param theta: The amount to be rotated, in degrees
# @param pivot: The axis of rotation, in a python list e.g. [x_coord, y_coord]
def rotate(v, theta, pivot):
    theta_rad = math.radians(theta)  # Convert into radians

    # Form the rotation matrix
    rotation_matrix = np.array([[math.cos(theta_rad), math.sin(theta_rad)],
                               [-1 * math.sin(theta_rad), math.cos(theta_rad)]])

    # Find the new vertices
    new_v1 = np.matmul(np.subtract(v[0], pivot), rotation_matrix) + pivot
    new_v2 = np.matmul(np.subtract(v[1], pivot), rotation_matrix) + pivot
    new_v3 = np.matmul(np.subtract(v[2], pivot), rotation_matrix) + pivot
    new_v = np.array([new_v1, new_v2, new_v3])

    # Make the new triangle
    new_triangle = pyplot.Polygon(new_v, color='orange', fill=False)
    pyplot.gca().add_patch(new_triangle)

    # Print new vertices (for debugging)
    print("Rotating triangle with vertices (", v[0], ",", v[1], ",", v[2], ") by ", theta, "degrees about", pivot, "...")
    print("New v1:", new_v1)
    print("New v2:", new_v2)
    print("New v3:", new_v3)
    print("Finished rotating.\n")

    return new_v

