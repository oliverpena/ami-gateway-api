from flask_restx import Model, fields

response_exception_model = Model('Response Exception Model', {  # noqa
    'errors': fields.Raw(required=False, description='Exception errors'),
    'message': fields.String(required=False, description='Exception message')
})
