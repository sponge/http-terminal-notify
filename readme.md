http-terminal-notify
====================

A small Python-based HTTP frontend to terminal-notifier to allow you to push notifications to Mountain Lion's Notification Center with just a simple POST.

How To Use
----------

Send a POST request to / with at minimum a "message" parameter:

curl -d "message=Hello%20World&title=My%20Title" localhost:8080

http-terminal-notify supports the "title", "subtitle", "group" and "url" parameters of alloy/terminal-notifier