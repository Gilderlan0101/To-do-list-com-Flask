from flask import Flask

def creat_app():
    app = Flask(__name__)
    app.secret_key = '2345tgfdd456ythgvc7__'
    from src.route.routes import home
    app.register_blueprint(home)

    return app