from django.urls import path
from . import views

urlpatterns = [
    path('',views.ask_question,name='ask_question'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('unlike_answer/<int:answer_id>/', views.unlike_answer, name='unlike_answer'),
]