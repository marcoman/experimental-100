# Overview

This is the day 90 assignment.

## _From the course:_
An online writing app where if you stop typing, your work will disappear.

For most writers, a big problem is writing block. Where you can't think of what to write and you can't write anything.

One of the most interesting solutions to this is a web app called The Most Dangerous Writing App, an online text editor where if you stop writing, all your progress will be lost.

A timer will count down and when the website detects the user has not written anything in the last 5/10 seconds, it will delete all the text they've written so far.

Try it out here:

https://www.squibler.io/dangerous-writing-prompt-app

You are going to build a desktop app that has similar functionality. The design is up to you, but it should allow a user to type and if they stop for more than 5 seconds, it should delete everything they've written so far.

## My comments:

So, this looks like it should be fairly easy to write.  

This was a simple application.  A large text box with a javascript script watching events and resetting the timer.  Also, a second javascript script counting down the time.


# Running

```bash
flask --app main --debug run
```

# External Links

# requirements.txt

# TODOs

