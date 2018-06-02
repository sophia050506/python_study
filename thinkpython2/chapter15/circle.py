import math

class Point:
    pass

class Circle:
    pass

'''
判断点是否在圆中
'''
def point_in_circle(circle, point):
    dy = circle.p.y - point.y
    dx = circle.p.x - point.x
    d = math.sqrt(dx ** 2 + dy ** 2)
    if d > circle.r:
        return False
    else:
        return True

class Rectangle:
    pass

'''
矩形是否完全在圆内或者在圆上
思路：确定矩形四个角坐标，判断到圆心的距离是否<=半径
假定给了矩形的左上角的坐标及长和宽
'''
def rect_in_circle(circle, rectangle):
    p = Point()
    p.x = rectangle.p.x
    p.y = rectangle.p.y

    p1 = Point()
    p1.x = rectangle.p.x  # 左下角坐标
    p1.y = rectangle.height + rectangle.p.y

    p2 = Point()
    p2.x = rectangle.width + rectangle.p.x # 右上角坐标
    p2.y = rectangle.p.y

    p3 = Point()
    p3.x = rectangle.width + rectangle.p.x # 右下角坐标
    p3.y = rectangle.height + rectangle.p.y

    if point_in_circle(circle,p) and point_in_circle(circle,p1) and point_in_circle(circle,p2) and point_in_circle(circle,p3):
        return True
    else:
        return False

circle = Circle()
circle.r = 75
circle.p = Point()
circle.p.x = 150
circle.p.y = 100

point = Point()
point.x = 2
point.y = 2
#print(point_in_circle(circle,point))

rectangle = Rectangle()
rectangle.p = Point()
rectangle.p.x = 0
rectangle.p.y = 0
rectangle.width = 200
rectangle.height = 10
print(rect_in_circle(circle,rectangle))

