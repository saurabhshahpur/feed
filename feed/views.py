from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from wheel.util import to_json


@api_view(['GET'])
# @authentication_classes((TokenAuthentication, SessionAuthentication,))
# @permission_classes((IsAuthenticated,))
def home(request):
    resp = {"test": "fun"}

    return Response(resp, status=status.HTTP_200_OK)
