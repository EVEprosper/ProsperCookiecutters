"""exceptions.py: collection of app-specific exceptions"""
class {{cookiecutter.project_name}}Exception(Exception):
    """base exception for all project exceptions"""
    pass

class ResponseException({{cookiecutter.project_name}}Exception):
    """container for messaging HTTP errors"""
    def __init__(self, status=200, message=''):
        self.status = status
        self.message = message
        Exception.__init__(self)
