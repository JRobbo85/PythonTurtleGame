import turtle 
import time
import random



WIDTH, HEIGHT = 800, 800
COLORS = ['red', 'green', 'blue', 'purple', 'black', "orange", "yellow", "brown", "pink", "cyan"]

def numberofracers():                                                                                   # Defining number of racers
    racers = 0                                                                                          # Setting initial number of racers
    while True:                                                                                         # while racers = 0 repeat
        racers = input("Input number of racers (2-10): ")                                               # ask user to input number of racers
        if racers.isdigit():                                                                            # Checks if input is a number
            racers = int(racers)                                                                        # IF it is, feed the number to the racers variable
        else:
            print ("Input is not a number, please try again.")                                          # Otherwise, ask for user to try again
            continue

        if 2 <= racers <=10:                                                                            # If number is within range, return the number
            return racers
        else:
            print ("Number not in range 2-10, please try again.")                                       # If not, ask again

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]
    


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.pencolor("black")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racer!!!!")

racers = numberofracers()
init_turtle()
turtle.Screen().bgcolor("lightgray")
random.shuffle(COLORS)
colors = COLORS[:racers]                                                                                # Slices the list of colours using the number of racers selected

winner = race(colors)
turtle.write(f"{winner} WINS!")
print(winner)
time.sleep(5)
turtle.exitonclick()