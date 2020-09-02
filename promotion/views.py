from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,
                  'index.html',     # 使用するテンプレート
                  {})         # テンプレートに渡すデータ


def student_list(request):
    #student = Student.objects.all().order_by('id')
    return render(request,
                  'student_list.html',     # 使用するテンプレート
                  {})                 # テンプレートに渡すデータ
