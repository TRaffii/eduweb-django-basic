from django.urls import path

from . import views

urlpatterns = [
    path('add', views.add_question),
    path('question/<int:question_id>/', views.show_question)
]