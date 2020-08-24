from django.conf.urls import url
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'device', views.DeviceViewSet, basename='')
router.register(r'password', views.PasswordViewSet, basename='')
router.register(r'import_device', views.DeviceFileViewSet, basename='')


urlpatterns = [
]

urlpatterns += router.urls