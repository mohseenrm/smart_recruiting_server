"""
"""
from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from smart_recruiting_server.conf.config_logger_setup import setup_config_logger
from smart_recruiting_server.service_api_handlers import \
     post_user_creation_handler
from smart_recruiting_server.utils.resource import Resource
from smart_recruiting_server.utils.auth import get_user
from smart_recruiting_server.service_api_handlers import get_questionnaires_handler

class Questionnaires(Resource):
    """ 
    This api returns all available questionnaires
    """

    def get(self):
        """
            This method returns all available active questionnaires
        """
        app.logger.debug("Call to get all active questionnaires")

        return get_questionnaires_handler.handle_request()

