from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'device', views.DeviceViewSet, basename='')


urlpatterns = [
]

urlpatterns += router.urls