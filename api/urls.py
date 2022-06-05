from django.urls import path

from . import views

urlpatterns = [
    # normal views
    path('students/', views.StudentListView.as_view(), name='student-list'),

    # rest_framework views
    path('', views.StudentListAPIView.as_view()),
    path('look-by-name/<str:name>/', views.StudentNameListAPIView.as_view()),
    path('create/', views.StudentCreateAPIView.as_view()),
    path('<int:pk>/update/', views.StudentUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.StudentDestroyAPIView.as_view()),
    path('<int:pk>/', views.StudentDetailAPIView.as_view()),
]