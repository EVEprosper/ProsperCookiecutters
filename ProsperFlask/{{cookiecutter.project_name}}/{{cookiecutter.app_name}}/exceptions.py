"""exceptions.py: collection of exceptions for {{cookiecutter.app_name}}"""
class ResponseException(Exception):
    """base class for wrapping HTTP errors going out for responses"""
    def __init__(self, status=200, message=''):
        self.status = status
        self.message = message
        Exception.__init__(self)
class HelloWorldEndpointFailure(ResponseException):
    """demo custom exception - cookiecutter"""
    pass

## {{cookiecutter.endpoint_group}}_utils exceptions ##
class {{cookiecutter.endpoint_group}}Exception(Exception):
    """base class for {{cookiecutter.endpoint_group}} exceptions"""
    pass

