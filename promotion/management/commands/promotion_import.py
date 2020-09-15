import logging
import os
import csv
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from promotion.models import Years, Classes, Clubs, Committees, Students, StudentPodiitons, Teachars, TeacharPodiitons
from promotion.settings import PROMOTION
from portfolio.settings import LOGGING_LEVEL

#IMPORT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/import/'
#logger = logging.getLogger('development')
logger=logging.getLogger(LOGGING_LEVEL)

REQUIRED = {
    'CLASSES_LIST_FILE' : [
        'code',
        'grade',
        'class_number',
        'name',
        'detail',
    ],
    'CLAB_LIST_FILE' : [
        'code',
        'name',
        'detail',
    ],
    'COMMITTEES_LIST_FILE' : [
        'code',
        'name',
        'detail',
    ],
    'ENROLLEES_LIST_FILE' : [
        'code',
        'name',
        'sex',
        'birth_day',
        'personality',
        'classes_code',
        'grade',
        'number',
        'clubs_code',
        'clubs_type',
        'committees_code',
        'committees_type',
    ],
}

#@django.db.transaction.commit_manually
class Command(BaseCommand): 
    args = '<target_id target_id ...>'
    help = u'年度を更新する。'

    def handle(self, *args, **options):
        logger.info('年度更新バッチを起動')
        try:
            # クラス、クラブ、委員会のリスト
            classes_list = {}
            clubs_list = {}
            committees_list = {}

            # 最新の年度情報を取得（存在しない場合は設定値から設定する）
            logger.info('最新年度取得')
            years = Years.objects.order_by("id").last()
            year = PROMOTION['INIT_YEAR']
            if years :
                year = years.year + 1

            logger.info('{0}年度の情報をインポートします。'.format(year))
            years = Years()
            years.year = year
            years.save()
            
            logger.info('年度更新-クラス情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['CLASSES_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for csv_row in f :
                    classes = Classes()
                    classes.code = csv_row['code']
                    classes.years = years
                    classes.grade = csv_row['grade']
                    classes.class_number = csv_row['class_number']
                    classes.name = csv_row['name']
                    classes.detail = csv_row['detail']
                    classes.save()
                    # 後の処理のためにリストを追加
                    classes_list[csv_row['code']] =  classes

            logger.info('年度更新-クラブ活動情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['CLAB_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for csv_row in f:
                    clubs = Clubs.objects.all().filter(code=csv_row['code']).order_by("id").last()
                    if clubs :
                        clubs.code = csv_row['code']
                        clubs.name = csv_row['name']
                        clubs.detail = csv_row['detail']
                        clubs.save()
                    else : 
                        clubs = Clubs()
                        clubs.code = csv_row['code']
                        clubs.name = csv_row['name']
                        clubs.detail = csv_row['detail']
                        clubs.save()

                    # 後の処理のためにリストを追加
                    clubs_list[csv_row['code']] = clubs
            
            logger.info('年度更新-委員会情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['COMMITTEES_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for csv_row in f:
                    committees = Committees.objects.all().filter(code=csv_row['code']).order_by("id").last()
                    if committees :
                        committees.code = csv_row['code']
                        committees.name = csv_row['name']
                        committees.detail = csv_row['detail']
                        committees.save()
                    else : 
                        committees = Committees()
                        committees.code = csv_row['code']
                        committees.name = csv_row['name']
                        committees.detail = csv_row['detail']
                        committees.save()

                    # 後の処理のためにリストを追加
                    committees_list[csv_row['code']] = committees

            logger.info('年度更新-入学者情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['ENROLLEES_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for csv_row in f:
                    students = Students()
                    students.code = csv_row['code']
                    students.name = csv_row['name']
                    students.sex = csv_row['sex']
                    students.birth_day = csv_row['birth_day']
                    students.personality = csv_row['personality']
                    students.save()

                    student_podiitons = StudentPodiitons()
                    student_podiitons.years = years
                    student_podiitons.students = students
                    student_podiitons.classes = classes_list[csv_row['classes_code']]
                    student_podiitons.grade = csv_row['grade']
                    student_podiitons.number = csv_row['number']
                    student_podiitons.clubs = clubs_list[csv_row['clubs_code']]
                    student_podiitons.clubs_type = csv_row['clubs_type']
                    student_podiitons.committees = committees_list[csv_row['committees_code']]
                    student_podiitons.committees_type = csv_row['committees_type']
                    student_podiitons.save()

            logger.info('年度更新-進級者情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['PROMOTION_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for csv_row in f:
                    students = Students.objects.all().filter(code=csv_row['code']).order_by("id").last()

                    student_podiitons = StudentPodiitons()
                    student_podiitons.years = years
                    student_podiitons.students = students
                    student_podiitons.classes = classes_list[csv_row['classes_code']]
                    student_podiitons.grade = csv_row['grade']
                    student_podiitons.number = csv_row['number']
                    student_podiitons.clubs = clubs_list[csv_row['clubs_code']]
                    student_podiitons.clubs_type = csv_row['clubs_type']
                    student_podiitons.committees = committees_list[csv_row['committees_code']]
                    student_podiitons.committees_type = csv_row['committees_type']
                    student_podiitons.save()

            logger.info('年度更新-教職員情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['TEACHAR_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for csv_row in f:
                    teachars = Teachars()
                    teachars.code = csv_row['code']
                    teachars.name = csv_row['name']
                    teachars.position = csv_row['position']
                    teachars.sex = csv_row['sex']
                    teachars.birth_day = csv_row['birth_day']
                    teachars.personality = csv_row['personality']
                    teachars.save()

                    teachar_podiitons = TeacharPodiitons()
                    teachar_podiitons.years = years
                    teachar_podiitons.teachar = teachars
                    teachar_podiitons.classes = classes_list[csv_row['classes_code']]
                    teachar_podiitons.classes_type = csv_row['classes_type']
                    teachar_podiitons.clubs = clubs_list[csv_row['clubs_code']]
                    teachar_podiitons.committees = committees_list[csv_row['committees_code']]
                    teachar_podiitons.save()

        except UnicodeDecodeError :
            transaction.rollback()
            raise InvalidSourceExcepion('Error: Failed to decode in line {}'.format(idx))
        except Exception as e :
            transaction.rollback()
            raise Exception(e)
        else :
            transaction.commit()

        


