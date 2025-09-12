def newton(a, x0, tol=10**-8): # define a new function
    """Newton's method for finding square roots."""
    x = x0 # initial value
    while True: # forever
        print(x)
        y = (x + a/x) / 2 # update y
        if abs(x - y) < tol: # x and y arbitrarily close
            break # exit the infinite loop
        x = y # update x
    return x
if __name__ == "__main__":
    newton(64, 5)