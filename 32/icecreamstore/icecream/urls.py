from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from . import views

router = routers.DefaultRouter()
router.register('icecream', views.IcecreamView, 'icecream')
urlpatterns = [
    path('', views.hello_view),
    path('api/', include(router.urls)),
    path('api/random', views.get_random_icecream),
    path('api/featured', views.get_featured_taste),
    path('api/token', TokenObtainPairView.as_view())
]
