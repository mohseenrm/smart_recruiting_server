"""
Created on 11 March 2017
@author: surajshah
"""
import django
from os.path import dirname, abspath, join

from django.conf import settings
from django.db import close_old_connections
from flask import Flask
from flask.ext import restful
from smart_recruiting_db.settings.pool import init_pool
from flask.ext.restful import reqparse, abort, Api, Resource
from smart_recruiting_server.conf.config_logger_setup import setup_config_logger
from smart_recruiting_server.session.interfaces import DBInterface
from smart_recruiting_server.service_apis.uservalidation import UserValidation
from smart_recruiting_server.service_apis.usercreation import UserCreation
from smart_recruiting_server.service_apis.answers import Answers
from flask.ext.cors import CORS
 
close_old_connections()
django.setup()
init_pool()

app = Flask(__name__)
CORS(app)
app.auth_header_name = 'X-Authorization-Token'
app.session_interface = DBInterface()
app.root_dir = dirname(dirname(abspath(__file__)))
api = restful.Api(app)
setup_config_logger(app)

app.logger.info("Setting up Resources")

api.add_resource(UserCreation, '/userservice/create/')
api.add_resource(UserValidation,'/userservice/uservalidation/')
api.add_resource(Answers,'/questionnaire/<role>')

app.logger.info("Resource setup done")

if __name__ == '__main__':
    from gevent import monkey
    from smart_recruiting_server.utils.hacks import gevent_django_db_hack
    gevent_django_db_hack()
    monkey.patch_all(socket=True, dns=True, time=True, select=True,thread=False, os=True, ssl=True, httplib=False, aggressive=True)
    app.run(host="0.0.0.0",debug=True, port=7285)
