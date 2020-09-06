from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from promotion.models import Students, StudentPodiitons
from promotion.forms import StudentsForm, StudentPodiitonForm

def index(request):
    return render(request,
                  'index.html',     # 使用するテンプレート
                  {})         # テンプレートに渡すデータ


def student_list(request):
    student_list = Students.objects.all().order_by('id')
    return render(request,
                  'student_list.html',     # 使用するテンプレート
                  {
                      'student_list': student_list
                  })                 # テンプレートに渡すデータ

def student_add(request):
    students = Students()
    student_podiitons = StudentPodiitons()
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=students)  # POST された request データからフォームを作成
        sub_form = StudentPodiitonForm(request.POST, instance=student_podiitons)  # POST された request データからフォームを作成
        if form.is_valid() and sub_form.is_valid():    # フォームのバリデーション
            student = form.save(commit=False)
            student.save()
            student_podiiton = sub_form.save(commit=False)
            student_podiiton.students = student
            student_podiiton.save()
            return redirect('student_list')
    else:
        form = StudentsForm()
        sub_form = StudentPodiitonForm()

    # GET の時
    return render(request,
        'student_add.html',     # 使用するテンプレート
        dict(form=form, sub_form=sub_form))         # テンプレートに渡すデータ

def student_edit(request, student_id=None):

    if student_id:   # id が指定されている (修正時)
        students = get_object_or_404(Students, pk=student_id)
    else:         # id が指定されていない (追加時)
        return redirect('student_list')

    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=students)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            student = form.save(commit=False)
            student.save()
            return redirect('student_list')
    else:
        form = StudentsForm(instance=students)

    # GET の時
    return render(request,
        'student_edit.html',     # 使用するテンプレート
        dict(form=form, student_id=student_id))         # テンプレートに渡すデータ

def student_del(request, student_id=None):
    students = get_object_or_404(Students, pk=student_id)
    students.delete()
    return redirect('student_list')