import turtle #allows users to create pictures and shapes with a provided, virtual canvas.
import random # here it is used to randomize the initial direction of the ball when the game starts and when a player scores a point.
import time  #helps to work with time values,add time delays to the program,measure time intervals and many more -here for delay after "Game over"
import pygame #library for the development of multimedia applications like video games using Python:here for handling sound
#consists of computer graphics and sound libraries

# Initialize pygame and sound
pygame.init()

# Set up the screen
wn = turtle.Screen()
wn.title("PongPaddleClash")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Load MP3 sound files
paddle_sound = pygame.mixer.Sound("ballhit.mp3")  # load sound files class that represent sound object 
score_sound = pygame.mixer.Sound("score.wav")    
game_over_sound = pygame.mixer.Sound("gameover.mp3")  

# Function to reset the game
def reset_game():
    global score_a, score_b
    #re-set the scores of both players
    score_a = 0
    score_b = 0
    update_score()
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    ball.goto(0, 0)#set ball at center
    ball.dx = random.choice([0.25, -0.25])
    ball.dy = random.choice([0.25, -0.25])
    wn.update() #update the screen

# Score variables
score_a = 0
score_b = 0

# Paddle A (Player)
           #library.object
paddle_a = turtle.Turtle()
paddle_a.speed(2)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()

'''penup() method is used to lift the pen (or turtle's tail) from the drawing surface. When the pen is "up," the turtle will 
not leave a trace when it moves. 
This is particularly useful when you want to reposition the turtle without drawing a line.
'''
paddle_a.goto(-350, 0)

# Paddle B (AI player)
paddle_b = turtle.Turtle()
paddle_b.speed(2)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()

paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(20)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = random.choice([0.25, -0.25])
ball.dy = random.choice([0.25, -0.25])

# AI Paddle speed
ai_paddle_speed = 0.25  

# Function to move Paddle A up
def paddle_a_up():
    y = paddle_a.ycor()#inbuilt method to get y coordinate 
    y += 20
    if y < 290:  # Restrict the top border
        paddle_a.sety(y)

# Function to move Paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y > -290:  
        paddle_a.sety(y)

def computer_player():
    if ball.dx < 0:
        # Ball is moving away from the computer, AI stays idle
        return

    # Calculate the AI paddle's target position
    impact_distance = 800 - ball.xcor()  # As total width of the screen is 800
    #impact_distance :represents the distance from the ball's current x-coordinate to the right edge of the screen
    impact_time = impact_distance / (ball.dx * ai_paddle_speed * 1000) #time=distance/speed
    #ball.dx:x component of ball's velocity
    #1000:scaling factor to adjust in the frame
    target_y = ball.ycor() + (ball.dy * ai_paddle_speed * 1000) * impact_time

 #If the AI paddle is already close enough to the estimated impact point, it doesn't need to move, and the function returns early.

    if abs(target_y - paddle_b.ycor()) < 10:
        # AI doesn't need to move
        return

    if target_y < paddle_b.ycor():
        # Move the AI paddle up if the ball is going above the paddle
        new_y = paddle_b.ycor() - ai_paddle_speed
    else:
        # Move the AI paddle down if the ball is going below the paddle
        new_y = paddle_b.ycor() + ai_paddle_speed

    # Update the AI paddle's position
    if -290 < new_y < 290:
        paddle_b.sety(new_y)

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle() #hide turtle cursor
score_display.goto(0, 260)
score_display.write("Player A: 0  AI Player: 0", align="center", font=("Courier", 24, "normal"))

# Function to update the score display
def update_score():
    score_display.clear()
    score_display.write(f"Player A: {score_a}  AI Player: {score_b}", align="center", font=("Courier", 24, "normal"))

# Function to display game over message
def game_over(winner):
    game_over_display = turtle.Turtle()
    game_over_display.speed(0)
    game_over_display.color("white")
    game_over_display.penup()
    game_over_display.hideturtle()
    game_over_display.goto(0, 0)
    game_over_display.write(f"Game Over\n{winner} wins!", align="center", font=("Courier", 36, "normal"))
    wn.update()
    game_over_sound.play()  # Play the game over sound
    time.sleep(2)  # Pause for 2 seconds
    game_over_display.clear()  # Clear the "game over" message

    # Ask the user if they want to play again
    play_again = wn.textinput("Play Again", "Do you want to play again? (yes or no)")

    if play_again and play_again.lower() == "yes":
        # Reset the game and scores
        reset_game()

    # If the user chooses not to play again or closes the input dialog, exit the game
    else:
        wn.bye()

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "Up")
wn.onkeypress(paddle_a_down, "Down")

# Function to start the game when the screen is clicked
def start_game(x, y):
    global game_started
    if not game_started:
        game_started = True
        start_button.clear()  # Clear the "Start Game" button
        reset_game()  # Start the game
        wn.update()

# Flag to track if the game has started
game_started = False

# Create a "Start Game" button on the screen
start_button = turtle.Turtle()
start_button.speed(0)
start_button.color("white")
start_button.penup()
start_button.hideturtle()
start_button.goto(0, 0)
start_button.write("Engage the bounce! Click for Pong fun.", align="center", font=("Courier", 20, "normal"))

# Listen for clicks on the screen and start the game when clicked
turtle.onscreenclick(start_game)

# Main Game Loop
while True:
    wn.update()

    if game_started:
        # Your game logic goes here
        wn.update()

        # Call the computer player function
#The reason for calling computer_player() first is to allow the AI paddle to react to the ball's movement 
# in the current frame before the ball moves to its next position.
        computer_player()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking for the ball
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
#ball may cross AI players border here
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx = random.choice([0.25, -0.25])  # Randomly choose a new direction for x
            ball.dy = random.choice([0.25, -0.25])  # Randomly choose a new direction for y
            # Player A scores a point
            score_a += 1
            update_score()
            if score_a >= 5:
                game_over("Player A")
            else:
                score_sound.play()  # Play the score sound effect

        elif ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx = random.choice([0.25, -0.25]) 
            ball.dy = random.choice([0.25, -0.25])  
            # AI Player scores a point
            score_b += 1
            update_score()
            if score_b >= 5:
                game_over("AI Player")
            else:
                score_sound.play()  # Play the score sound effect

        # Paddle and ball collisions
        if (ball.dx > 0) and (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
            #checks if ball moving in positive ,checks if ball is closer to paddle ,
            ball.color("blue")
            ball.setx(340)
            ball.dx *= -1  # Reverse the ball's direction
            paddle_sound.play()  # Play the paddle collision sound

        elif (ball.dx < 0) and (-350 > ball.xcor() > -360) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
            ball.color("red")
            ball.setx(-340)
            ball.dx *= -1  # Reverse the ball's direction
            paddle_sound.play()  # Play the paddle collision sound
