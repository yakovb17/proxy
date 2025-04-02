import os

from flask import Flask

from proxy.apis.health_check import health_check_bp
from proxy.apis.proxy import ProxyPass


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    register_apis(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

def register_apis(app: Flask) -> None:
    app.add_url_rule('/', view_func=ProxyPass.as_view('proxy_pass_view'))
    app.register_blueprint(health_check_bp)