'''
'''

from flask import session


def handle_request(request):
    """
      This method is used to log out a ussr session
    """
    session['user_id'] = None
