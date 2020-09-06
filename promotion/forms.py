from django import forms
from django.forms import ModelForm
from promotion.models import Students, StudentPodiitons, Years


class StudentsForm(ModelForm):
    """学生登録のフォーム"""
    class Meta:
        model = Students
        fields = ('code', 'name', 'sex', 'birth_day', 'personality' , )

class StudentPodiitonForm(ModelForm):
    """学生ポジション登録のフォーム"""
    class Meta:
        model = StudentPodiitons
        fields=("years", "classes", "grade", "number", "clubs", "clubs_type", "committees", "committees_type", )

class SearchForm(ModelForm):
    """検索フォーム"""
    class Meta:
        model = Years
        fields=("year",)

