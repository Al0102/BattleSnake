import os
import logging
import flask
from workers import WorkerEntrypoint, wsgi

import battle_handler as bs

def start_server(handlers: bs.BattleSnakeHandlers):
    app = flask.Flask("BattleSnakeTest")

    @app.get("/")
    def on_info():
        return handlers.info()

    @app.post("/start")
    def on_start():
        handlers.start(flask.request.get_json())
        return "ok"

    @app.post("/move")
    def on_move():
        return handlers.get_move(flask.request.get_json())

    @app.post("/end")
    def on_stop():
        handlers.stop(flask.request.get_json())
        return "ok"

    @app.after_request
    def identify_request(response):
        response.headers.set(
            "server", "battlesnake/test"
        )
        return response

    return app


