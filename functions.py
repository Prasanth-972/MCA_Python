num=int(input("Enter the number:"))
list=[i for i in range(1,num+1)if num%i==0]
print("factors of number=",list)
print("\nEnter length and breadth of a rectangle:")
l=int(input("length:"))
b=int(input("breadth:"))
c=lambda x, y: x*y
print("Area of rectagnle:",c(l,b))
print("\nEnter side of square:")
s=int(input("Side of square:"))
c=lambda x: x*x
print("Area of Square:",c(s))
