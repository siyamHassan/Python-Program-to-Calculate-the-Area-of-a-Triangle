import math
# Python Program to find the area of triangle
a = float(input("Entre Frist side:"))
b= float(input("Enter second side:"))
c = float(input("Entre third side"))
def Triangle(a,b,c):
    if (a+b)>c and (b+c)>a and (c+a)>b:
      s = (a+b+c)/2
      result = math.sqrt(s*(s-a)*(s-b)*(s-c))
      return result
    else:
        return "Triangle is not posible"
iam_result = Triangle(a,b,c)
print(f"Triangle is {iam_result}")
