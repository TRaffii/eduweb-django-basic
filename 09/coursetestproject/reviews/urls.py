from django.urls import path, re_path

from . import views

urlpatterns = [
    path('add', views.add_question),
    path('show/<int:question_id>/', views.show_question),
    re_path(r'^find/(?P<year>[0-9]{4})/$', views.show_by_year)
]