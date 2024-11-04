from flask import Flask


def create_app():  # Corrigido para create_app
    app = Flask(__name__)
    app.secret_key = '2345tgfdd456ythgvc7__'
    from src.route.routes import home





    app.register_blueprint(home)

    return app
