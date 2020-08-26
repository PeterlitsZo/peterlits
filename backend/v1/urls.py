from django.conf.urls import url, include
from django.conf import settings

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

# if settings.DEBUG:
#     # if DEBUG, then we can use /v1/test for test
#     urlpatterns.append(url(r'^test', include('rest_framework.urls', namespace='rest_framework')))