#!/usr/bin/env python

from flask import Flask, views
import statsd
import stat_server

def log_status_code(res):
    stat_server.status_stat(res.status_code)
    return res

def main():
    app = Flask(__name__)

    @app.route("/page/<id>")
    def display_message(id):
        stat_server.users_stat()
        return "Page ID is {} !".format(id)

    app.after_request(log_status_code) # the parameter function will run
    app.run(debug=True)                # after each request

if __name__ == "__main__":
    main()
