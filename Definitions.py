# Jumping hurdles with equal height and equal distance:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    hurdle()

