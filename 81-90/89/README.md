# Overview

This is the day 89 assignment.

## _From the course:_
Build a todo list website.

Today, you are going to build a todo list website. This is a right of passage for any developer.

You can choose the type of todo list you want to build. It could be as simple as a website where you can list some items and cross them out. Or as complex as a Kanban-style task list like Trello.

Here is a website for inspiration:

https://flask.io/new

Top Secret: Most developer jobs will be interviewed by someone who is a manager. The top piece of technology a manager uses is a task-manager like Trello or Jira. If you can build a good task-manager, you will definitely impress your future interviewer!


## My comments:

Building a TODO list is something many people think about.  I use Microsoft's To-do because it is appoximately what I need to use. 

I'm expecting a few things to add to the TODO app.
- a landing page that shows my current list.
    - This page should allow for direct entry.  As simple as "start typing on this line."
- links on each to edit, mark complete, or delete.
- routes for `add` `edit` `delete` and `mark complete`.  These sound like the basic CRUD operations and their API-based methods.
- pretty screens to display
    - all open tasks
    - edit page
    - details of a single task
- a TODO item should contain the following information:
    - The title
    - The due date
    - The date entered
    - a Note field
    - a category

We can display a sortable list with this HTML:

```html
    <div class="container mt-5">
      <h2>Sortable List</h2>
      <ul id="sortable-list" class="list-group">
              <li class="list-group-item">item1</li>
              <li class="list-group-item">item2</li>
              <li class="list-group-item">item3</li>
      </ul>
    </div>
```
# Running

```bash
flask --app main --debug run
```

# External Links

# requirements.txt

# TODOs

There is a lot of stuff I can continue to do to make this application better.

- Allow the user to drag-and-drop the table entries to reorder.
- Enable the reorder buttons to swap items.
- Allow for an in-line add text box.  The idea is there is a text box always present, and I can add text and press return to add to my list.
- Maybe do away with the title & description, and only have the title.
- Add an "order" field to tell us the order of our list.  This has to scale, so I'm inclined to think we add all new items to the bottom of the list.
    - If we delete, we should probably re-order the remaining items.  This will require an iterator over the remaining items.  I don't know if I want to rely on a different type of sorting algorithm at this time.
    - The order is not the ID, or a key, but it should be unique.  

