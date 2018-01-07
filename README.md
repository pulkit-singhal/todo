todo
=======

[![AUR](https://img.shields.io/aur/license/yaourt.svg)]()
[![PYT](https://img.shields.io/badge/Python-%3E%3D%203.0-brightgreen.svg)]()
[![SDP](https://img.shields.io/badge/Side%20Project-True-yellow.svg)]()

`todo` is a minimalist and simple command line task manager. It aims for those who want to *finish* their tasks, not to organize them.

It is written in `Python 3` and uses `sqlite3` to store your tasks.

Why todo?
------

There are various command-line task managers are out there but the there are various reasons to use `todo`

* Simple things are easily manageable, being not a feature-packed is one of its pros
* If you are taking 15 minutes to tag or organize your todo-list, better option is to finish off some tasks in those 15 minutes

`todo` was inspired by [t][].

[t]: https://github.com/sjl/t


Installing todo
------------

`todo` requires [Python][] 3 or newer, and some form of UNIX-like shell (bash
works well).  It works on Linux, OS X, and Windows (with [Cygwin][]).

[Python]: http://python.org/
[Cygwin]: http://www.cygwin.com/

Installing and setting up `todo` will not take more than a minute.

First, [download][] the newest version or clone the git repository
(`git clone https://github.com/pulkit-singhal/todo.git`).  Put it anywhere you like.

[download]: https://github.com/pulkit-singhal/todo/archive/master.zip

Next, decide where you want to keep your todo list. I put mine in `~/tasks.todo`.

Finally, set up an alias to run `todo`.  Put something like this in your
`~/.bashrc` file:

    alias todo='python ~/path/to/todo.py --location ~/tasks.todo'
    
If you have both Python 2 and 3 installed you need to explicitly use Python 3

	alias todo='python3 ~/path/to/todo.py --location ~/tasks.todo'

Make sure you run `source ~/.bashrc` or restart your terminal window to make
the alias take effect.

Using todo
-------

`todo` is quick and easy to use.

### Add a Task

To add a task, use `todo [task description]`:
    
    $ todo Clean the room.
    $ todo Buy more milk.
    $ todo Plan the travel to Shimla.
    $

### List Your Tasks

Listing your tasks is even easier -- just use `todo`:

    $ todo
    +----+----------------------------+
	| ID |            Task            |
	+----+----------------------------+
	| 1  |      Clean the room.       |
	| 2  |       Buy more milk.       |
	| 3  | Plan the travel to Shimla. |
	+----+----------------------------+
    $

`todo` will list all of your unfinished tasks and their IDs.

### Finish a Task

After you're done with something, use `todo -f ID` to finish it:

    $ todo -f 2
    $ todo
    +----+----------------------------+
	| ID |            Task            |
	+----+----------------------------+
	| 1  |      Clean the room.       |
	| 3  | Plan the travel to Shimla. |
	+----+----------------------------+
    $
   
You can finish off multiple tasks at once, by providing the list of ID like, `todo -f 1 3` will remove task with ID 1 and 3.

### Edit a Task

Sometimes you might want to change the wording of a task.  You can use
`todo -e ID [new description]` to do that:

    $ todo -e 3 Plan the travel to Manali.
    $ todo
    +----+----------------------------+
	| ID |            Task            |
	+----+----------------------------+
	| 1  |      Clean the room.       |
	| 3  | Plan the travel to Manali. |
	+----+----------------------------+
    $

### Multiple Lists

`todo` is for people that want to *do* tasks, not organize them. With that said,
sometimes it's useful to be able to have at least *one* level of organization.
To split up your tasks into different lists you can add a few more aliases:

    alias tg='python ~/path/to/todo.py --location ~/groceries.todo'
    alias tw='python ~/path/to/todo.py --location ~/work.todo'

### Distributed Bugtracking

Like the idea of distributed bug trackers, but don't want to use such a heavyweight system?  You can use `todo` instead.

Add another alias to your `~/.bashrc` file:

    alias bugs='python ~/path/to/todo.py --location ~/bugs.file'

Now when you're in your project directory you can use `bugs` to manage the list of
bugs/tasks for that project.