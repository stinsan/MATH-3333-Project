from LinAlg import *

# Let's begin!
print("Welcome!")
print("Please input three coordinates of form \"x y\" to make a triangle with those three coordinates as its vertices.")

# Input for the initial triangle
vertices = []
for i in range(3):
    print("Vertex", i + 1, ":")
    inp = input()
    coords = inp.split()
    x = float(coords[0])
    y = float(coords[1])
    vertices.append([x, y])

# Make the vertices list into a numpy array
vertices = np.array(vertices)

# Initial triangle
print("Here is your triangle, close the window to continue.")
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.title("Original Triangle")
pyplot.axis([0, 10, 0, 10])
triangle = pyplot.Polygon(vertices, color='red', fill=False)
pyplot.gca().add_patch(triangle)
pyplot.show()

# The transformation menu
print("Choose an option:")
inp = input("(T)ranslate, (S)cale, (R)otate, or (Q)uit?\n")

# Loop until user wants to quit
while True:

    # Translation
    if inp == "t" or inp == "T":
        # Take translation input
        inp = input("Translate in which direction? Please input in the form \"x y\".\n")
        trans = inp.split()
        trans = [float(trans[0]), float(trans[1])]

        # Print translated triangle
        pyplot.xlabel('x')
        pyplot.ylabel('y')
        pyplot.title("Translated Triangle")
        pyplot.axis([0, 10, 0, 10])
        t = pyplot.Polygon(vertices, color='red', fill=False, linestyle='dashed')
        pyplot.gca().add_patch(t)
        vertices = translate(vertices, trans)
        print("Here is your triangle, close the window to continue.")
        pyplot.show()

    # Scaling
    elif inp == "s" or inp == "S":
        # Take scale factor input
        inp = input("Scale by how much? Please input in the form \"x_scale y_scale\".\n")
        sf = inp.split()
        sf = [float(sf[0]), float(sf[1])]

        # Print scaled triangle
        pyplot.xlabel('x')
        pyplot.ylabel('y')
        pyplot.title("Scaled Triangle")
        pyplot.axis([0, 10, 0, 10])
        t = pyplot.Polygon(vertices, color='red', fill=False, linestyle='dashed')
        pyplot.gca().add_patch(t)
        vertices = scale(vertices, sf)
        print("Here is your triangle, close the window to continue.")
        pyplot.show()

    # Rotating
    elif inp == "r" or inp == "R":
        # Take axis of rotation and amount of rotation input
        inp = input("What are the coordinates for the axis of rotation? Please input in the form \"x y\".\n")
        theta = float(input("How many degrees would you like to rotate?\n"))
        pivot = inp.split()
        pivot = [float(pivot[0]), float(pivot[1])]

        # Output rotated triangle
        pyplot.xlabel('x')
        pyplot.ylabel('y')
        pyplot.title("Rotated Triangle")
        pyplot.axis([0, 10, 0, 10])
        t = pyplot.Polygon(vertices, color='red', fill=False, linestyle='dashed')
        pyplot.gca().add_patch(t)
        vertices = rotate(vertices, theta, pivot)
        print("Here is your triangle, close the window to continue.")
        pyplot.show()

    # Quit
    elif inp == "q" or inp == "Q":
        print("Goodbye!")
        exit(0)

    # Invalid input
    else:
        print("Not a valid input, try again.")

    # Restate prompt
    inp = input("(T)ranslate, (S)cale, (R)otate, or (Q)uit?\n")
