"""
"""
from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from smart_recruiting_server.conf.config_logger_setup import setup_config_logger
from smart_recruiting_server.utils.resource import Resource
from smart_recruiting_server.utils.auth import get_user
from smart_recruiting_server.service_api_handlers import post_answers_handler


class Answers(Resource):
    """ 
    This api logs user data
    """

    def post(self, role):
        data = request.get_json(force=True)
        app.logger.debug("Parameters:"+str(data)+"\nRole:"+str(role))
        return post_answers_handler.handle_request(data, role)

    post.authenticated = False
