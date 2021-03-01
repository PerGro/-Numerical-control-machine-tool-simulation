import turtle
import numpy as np
from numpy import arccos

def move_to():
    return 'move_to', turtle.goto

def move_to_temp(kwargs):
    x = kwargs['X']
    y = kwargs['Y']
    return x, y

def pu():
    turtle.pu()

def pd():
    turtle.pd()

def circle_l():
    return 'circle_l', turtle.circle

def circle_r():
    return 'circle_r', turtle.circle

def clockwise_circle(kwargs):
    turtle.seth(0)
    if kwargs.get('I') is None:
        x = kwargs.get('X')
    else:
        x = kwargs.get('I')
    if kwargs.get('J') is None:
        y = kwargs.get('Y')
    else:
        y = kwargs.get('J')
    r = kwargs.setdefault('R', None)
    if r is None:
        turtle.seth(0)
        turtle.goto(-x, -y)
        turtle.seth(180)
        return (x ** 2 + y ** 2) ** 0.5, 360
    else:
        last_point = kwargs['last_point']
        center = find_center(x - last_point[0], y - last_point[1], r)
        if r > 0:
            theta = change_turtle_orientation(center[1][0], center[1][1], kwargs['last_point'])
            turtle.seth(theta)

            x_difference = abs(last_point[0] - x)
            y_difference = abs(last_point[1] - y)
            # change_turtle_orientation(x - last_point[0], y - last_point[1], last_point)
            distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
            another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
            theta = np.arccos(another_line / (2 * r)) * 2
            theta = theta * 180 / np.pi
            return abs(r), -theta
        elif r < 0:
            theta = change_turtle_orientation(center[0][0], center[0][1], kwargs['last_point'])
            turtle.seth(theta)

            x_difference = abs(last_point[0] - x)
            y_difference = abs(last_point[1] - y)
            distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
            another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
            theta = np.arccos(another_line / (2 * r)) * 2
            theta = theta * 180 / np.pi
            return abs(r), -theta

def anti_clockwise_circle(kwargs):
    turtle.seth(0)
    if kwargs.get('I') is None:
        x = kwargs.get('X')
    else:
        x = kwargs.get('I')
    if kwargs.get('J') is None:
        y = kwargs.get('Y')
    else:
        y = kwargs.get('J')
    r = kwargs.setdefault('R', None)
    if r is None:
        turtle.seth(0)
        turtle.goto(-x, -y)
        turtle.seth(180)
        return (x ** 2 + y ** 2) ** 0.5, 360
    else:
        last_point = kwargs['last_point']
        center = find_center(x - last_point[0], y - last_point[1], r)
        if r > 0:
            theta = change_turtle_orientation(center[0][0], center[0][1], kwargs['last_point'])
            turtle.seth(theta)

            x_difference = abs(last_point[0] - x)
            y_difference = abs(last_point[1] - y)
            distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
            another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
            theta = np.arccos(another_line / (2 * r)) * 2
            theta = theta * 180 / np.pi
            return abs(r), theta
        elif r < 0:
            theta = change_turtle_orientation(center[1][0], center[1][1], kwargs['last_point'])
            turtle.seth(theta)

            x_difference = abs(last_point[0] - x)
            y_difference = abs(last_point[1] - y)
            distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
            another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
            theta = np.arccos(another_line / (2 * r)) * 2
            theta = theta * 180 / np.pi
            return abs(r), theta

def change_turtle_orientation(x, y, last_point):
    distance = (x ** 2 + y ** 2) ** 0.5
    _sin = y / distance
    _cos = x / distance
    if _sin >= 0:
        return -90 + np.arccos(_cos) * 180 / np.pi
    else:
        return 270 - np.arccos(_cos) * 180 / np.pi

