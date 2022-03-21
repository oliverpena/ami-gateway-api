import json
import logging

from flask_restx import Namespace, Resource
from werkzeug.exceptions import BadRequest, Unauthorized

from models.health import response_exception_model
from utils.jwt_utils import jwt_required

health_name_space = Namespace('health', description='To check service health')

api = health_name_space
api.models[response_exception_model.name] = response_exception_model

logger = logging.getLogger(__name__)


@api.doc(security='apikey')
@api.route('/status')
class Status(Resource):
    @api.response(code=200, description='OK')
    @api.response(code=400, model=response_exception_model,
                  description='Bad Request')
    @api.response(code=401, model=response_exception_model,
                  description='Unautorized')
    @jwt_required
    def get(self):
        try:
            return '200 OK', 200
        except (Unauthorized, BadRequest) as e:
            api.abort(e.code, e.__doc__, errors={
                      'Exception': json.loads(str(e))["message"]})
