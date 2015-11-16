class Point:
    x = 0
    y = 0
    def __init__(self, str = '0,0'):
        self.x, self.y = str.split(',')
        self.x, self.y = float(self.x), float(self.y)
    def __str__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
    def __add__(self, other):
        return Point(str(self.x +other.x) + ',' + str(self.y + other.y))
    def __truediv__(self, number):
        return Point(str(self.x / number) + ',' + str(self.y / number))
    def Distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def DistanceTo(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    def Perimetr(self, other1, other2):
        return self.DistanceTo(other1) + other1.DistanceTo(other2) + other2.DistanceTo(self)
    def Square(self, Other1, Other2):
        p = self.Perimetr(Other1, Other2) / 2
        a = self.DistanceTo(Other1)
        b = Other1.DistanceTo(Other2)
        c = Other2.DistanceTo(self)
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

N = int(input())
Points = []
for i in range(N):
    Points.append(Point(input()))
Max_square = Points[0].Square(Points[1], Points[2])
A = Points[0]
B = Points[1]
C = Points[2]
for point1 in Points:
      for point2 in Points:
          for point3 in Points:
              if point1.Square(point2, point3) > Max_square:
                  Max_square = point1.Square(point2, point3)
                  A = point1
                  B = point2
                  C = point3
print(A, B, C, Max_square)
