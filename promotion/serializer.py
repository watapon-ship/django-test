from rest_framework import serializers # Django Rest Frameworkをインポート
from promotion.models import Years, Classes, Clubs, Committees, Students, StudentPodiitons, Teachars, TeacharPodiitons

class YearsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Years # 扱う対象のモデル名を設定する
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes # 扱う対象のモデル名を設定する
        fields = '__all__'

class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clubs # 扱う対象のモデル名を設定する
        fields = '__all__'

class CommitteesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committees # 扱う対象のモデル名を設定する
        fields = '__all__'

class StudentPodiitonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPodiitons # 扱う対象のモデル名を設定する
        fields = '__all__'

class TeacharPodiitonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacharPodiitons # 扱う対象のモデル名を設定する
        fields = '__all__'
