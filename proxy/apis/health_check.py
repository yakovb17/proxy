from http import HTTPStatus

from flask import Blueprint

health_check_bp: Blueprint = Blueprint('health_check', __name__, url_prefix='/api/health_check')

@health_check_bp.get('/')
def health_check() -> tuple:
    return {'status': 'OK'}, HTTPStatus.OK