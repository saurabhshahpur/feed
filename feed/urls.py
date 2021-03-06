"""feed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


from feed.views import home
from social_community.views import FeedViewSet
from users.views import UserViewSet
router = routers.SimpleRouter()

API_TITLE = 'Feed API'
API_DESCRIPTION = 'A Web API.'
schema_view = get_swagger_view(title=API_TITLE)
router.register(r'users', UserViewSet, base_name='users')
router.register(r'feed', FeedViewSet, base_name='')


urlpatterns = [
    url(r'^swagger$', schema_view),
    # url(r'^users', ),
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^home', home)

]
