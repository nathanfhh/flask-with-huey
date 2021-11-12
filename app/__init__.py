from flask import Flask


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.API import core_api
    app.register_blueprint(core_api)
    app.app_context().push()
    return app
