"""
"""
from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from django.db import close_old_connections
from smart_recruiting_server.service_api_handlers import \
    post_user_validation_handler, delete_user_validation_handler
from smart_recruiting_server.utils.resource import Resource
from smart_recruiting_server.utils.auth import get_user


class UserValidation(Resource):
    """ 
    This class validates the user and returns back an authentication token
    """

    def post(self):
        """
            This method authenticates the user
        """    
        remember_me = 0
        try:
            remember_me = request.json['remember_me']
        except Exception as e:
            app.logger.debug(e)
            app.logger.debug('Remember me not sent')

        app.logger.debug("Email ID:"+str(request.json['email']) + " Password:"+ str(request.json['pswd'])+ 
                                     " remember_me: " +str(remember_me))

        return post_user_validation_handler.handle_request(str(request.json['email']), str(request.json['pswd']),
                                            str(remember_me))        
        close_old_connections()

    post.authenticated = False


    def delete(self):
        """
        This method deletes the authentication session
        """
        try:
            logged_in_user = get_user()
            app.logger.info("Logout called for the user %s",
                            logged_in_user.email)
        except:
            app.logger.info("Logout called for an invalid session %s",
                            request.remote_addr)
            return {
                'success': False,
                'errorMessage': 'Logout for invalid session called',
                'errorCode': 422 
            }

        delete_user_validation_handler.handle_request(request)
        return {
            'success': True,
            'responseData': {
                'is_deleted': True
            }
        }
