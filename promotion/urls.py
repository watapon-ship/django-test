from django.urls import path

from rest_framework import routers
from .views import student_list, teachar_list
from .views.api import YearsViewSet, ClassesViewSet, ClubsViewSet, CommitteesViewSet, StudentPodiitonsViewSet, TeacharPodiitonsViewSet

urlpatterns = [
    # トップ
    path('', student_list.index, name='index'),
    # 生徒一覧
    path('student_list/', student_list.student_list, name='student_list'),
    # 転校生追加
    path('student_list/add/', student_list.student_add, name='student_add'),
    # 生徒情報修正
    path('student_list/edit/<int:student_id>/<int:year_id>/', student_list.student_edit, name='student_edit'),
    # 生徒転校
    path('student_list/del/<int:student_id>/', student_list.student_del, name='student_del'),

    # 教師一覧
    path('teachar_list/', teachar_list.teachar_list, name='teachar_list'),
    # 教師追加
    path('teachar_list/add/', teachar_list.teachar_add, name='teachar_add'),
    # 教師情報修正
    path('teachar_list/edit/<int:teachar_id>/<int:year_id>/', teachar_list.teachar_edit, name='teachar_edit'),
    # 教師転勤
    path('teachar_list/del/<int:teachar_id>/', teachar_list.teachar_del, name='teachar_del'),
]

router = routers.DefaultRouter()
router.register(r'years', YearsViewSet)
router.register(r'classes', ClassesViewSet)
router.register(r'clubs', ClubsViewSet)
router.register(r'committees', CommitteesViewSet)
router.register(r'student', StudentPodiitonsViewSet)
router.register(r'teachar', TeacharPodiitonsViewSet)
