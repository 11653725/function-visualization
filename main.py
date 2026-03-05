import os
import sys
import numpy as np
import matplotlib.pyplot as plt

from functions import lin, quad, sin, cos, exp


if not os.path.exists("images"):
    os.makedirs("images")


# gen
x = np.linspace(-10, 10, 1000)



if len(sys.argv) > 1:

    name = sys.argv[1]

    if name == "linear":
        y = lin(x, 2, 1)
        title = "Linear Function"
        filename = "images/linear.png"

    elif name == "quadratic":
        y = quad(x, 1, -2, 1)
        title = "Quadratic Function"
        filename = "images/quadratic.png"

    elif name == "sin":
        y = sin(x)
        title = "Sine Function"
        filename = "images/sine.png"

    elif name == "cos":
        y = cos(x)
        title = "Cosine Function"
        filename = "images/cosine.png"

    elif name == "exp":
        y = exp(x)
        title = "Exponential Function"
        filename = "images/exponential.png"

    else:
        print("Use: linear, quadratic, sin, cos, exp")
        exit()

    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()

    plt.savefig(filename)
    plt.close()

    print("Graph saved:", filename)

else:

    # linear
    y = lin(x, 1.5, -2)
    plt.plot(x, y)
    plt.title("Linear Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.savefig("images/linear.png")
    plt.close()


    # quadratic
    y = quad(x, 0.4, -1, 1)
    plt.plot(x, y)
    plt.title("Quadratic Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.savefig("images/quadratic.png")
    plt.close()


    # sine
    y = sin(x)
    plt.plot(x, y)
    plt.title("Sine Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.savefig("images/sine.png")
    plt.close()


    # cosine
    y = cos(x)
    plt.plot(x, y)
    plt.title("Cosine Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.savefig("images/cosine.png")
    plt.close()


    # exponential
    y = exp(0.3 * x)
    plt.plot(x, y)
    plt.title("Exponential Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.savefig("images/exponential.png")
    plt.close()


    # combined
    y1 = lin(x, 1, 0)
    y2 = quad(x, 0.2, 0, -2)
    y3 = sin(x)

    plt.plot(x, y1, label="linear")
    plt.plot(x, y2, label="quadratic")
    plt.plot(x, y3, label="sin")

    plt.title("Multiple Functions")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()

    plt.savefig("images/multiple_functions.png")
    plt.close()

    print("All graphs saved in images folder")