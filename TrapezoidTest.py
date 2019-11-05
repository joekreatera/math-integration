
def linear(x):
    return x


def quadratic(x):
    return x*x


def trapezoids(fn,a,b,n):
    dist = (b-a)/n
    totalTrapezoidsArea = 0
    xi = a
    for i in range(0,n):
        totalTrapezoidsArea = totalTrapezoidsArea + (fn(xi)+fn(xi+dist))/2
        xi = xi + dist

    return totalTrapezoidsArea*(dist)

print("Trapezoids test!")
totalIntegration= trapezoids(quadratic , 0, 3, 1)
print("Trapezoids result 1 " , totalIntegration )
totalIntegration= trapezoids(quadratic , 0, 3, 2)
print("Trapezoids result 2" , totalIntegration )
totalIntegration= trapezoids(quadratic , 0, 3, 3)
print("Trapezoids result 3" , totalIntegration )
totalIntegration= trapezoids(quadratic , 0, 3, 4)
print("Trapezoids result 4" , totalIntegration )
totalIntegration= trapezoids(quadratic , 0, 3, 5)
print("Trapezoids result 5" , totalIntegration )
totalIntegration= trapezoids(quadratic , 0, 3, 100)
print("Trapezoids result 100" , totalIntegration )

