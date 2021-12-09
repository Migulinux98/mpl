from math import sqrt

def triangle(a, b, c):
    
    if a<(b+c) and b<(a+c) and c<(a+b):
        sp=(a+b+c)/2

        area = sqrt(sp*(sp-a)*(sp-b)*(sp-c))

        return area
   
    else:
   
        return(0)


total = triangle(10, 10, 10)

if total > 0:
    print("The area is: ", total)
else: 
    print("The triangle doesnt exist")
