# Overview

This is the day 94 assignment.

## _From the course:_
Write Python code to play the Google Dinosaur Game.

On Chrome, when you try to access a website and your internet is down, you see a little dinosaur. (Apparently because dinosaurs have short arms and they "can't reach" your website.

On this page, there is a hidden game, if you hit space bar you can play the T-rex run game.

Alternatively you can access the game directly here:
https://elgoog.im/t-rex/

You goal today is to write a Python script to automate the playing of this game. Your program will look at the pixels on the screen to determine when it needs to hit the space bar and play the game automatically.

You can see what it looks like when the game is automated with a bot:
https://elgoog.im/t-rex/?bot


You might want to look up these two packages:

https://pypi.org/project/Pillow/
https://pyautogui.readthedocs.io/en/latest/


## My comments:

This should be interesting!

# Running

Setup `.Xauthority` with some default information as [I found online](https://micwan88.github.io/linux/xauth/2019/10/16/create-xauthority-manually.html)

```bash
xauth add ${HOST}:0 . $(xxd -l 16 -p /dev/urandom)
xauth list
> potato/unix:0  MIT-MAGIC-COOKIE-1  00a877c5d47746e828bf73dc59cf7245
```

```
python3 main.py
```
![alt text](image.png)
![alt text](image.png)
![big cactus](cactus.png)
![small cactus](cactus-small.png)
![three cactii](cactus-three.png)
![two cactii](cactus-two.png)


# External Links

- [Pillow](https://pypi.org/project/pillow/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
- [Stack Overflow, debug - locateOnScreen](https://stackoverflow.com/questions/48709009/python-3-6-3-pyautogui-locateonscreen-not-working)

# requirements.txt

```
sudo apt install scrot
sudo apt install gnome-screenshot
pip install pyautogui
pip install pillow
```


# TODOs

- instead of cutting-and-pasting the full XPath, and then modifying the format, let's instead use a library to conver the XPath into a format that is convenient to use with Beautiful Soup.
