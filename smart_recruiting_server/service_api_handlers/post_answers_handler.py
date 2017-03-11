'''
'''

from flask import Flask, request, session
from flask import current_app as app
from flask.ext import restful

from django import db
from django.db import close_old_connections
from django.contrib.auth.models import User
from smart_recruiting_server.utils.auth import get_user
from smart_recruiting_db.recruiting_models.models import (JobSeeker, Recruiter)

def handle_request(data, role):
    """
      Log the user data
    """
    try:
	if str(role).lower() == 'recruiter':
		val = Recruiter.objects.create(details=data)
	else:
		val = JobSeeker.objects.create(details=data)
		val.save()
    except Exception as e:
        app.logger.debug(e)
        return {
            'success': False,
            'errorMessage': 'Internal Server Error',
            'errorCode': 500
            }
    finally:
        close_old_connections()
