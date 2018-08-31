import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.utils import json

from feed.models import UserDetail
from feed.serializers import UserSerializer

logger = logging.getLogger(__name__)


# class Users(viewsets.ViewSet):
#     @action(methods=['POST'], detail=False, permission_classes=[], authentication_classes=[])
#     def signup(self, request):
#         try:
#             logger.info("signup started." + str(json.dumps(request.data)), exc_info=True)
#
#         except Exception as ex:
#             logger.error("exception occurred in hog_startup " + str(ex), exc_info=True)
#             return Response({"msg": "Exception Occurred in hog_startup: " + str(ex)},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserViewSet(viewsets.ViewSet):
    """
    Users viewset
    """

    @authentication_classes((TokenAuthentication,))
    @permission_classes((IsAuthenticated, IsAdminUser))
    def list(self, request):
        queryset = UserDetail.objects.all()
        serializer_class = UserSerializer
        return Response({"Success": True, "msg": "Ok"})

    """
    Create New user
    """

    def create(self, request):
        user_name = request.data["user_name"]
        password = request.data["password"]
        auth_user = User.objects.create(username=user_name, password=password, email=user_name, is_staff=True)
        UserDetail.objects.create(user=auth_user)
        token = Token.objects.get_or_create(user=auth_user)
        token_data = str(token[0].key)
        return Response({"success": "True", "msg": "user created", "token":token_data})

    def retrieve(self, request, pk=None):
        return Response({"Success": True, "msg": "Ok"})
        # pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
