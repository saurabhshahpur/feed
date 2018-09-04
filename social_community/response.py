from social_community.constants import ResponseConstants


class SuccessResponse(object):
    def __init__(self, results=None, msg=None):
        self.results = results
        self.msg = msg
        self.success = True


class ServerErrorResponse(object):
    def __init__(self, msg=ResponseConstants.SERVER_ERROR_5XX):
        self.results = None
        self.msg = msg
        self.success = False
