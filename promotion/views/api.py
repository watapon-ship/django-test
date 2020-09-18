import logging
from rest_framework import viewsets, filters

from promotion.models import Years, Classes, Clubs, Committees, Students, StudentPodiitons, Teachars, TeacharPodiitons
from promotion.serializer import YearsSerializer, ClassesSerializer, ClubsSerializer, CommitteesSerializer, StudentPodiitonsSerializer, TeacharPodiitonsSerializer
from portfolio.settings import LOGGING_LEVEL

logger=logging.getLogger(LOGGING_LEVEL)

class YearsViewSet(viewsets.ModelViewSet):
    queryset = Years.objects.all() # 全てのデータを取得
    serializer_class = YearsSerializer

class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all() # 全てのデータを取得
    serializer_class = ClassesSerializer

class ClubsViewSet(viewsets.ModelViewSet):
    queryset = Clubs.objects.all() # 全てのデータを取得
    serializer_class = ClubsSerializer

class CommitteesViewSet(viewsets.ModelViewSet):
    queryset = Committees.objects.all() # 全てのデータを取得
    serializer_class = CommitteesSerializer

class StudentPodiitonsViewSet(viewsets.ModelViewSet):
    queryset = StudentPodiitons.objects.all() # 全てのデータを取得
    serializer_class = StudentPodiitonsSerializer

class TeacharPodiitonsViewSet(viewsets.ModelViewSet):
    queryset = TeacharPodiitons.objects.all() # 全てのデータを取得
    serializer_class = TeacharPodiitonsSerializer