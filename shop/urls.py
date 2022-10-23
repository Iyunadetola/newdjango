from django.urls import path,include
from rest_framework import routers
from .views import ShopViewSet

router=routers.DefaultRouter()

router.register(r'shop', ShopViewSet)

urlpatterns=[
    path('', include(router.urls))
]