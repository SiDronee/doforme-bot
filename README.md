DoForMe
=======

A Telegram bot for assigning tasks to other people.
It helps you keeping track of your own tasks as well as tasks that you assigned others.

Just add it to a group and follow the instructions.

:construction: Under construction!


Features
--------

* Create tasks including due date and assignee
* Mark tasks as complete
* Edit due date of tasks
* Daily reminder of your open tasks
* Weekly review


Install
-------

* Python 3.6
* pip install -r requirements.txt
* Register the bot with privacy status 'disabled'


Run
---

### Console

Run python main.py -t [your telegram token] -a [admin id]

### Web app

A Flask web app of the bot is available in app.py. It requires the following environment variables to be set:
* DFM_WEB_IP: the web server ip, e.g. 0.0.0.0
* DFM_WEB_PORT: the web server port, e.g. 8080
* DFM_WEB_DNS: the public domain name of the bot
* DFM_BOT_TOKEN: the Telegram bot token
* DFM_REQUEST_SECRET: a secret to slightly protect requests to the web app
* DFM_ADMIN_ID: the Telegram user id of the admin

### Database

To use a MySQL database instead the default SQLite (data/database.sqlite) database, set the following environment variables:
* DFM_DB_HOST
* DFM_DB_PORT
* DFM_DB_USERNAME
* DFM_DB_PASSWORD
* DFM_DB_DATABASE


Usage
-----

The admin id is a Telegram user id and allows the specified user to perform following commands:

* admin-stats: Shows basic stats of the data in the database.
* admin-announce ([text]): Sends [text] to all users.
* admin-feedback-show: Lists unresolved (not done) feedback entries.
* admin-feedback-reply ([id] [text]): Sends [text] to the user that issued feedback [id].
* admin-feedback-close ([id]): Marks feedback [id] as done.


Libraries
---------

* https://github.com/grcanosa/telegram-calendar-keyboard
