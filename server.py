
import os
import logging
import flask
import handlers as bs

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
        handlers.stop()
        return "ok"

    @app.after_request
    def identify_request(response):
        response.headers.set(
            "server", "battlesnake/test"
        )
        return response

    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "8000"))

    logging.getLogger("werkzeug").setLevel(logging.ERROR)

    print(f"\nRunning Battlesnake at http://{host}:{port}")
    app.run(host=host, port=port)




