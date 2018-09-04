import logging
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from feed.models import UserDetail
from social_community.log_message import Warn, Error

logger = logging.getLogger(__name__)


# function to check if users is logged in and not a guest users
def logged_in(function):
    def wrap(request, *args, **kwargs):
        try:
            request_obj = request
            if not isinstance(request, Request):
                request_obj = args[0]
            user = UserDetail.objects.get(user=request_obj.user)
            if user.is_guest or not user.logged_in:
                logger.warning(Warn.GUEST_OR_LOGOUT_USER + str(user.id))
                return Response({"msg": "user don't have permission, please SignIn", "success": True},
                                status=status.HTTP_403_FORBIDDEN)
            request_obj.GET._mutable = True
            request_obj.GET["uid"] = user.id
            # due to two binding it also change in request/args variable
            return function(request, *args, **kwargs)
        except Exception as e:
            logger.error(Error.LOGIN_CHECK_FAILED + str(e))
            return Response({"msg": "SERVER ERROR", "success": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
