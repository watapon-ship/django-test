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

CSV_HEAD = {
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
    'PROMOTION_LIST_FILE' : [
        'code',
        'classes_code',
        'grade',
        'number',
        'clubs_code',
        'clubs_type',
        'committees_code',
        'committees_type',
    ],
    'TEACHAR_LIST_FILE' : [
        'code',
        'name',
        'position',
        'sex',
        'birth_day',
        'personality',
        'classes_code',
        'classes_type',
        'clubs_code',
        'committees_code',
    ],
}

#@django.db.transaction.commit_manually
class Command(BaseCommand): 
    args = '<target_id target_id ...>'
    help = u'年度を更新する。'

    def handle(self, *args, **options):
        logger.info('年度更新バッチで使うデータのサンプルを出力します。')
        try:

            # 最新の年度情報を取得（存在しない場合は設定値から設定する）
            logger.info('最新年度取得')
            years = Years.objects.order_by("id").last()
            year = PROMOTION['INIT_YEAR']
            if years :
                year = years.year

            logger.info('{0}年度の情報をエクスポートします。'.format(year))
            # years = Years()
            # years.year = year

            logger.info('クラス情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['CLASSES_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['CLASSES_LIST_FILE'])
                classes_list = Classes.objects.all().filter(years__year=years.year).order_by('id')
                for classes in classes_list : 
                    w1.writerow([
                        classes.code,
                        classes.grade,
                        classes.class_number,
                        classes.name,
                        classes.detail,
                    ])
            
            logger.info('部活情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['CLAB_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['CLAB_LIST_FILE'])
                clubs_list = Clubs.objects.all().order_by('id')
                for clubs in clubs_list : 
                    w1.writerow([
                        clubs.code,
                        clubs.name,
                        clubs.detail,
                    ])

            logger.info('委員会情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['COMMITTEES_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['COMMITTEES_LIST_FILE'])
                clubs_list = Clubs.objects.all().order_by('id')
                for clubs in clubs_list : 
                    w1.writerow([
                        clubs.code,
                        clubs.name,
                        clubs.detail,
                    ])

            logger.info('入学者情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['ENROLLEES_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['ENROLLEES_LIST_FILE'])
                students_list = StudentPodiitons.objects.all().filter(years__year=years.year).order_by('id')
                for students in students_list : 
                    w1.writerow([
                        students.students.code,
                        students.students.name,
                        students.students.sex,
                        students.students.birth_day,
                        students.students.personality,
                        students.classes.code,
                        students.grade,
                        students.number,
                        students.clubs.code,
                        students.clubs_type,
                        students.committees.code,
                        students.committees_type,
                    ])
            
            logger.info('進級者情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['PROMOTION_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['PROMOTION_LIST_FILE'])
                students_list = StudentPodiitons.objects.all().filter(years__year=years.year).order_by('id')
                for students in students_list : 
                    w1.writerow([
                        students.students.code,
                        students.classes.code,
                        students.grade + 1,
                        students.number,
                        students.clubs.code,
                        students.clubs_type,
                        students.committees.code,
                        students.committees_type,
                    ])

            logger.info('教師情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['TEACHAR_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['TEACHAR_LIST_FILE'])
                teachars_list = TeacharPodiitons.objects.all().filter(years__year=years.year).order_by('id')
                for teachars in teachars_list : 
                    w1.writerow([
                        teachars.teachar.code,
                        teachars.classes.code,
                        teachars.classes_type,
                        teachars.clubs.code,
                        teachars.committees.code,
                    ])

        except UnicodeDecodeError :
            raise InvalidSourceExcepion('Error: Failed to decode in line {}'.format(idx))
        except Exception as e :
            raise Exception(e)
        else :
            logger.info('成功')
