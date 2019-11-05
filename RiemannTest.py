#riemann rest for integration

def linear(x):
    return x

def quadratic(x):
    return x*x


def riemannIntegration(fn,a,b,n):

    integrationTotal = 0
    base = (b-a)/n
    halfBase = base/2
    for i in range(0,n):
        integrationTotal = integrationTotal + fn(i*base+halfBase)
    return (integrationTotal*base)


print("Riemann test!")
totalIntegration= riemannIntegration(quadratic , 0, 3, 1)
print("Riemann result 1 " , totalIntegration )
totalIntegration= riemannIntegration(quadratic , 0, 3, 2)
print("Riemann result 2" , totalIntegration )
totalIntegration= riemannIntegration(quadratic , 0, 3, 3)
print("Riemann result 3" , totalIntegration )
totalIntegration= riemannIntegration(quadratic , 0, 3, 4)
print("Riemann result 4" , totalIntegration )
totalIntegration= riemannIntegration(quadratic , 0, 3, 5)
print("Riemann result 5" , totalIntegration )
totalIntegration= riemannIntegration(quadratic , 0, 3, 100)
print("Riemann result 100" , totalIntegration )











