class Point:
  points_counter = 0
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y
    Point.points_counter += 1

  def move_coords(self, x = 0, y = 0):
    self.x = x
    self.y = y

object_0 = Point()
object_1 = Point(3, 6)
object_2 = Point(2, 8)
print(Point.points_counter)
print(object_2.points_counter)

# # print(object_0.x, object_0.y)
# print(object_1.x, object_1.y)
# # print(object_2.x, object_2.y)

# object_1.move_coords(5, 7)
# print(object_1.x, object_1.y)