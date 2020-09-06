from django.urls import path

from . import views

urlpatterns = [
    # トップ
    path('', views.index, name='index'),
    # 生徒一覧
    path('student_list/', views.student_list, name='student_list'),
    # 転校生追加
    path('student_list/add/', views.student_add, name='student_add'),
    # 生徒情報修正
    path('student_list/edit/<int:student_id>/<int:year_id>/', views.student_edit, name='student_edit'),
    # 生徒転校
    path('student_list/del/<int:student_id>/', views.student_del, name='student_del'),
]