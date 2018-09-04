import logging

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from social_community.constants import ResponseConstants, PostTypeList
from social_community.decorator import logged_in
from social_community.log_message import Warn, Error
from social_community.response import SuccessResponse, ServerErrorResponse
from social_community.util import to_dict

logger = logging.getLogger(__name__)


@api_view(["GET"])
@authentication_classes((TokenAuthentication, SessionAuthentication,))
@permission_classes((IsAuthenticated,))
@logged_in
def get_feed(request):
    return Response({"msg": "OK", "Success": "True"})


class FeedViewSet(viewsets.ViewSet):
    #  publish a new post
    @authentication_classes((TokenAuthentication, SessionAuthentication,))
    @permission_classes((IsAuthenticated,))
    @logged_in
    def create(self, request):
        try:
            data = request.data
            uid = request.query_params["uid"]
            post_type = int(data.get("type", 0))
            if not post_type or post_type not in PostTypeList:
                logger.warn(Warn.INVALID_POST_TYPE + str(uid) + "," + str(post_type))
                response = SuccessResponse(msg=ResponseConstants.INVALID_POST_TYPE + str(PostTypeList))
                return Response(to_dict(response), status=status.HTTP_400_BAD_REQUEST)
            response = SuccessResponse()
            return Response(to_dict(response))
        except Exception as e:
            logger.error(Error.PUBLISH_POST_ERROR + str(e))
            response = ServerErrorResponse()
            return Response(to_dict(response), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # get all post
    def list(self, request):
        return Response({"msg": "GET list"})

    # get Single post
    def retrieve(self, request, pk=None):
        return Response({"msg": "GET Single"})

    # PUT full update (post edit)
    @authentication_classes((TokenAuthentication, SessionAuthentication,))
    @permission_classes((IsAuthenticated,))
    @logged_in
    def update(self, request, pk=None):
        return Response({"msg": "Update Post"})

    # PATCH partial Update (like/comment/share)
    @authentication_classes((TokenAuthentication, SessionAuthentication,))
    @logged_in
    def partial_update(self, request, pk=None):
        return Response({"msg": "partial update Post"})

    # delete a post (mark as deleted)
    @authentication_classes((TokenAuthentication, SessionAuthentication,))
    @permission_classes((IsAuthenticated,))
    @logged_in
    def destroy(self, request, pk=None):
        return Response({"msg": "Post deleted"})
