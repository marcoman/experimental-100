# Overview

This is the day 87 assignment.

## _From the course:_

Using Python Turtle, build a clone of the 80s hit game Breakout.

## My comments:

I used Day 22 as a reference.  Day22 was a pong game, and the mechanics of the ball and paddle bounces were re-usable.  I made some improvements for a grid, specifically how balls bounce from a brick.

I see I still have the paddle bounce problem where a ball may bounce more than once because the logic is about proximity, and not the actual detection of colors touching.  This means that when a ball is close to a paddle, it will continue to bouce as long as that paddle is close to the ball.  Not optimal, but it works for now.

I keep a score, and a high score.  I don't persist the information.  That would be a TODO.


# Running

```bash
python3 day87.py
```



# External Links

# requirements.txt


# Final Solution

# TODOs

- Persist the high score.
- Add a "number of lives" count.
- Enhance the gameplay to let two players play.
- Enhance the gameplay to let people type in, 'r' to restart.
- Enhance the gameplay to let people type in, 'q' to quit.
- position the screen where I want it, rather than have it show up at a random screen location.