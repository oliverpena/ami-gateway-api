from typing import Dict

from flask import Blueprint, Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from core.config import app_config
from core.container import Container
from name_spaces.health import health_name_space


def create_app(environment: str) -> Flask:
    config_obj = app_config[environment]
    container = Container()
    container.config.from_dict(config_obj.config)

    app = Flask(config_obj.FLASK_APP_NAME)
    blueprint = Blueprint(app.name, __name__, url_prefix=f'/{app.name}')
    api = Api(blueprint, version='1.0', title='AMI RESTful API',
              description='REST API to handle AMI Commands.',
              contact='Oliver Peña',
              contact_email='oliverpena.itt@gmail.com',
              authorizations=authorisations(),
              security='apikey')
    api.add_namespace(health_name_space, path='/health')
    app.register_blueprint(blueprint)
    app.container = container
    app.config.from_object(config_obj)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    return app


def authorisations() -> Dict:
    return {'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY',
        'description': "Type in the *'Value'* in the input box blow: **' The API Key Provided by the API Author '**"  # noqa

    }}
