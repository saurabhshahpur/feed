from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import authentication_classes, api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['POST'])
# @authentication_classes((TokenAuthentication, SessionAuthentication,))
# @permission_classes((IsAuthenticated,))
def home(request):
    """
    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """
    if "test" in request.data:
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
    resp = {"test": "fun"}

    return Response(resp, status=status.HTTP_200_OK)
