#!/usr/bin/env python

from flask import Flask, views
import statsd
import stat_server

def main():
    app = Flask(__name__)

    @app.route("/page/<id>")
    def display_message(id):
        stat_server.users_stat()
        return "Page ID is {} !".format(id)

    app.run(debug=True)

if __name__ == "__main__":
    main()
