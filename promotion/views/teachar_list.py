import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from promotion.models import Teachars, TeacharPodiitons, Years
from promotion.forms import TeacharsForm, TeacharPodiitonForm, SearchForm
from portfolio.settings import LOGGING_LEVEL

logger=logging.getLogger(LOGGING_LEVEL)

# 教師一覧
def teachar_list(request):
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

    teachar_list = TeacharPodiitons.objects.all().filter(years__year=years.year).order_by('id')

    return render(request,
                  'teachar_list/list.html',     # 使用するテンプレート
                  dict(form=form, teachar_list=teachar_list, year=years.year),
                  )                 # テンプレートに渡すデータ


# 教師追加
def teachar_add(request):
    teachars = Teachars()
    teachar_podiitons = TeacharPodiitons()
    if request.method == 'POST':
        form = TeacharsForm(request.POST, instance=teachars)  # POST された request データからフォームを作成
        sub_form = TeacharPodiitonForm(request.POST, instance=teachar_podiitons)  # POST された request データからフォームを作成
        if form.is_valid() and sub_form.is_valid():    # フォームのバリデーション
            teachar = form.save(commit=False)
            teachar.save()
            teachar_podiiton = sub_form.save(commit=False)
            teachar_podiiton.teachar = student
            teachar_podiiton.save()
            return redirect('teachar_list')
    else:
        form = TeacharsForm()
        sub_form = TeacharPodiitonForm()

    # GET の時
    return render(request,
        'teachar_list/add.html',     # 使用するテンプレート
        dict(form=form, sub_form=sub_form))         # テンプレートに渡すデータ

# 教師情報修正
def teachar_edit(request, teachar_id=None, year_id=None):
    if teachar_id and year_id:   # id が指定されている (修正時)
        teachars = get_object_or_404(Teachars, pk=teachar_id)
        teachar_podiitons = get_object_or_404(TeacharPodiitons, teachar_id=teachar_id, years_id=year_id)
    else:         # id が指定されていない (追加時)
        return redirect('teachar_list')

    if request.method == 'POST':
        form = TeacharsForm(request.POST, instance=teachars)  # POST された request データからフォームを作成
        sub_form = TeacharPodiitonForm(request.POST, instance=teachar_podiitons)  # POST された request データからフォームを作成
        if form.is_valid() and sub_form.is_valid():    # フォームのバリデーション
            teachar = form.save(commit=False)
            teachar.save()
            teachar_podiiton = sub_form.save(commit=False)
            teachar_podiiton.teachar = teachar
            teachar_podiiton.save()
            return redirect('teachar_list')
    else:
        form = TeacharsForm(instance=teachars)
        sub_form = TeacharPodiitonForm(instance=teachar_podiitons)

    # GET の時
    return render(request,
        'teachar_list/edit.html',     # 使用するテンプレート
        dict(form=form, sub_form=sub_form, teachar_id=teachar_id, year_id=year_id))         # テンプレートに渡すデータ

# 教師転勤
def teachar_del(request, teachar_id=None, year_id=None):
    teachars = get_object_or_404(Teachars, pk=teachar_id)
    teachars.delete()
    return redirect('teachar_list')