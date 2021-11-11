from django.urls import path, include
from event import views

urlpatterns = [
    path('', views.EventUsersDataCreateView.as_view()),
    path('list/', views.EventUsersDataListView.as_view()),
]
