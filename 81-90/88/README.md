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

Since this is an open-ended assignment, I intend to run this idea.

I'll copy over the two projects and call them front-end and back-end.  At the completion, I think my code will only reside with front-end which means I'll display the UI from the Day62 exercise and rely on the database tech to serve up the date.  This means shifting from the csv-based data load to the DB only data load/store and more.

In principle, it should be a porting exercise.


# Running

```bash
flask --app main --debug run
```

I added a link to the display table to delete a cafe.  This is represented by the stylized ✘ character in red by using the CSS style `text-danger.`  The behavior is fairly straightforward - click on on the ✘ and the cafe is deleted.

At this time, we add a cafe by navigating to the /add URL.  I don't include a link from the main page for add because my goal at this time was to get something workign with the DB-based solution and not the UI.

# External Links

# requirements.txt

# TODOs

- Add a more proper ADD button or link to the main page.
- Stretch: add a logon screen and authenticate the user with permissons.
- Make the UI prettier.  Remember, this is a Proof-of-Concept.
