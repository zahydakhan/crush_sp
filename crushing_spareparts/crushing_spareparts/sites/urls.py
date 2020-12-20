from django.urls import path, include
from rest_framework import routers
from .views import SiteViewSet

router=routers.DefaultRouter()
router.register("sites", SiteViewSet, basename='sites')

urlpatterns = [
    path('', include(router.urls)),
]