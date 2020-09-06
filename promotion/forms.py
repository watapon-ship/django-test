from django import forms
from django.forms import ModelForm
from promotion.models import Students, StudentPodiitons


class StudentsForm(ModelForm):
    """学生のフォーム"""
    class Meta:
        model = Students
        fields = ('code', 'name', 'sex', 'birth_day', 'personality' , )

class StudentPodiitonForm(ModelForm):
    """学生ポジションのフォーム"""
    class Meta:
        model = StudentPodiitons
        fields=("years", "classes", "grade", "number", "clubs", "clubs_type", "committees", "committees_type", )

