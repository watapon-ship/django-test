from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_list/', views.student_list, name='student_list'),
    path('student_list/add/', views.student_add, name='student_add'),
    path('student_list/edit/<int:student_id>/', views.student_edit, name='student_edit'),
    path('student_list/del/<int:student_id>/', views.student_del, name='student_del'),
]