# Overview

This is the day 88 assignment.

## _From the course:_

Build a website that lists cafes with wifi and power for remote working.

On day 66, we create an API that serves data on cafes with wifi and good coffee. Today, you're going to use the data from that project to build a fully-fledged website to display the information.

Included in this assignment is an SQLite database called cafes.db that lists all the cafe data.

Using this database and what you learnt about REST APIs and web development, create a website that uses this data. It should display the cafes, but it could also allow people to add new cafes or delete cafes.

For example, this startup in London has a website that does exactly this:

https://laptopfriendly.co/london



## My comments:

I can re-use the webiste from a previous assignmets:

- Day 62 to setup the web page
- Day 66 where we built a restful API to get details from our local data store, which was a sqlite db.

- Start by writing an app that displays a page.
- Add pages to view a cafe, edit a cafe.

Since this is an open-ended assignment, I intend to run this with two components.
1. I'll start the API service on its own port and it will generally run as-is.  This is Day 66.
2. I'll modify the Day62 code to use the API to get the data and display it onscreen.  This means that instead of using SQLite calls in Day62, I'll rely on API calls to the REST interface.

This means starting by copying over day 62 results to my Day 88 folder.  I'll runn that service on port 5001.

# Running

```bash
flask --app main --debug run
```


I have Postman installed as a VS Code extension, with a preference toward running in Ubuntu.

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