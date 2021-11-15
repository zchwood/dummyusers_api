from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'theOffice_users', views.theOfficeViewSet)
router.register(r'GOT_users', views.GOTViewSet)
router.register(r'random_users', views.random_userViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]