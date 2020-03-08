import math
import enum

class Axis(enum.Enum):
    X_AXIS = 0
    Y_AXIS = 1
    BOTH = 2

class Point:
    x: float = 0
    y: float = 0

    def __init__(self, x, y):
        # init class with x,y values
        self.x = x
        self.y = y

    def translate(self, offset_x: float, offset_y: float):
        # add offset values to respective axes values
        self.x += offset_x
        self.y += offset_y

        return self

    def rotate(self, rotation_angle: float, rotation_point: tuple([float, float])):
        # turn angle into radians because that's what the formula requires
        rotation_radians = math.radians(rotation_angle)

        # translate the system to be relative to the rotation point 
        self.translate(-rotation_point[0], -rotation_point[1])

        # rotate with sine / cosine formulas
        # https://gist.github.com/LyleScott/e36e08bfb23b1f87af68c9051f985302 check for more info
        old_x = self.x
        old_y = self.y

        # round due to floating point precision causing results like such as "-1.9999999999999998"
        self.x = round(
            old_x * math.cos(rotation_radians) + old_y * math.sin(rotation_radians),
            10)
        self.y = round(
            -old_x * math.sin(rotation_radians) + old_y * math.cos(rotation_radians),
            10)

        # translate the system back to being relative to origin
        self.translate(rotation_point[0], rotation_point[1])
        return self

    def reflect(self, reflection_axis: Axis, reflection_point: tuple([float, float])):
        # no switch case in python so i have to use if statements ._.

        # get distance from reflection point y to self y and put it on other side
        if (reflection_axis == Axis.X_AXIS):
            self.y = reflection_point[1] - (self.y - reflection_point[1])

        elif (reflection_axis == Axis.Y_AXIS):
            self.x = reflection_point[0] - (self.x - reflection_point[0])

        elif (reflection_axis == Axis.BOTH):
            self.y = reflection_point[1] - (self.y - reflection_point[1])
            self.x = reflection_point[0] - (self.x - reflection_point[0])
        
        return self

    def dilate(self, scale_factor: float, dilation_point: tuple([float, float])):
        self.x = scale_factor * self.x - dilation_point[0]
        self.y = scale_factor * self.y - dilation_point[1]

        return self

    
    def __str__(self):
        # returns nice string version of class
        return f"({str(self.x)}, {str(self.y)})"


origin_point = Point(0,0)