from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from promotion.models import Students, StudentPodiitons, Years
from promotion.forms import StudentsForm, StudentPodiitonForm, SearchForm


# トップ画面
def index(request):
    return render(request,
                  'index.html',     # 使用するテンプレート
                  {})         # テンプレートに渡すデータ

# 生徒名簿
def student_list(request):
    #student_list = Students.objects.all().order_by('id')
    years = Years()
    form = SearchForm()
    if request.method == 'POST':
        # 検索フォームを使っている場合は選択年月で絞る
        form = SearchForm(request.POST, instance=years)  # POST された request データからフォームを作成
        years = form.save(commit=False)
    else:
        # 検索フォームを使っていない場合は最新年月で絞る
        years = Years.objects.order_by("id").last()
        form = SearchForm(initial = {
            'year': years.year   # 初期値
        })

    student_list = StudentPodiitons.objects.all().filter(years__year=years.year).order_by('id')

    return render(request,
                  'student_list/list.html',     # 使用するテンプレート
                  dict(form=form, student_list=student_list, year=years.year),
                  )                 # テンプレートに渡すデータ

    # datadesustr = str([200,{'rss': 1999, 'saa': '\x31' }])
    # datadesu = eval(datadesustr)
    # return render(request,
    #               'student_list.html',     # 使用するテンプレート
    #               dict(form=form, student_list=student_list, datadesu=datadesu[1]),
    #               )                 # テンプレートに渡すデータ

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
        'student_list/add.html',     # 使用するテンプレート
        dict(form=form, sub_form=sub_form))         # テンプレートに渡すデータ

def student_edit(request, student_id=None, year_id=None):

    if student_id and year_id:   # id が指定されている (修正時)
        students = get_object_or_404(Students, pk=student_id)
        student_podiitons = get_object_or_404(StudentPodiitons, students_id=student_id, years_id=year_id)
    else:         # id が指定されていない (追加時)
        return redirect('student_list')

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
        form = StudentsForm(instance=students)
        sub_form = StudentPodiitonForm(instance=student_podiitons)

    # GET の時
    return render(request,
        'student_list/edit.html',     # 使用するテンプレート
        dict(form=form, sub_form=sub_form, student_id=student_id, year_id=year_id))         # テンプレートに渡すデータ

def student_del(request, student_id=None):
    students = get_object_or_404(Students, pk=student_id)
    students.delete()
    return redirect('student_list')

