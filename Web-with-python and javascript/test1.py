import random
import curses

# Set up the window
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initial snake position and food
snake_x = sw//4
snake_y = sh//2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI)

# Initial direction
key = curses.KEY_RIGHT

# Game logic
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Determine new head position
    new_head = [snake[0][0], snake[0][1]]

    # Check which direction to move the snake
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert new head and update snake
    snake.insert(0, new_head)

    # Check if snake has hit the wall or itself
    if (snake[0][0] in [0, sh]) or (snake[0][1] in [0, sw]) or (snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Check if snake has eaten the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Display updated snake
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
