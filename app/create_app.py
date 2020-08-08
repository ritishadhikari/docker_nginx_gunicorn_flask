from flask import Flask

def create_app():
    app=Flask(import_name=__name__)

    @app.route("/")
    def index():
        return "hello world"

    return app\