def find_center(x, y, r):
    distance = (x ** 2 + y ** 2) ** 0.5
    _sin = y / distance
    theta = np.arccos(x / distance) * 180 / np.pi
    point = np.array([x, y])
    if _sin > 0:
        matrix = _get_rotate_m(theta)
    else:
        matrix = _get_rotate_m(-theta)
    new_coor = np.dot(point, matrix)
    midpoint = new_coor[0] / 2
    center_y_p = (r ** 2 - midpoint ** 2) ** 0.5
    center_y_n = -center_y_p
    center_x = midpoint
    center_p = np.array([center_x, center_y_p])
    center_n = np.array([center_x, center_y_n])
    if _sin > 0:
        matrix = _get_rotate_m(-theta)
    else:
        matrix = _get_rotate_m(theta)
    center_p = list(np.dot(center_p, matrix))
    center_n = list(np.dot(center_n, matrix))
    return [center_p, center_n]

def _get_rotate_m(theta):
    theta = theta * np.pi / 180
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])




class StepsCounter:
    def __init__(self):
        self.step = 0

    @staticmethod
    def move_to():
        return 'move_to', turtle.goto

    @staticmethod
    def move_to_temp(kwargs):
        x = kwargs['X']
        y = kwargs['Y']
        return x, y

    def clockwise_circle(self, kwargs):
        turtle.seth(0)
        self.step += 1
        if kwargs.get('I') is None:
            x = kwargs.get('X')
        else:
            x = kwargs.get('I')
        if kwargs.get('J') is None:
            y = kwargs.get('Y')
        else:
            y = kwargs.get('J')
        r = kwargs.setdefault('R', None)
        if r is None:
            turtle.goto(-x, -y)
            self.step += 1
            turtle.seth(180)
            self.step += 1
            return (x ** 2 + y ** 2) ** 0.5, 360
        else:
            last_point = kwargs['last_point']
            center = find_center(x - last_point[0], y - last_point[1], r)
            if r > 0:
                theta = change_turtle_orientation(center[1][0], center[1][1], kwargs['last_point'])
                turtle.seth(theta)
                self.step += 1

                x_difference = abs(last_point[0] - x)
                y_difference = abs(last_point[1] - y)
                # change_turtle_orientation(x - last_point[0], y - last_point[1], last_point)
                distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
                another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
                theta = np.arccos(another_line / (2 * r)) * 2
                theta = theta * 180 / np.pi
                return abs(r), -theta
            elif r < 0:
                theta = change_turtle_orientation(center[0][0], center[0][1], kwargs['last_point'])
                turtle.seth(theta)
                self.step += 1

                x_difference = abs(last_point[0] - x)
                y_difference = abs(last_point[1] - y)
                distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
                another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
                theta = np.arccos(another_line / (2 * r)) * 2
                theta = theta * 180 / np.pi
                return abs(r), -theta

    def anti_clockwise_circle(self, kwargs):
        turtle.seth(0)
        self.step += 1
        if kwargs.get('I') is None:
            x = kwargs.get('X')
        else:
            x = kwargs.get('I')
        if kwargs.get('J') is None:
            y = kwargs.get('Y')
        else:
            y = kwargs.get('J')
        r = kwargs.setdefault('R', None)
        if r is None:
            turtle.goto(-x, -y)
            self.step += 1
            turtle.seth(180)
            self.step += 1
            return (x ** 2 + y ** 2) ** 0.5, 360
        else:
            last_point = kwargs['last_point']
            center = find_center(x - last_point[0], y - last_point[1], r)
            if r > 0:
                theta = change_turtle_orientation(center[0][0], center[0][1], kwargs['last_point'])
                turtle.seth(theta)
                self.step += 1

                x_difference = abs(last_point[0] - x)
                y_difference = abs(last_point[1] - y)
                distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
                another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
                theta = np.arccos(another_line / (2 * r)) * 2
                theta = theta * 180 / np.pi
                return abs(r), theta
            elif r < 0:
                theta = change_turtle_orientation(center[1][0], center[1][1], kwargs['last_point'])
                turtle.seth(theta)
                self.step += 1

                x_difference = abs(last_point[0] - x)
                y_difference = abs(last_point[1] - y)
                distance = (x_difference ** 2 + y_difference ** 2) ** 0.5
                another_line = ((r * 2) ** 2 - distance ** 2) ** 0.5
                theta = np.arccos(another_line / (2 * r)) * 2
                theta = theta * 180 / np.pi
                return abs(r), theta

    def pu(self):
        self.step += 1
        turtle.pu()

    def pd(self):
        self.step += 1
        turtle.pd()

    def get(self):
        return self.step


