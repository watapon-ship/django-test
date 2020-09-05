from django.forms import ModelForm
from promotion.models import Students


class StudentsForm(ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Students
        fields = ('code', 'name', 'number', 'sex', 'birth_day', 'personality' , )