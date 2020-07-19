from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('icecream', views.IcecreamView, 'icecream')
urlpatterns = [
    path('', views.hello_view),
    path('api', include(router.urls))
]
