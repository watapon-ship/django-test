from django.shortcuts import render
from django.http import HttpResponse

from promotion.models import StudentPodiitons
from promotion.forms import StudentsForm

def index(request):
    return render(request,
                  'index.html',     # 使用するテンプレート
                  {})         # テンプレートに渡すデータ


def student_list(request):
    student_list = StudentPodiitons.objects.all().order_by('id')
    return render(request,
                  'student_list.html',     # 使用するテンプレート
                  {
                      'student_list': student_list
                  })                 # テンプレートに渡すデータ

def student_add(request):
    form = StudentsForm()  # フォームを作成
    return render(request,
                  'student_edit.html',     # 使用するテンプレート
                  dict(form=form))         # テンプレートに渡すデータ

def student_edit(request, students_id=None):
    return render(request,
        'student_edit.html',     # 使用するテンプレート
        {})         # テンプレートに渡すデータ

def student_del(request, students_id=None):
    return render(request,
        'index.html',     # 使用するテンプレート
        {})         # テンプレートに渡すデータ