from http import HTTPStatus

from flask import Blueprint
from flask.views import MethodView

class ProxyPass(MethodView):
    def get(self) -> tuple:
        return 'GET_ok', HTTPStatus.OK

    def post(self) -> tuple:
        return 'POST_ok', HTTPStatus.OK

    def put(self) -> tuple:
        return 'PUT_ok', HTTPStatus.OK

    def delete(self) -> tuple:
        return 'DELETE_ok', HTTPStatus.OK


