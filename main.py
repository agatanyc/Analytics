#!/usr/bin/env python

from flask import Flask, views
import statsd
import c

def main():
    app = Flask("__name__")

    @app.route("/page/<id>")
    def display_message(id):
        c.users_stat()
        return "Page ID is " + str(id) + "!"

    app.debug = True
    app.run()

if __name__ == '__main__':
    main()
