http-terminal-notify
====================

A small Python-based HTTP frontend to terminal-notifier to allow you to push notifications to Mountain Lion's Notification Center with just a simple POST.

Requirements
------------

- OS X 10.8 or later

- [terminal-notifier](https://github.com/alloy/terminal-notifier)

Installation
------------

- Download terminal-notifier.app and place in `/Applications/`

- Run `python httpnotify.py` with optional parameter `--port` to change the port listened on.

How To Use
----------

Send a POST request to / with at minimum a `message` parameter:

<pre>curl -d "message=Hello%20World&title=My%20Title" localhost:8080</pre>

http-terminal-notify supports the `title`, `subtitle`, `group` and `url` parameters, and are unchanged in functionality. `activate` and `command` are disabled due to security concerns, but can be trivially added.

irssi Script
------------

An irssi script, `irssi_hilight_http.pl` is included, and will send an HTTP POST to a given URL when you receive a private message or are hilighted. Place the script in `~/.irssi/scripts/autorun` to run at startup. To load the script without restarting: 

<pre>/script load autorun/irssi_hilight_http.pl</pre>

To change the URL that irssi will send hilights to, set `hilight_http_url` and point it at the Python server running on your Mac:

<pre>/set hilight_http_url http://localhost:8080</pre>

To set a rate limit on outgoing notifications, set `hilight_http_cooldown` to the amount of time in seconds:

<pre>/set hilight_http_cooldown 30</pre>
