import logging
import os
import csv
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from promotion.models import Years
from promotion.settings import PROMOTION
from portfolio.settings import LOGGING_LEVEL

#IMPORT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/import/'
#logger = logging.getLogger('development')
logger=logging.getLogger(LOGGING_LEVEL)

CLASSES_LIST_FILE_FORMAT = [
    {
        'key' : 'data_type',
    },
    {
        'key' : 'code',
    },
    {
        'key' : 'grade',
    },
    {
        'key' : 'class_number',
    },
    {
        'key' : 'name',
    },
    {
        'key' : 'detail',
    },
]

CLAB_LIST_FILE_FORMAT = [
    {
        'key' : 'data_type',
    },
    {
        'key' : 'code',
    },
    {
        'key' : 'name',
    },
    {
        'key' : 'detail',
    },
]

COMMITTEES_LIST_FILE_FORMAT = [
    {
        'key' : 'data_type',
    },
    {
        'key' : 'code',
    },
    {
        'key' : 'name',
    },
    {
        'key' : 'detail',
    },
]

STUDENT_LIST_FILE_FORMAT = [
    {
        'key' : 'data_type',
    },
    {
        'key' : 'code',
    },
    {
        'key' : 'name',
    },
    {
        'key' : 'sex',
    },
    {
        'key' : 'birth_day',
    },
    {
        'key' : 'personality',
    },
    {
        'key' : 'sex',
    },
]

#@django.db.transaction.commit_manually
class Command(BaseCommand): 
    args = '<target_id target_id ...>'
    help = u'年度を更新する。'

    def handle(self, *args, **options):
        logger.info('年度更新バッチを起動')
        try:
            # 最新の年度情報を取得（存在しない場合は設定値から設定する）
            logger.info('最新年度取得')
            years = Years.objects.order_by("id").last()
            year = PROMOTION['INIT_YEAR']
            if years :
                year = years.year
            
            logger.info('ファイルチェック-クラブ活動情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['CLAB_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for row in f:
                    # 必須チェック
                    for field in CLAB_LIST_FILE_FORMAT:
                        if field['key'] not in row : 
                            logger.error('必須チェックエラー-クラブ活動情報CSVの' + field['key'] + 'が存在しません。')

            logger.info('ファイルチェック-委員会情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['COMMITTEES_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for row in f:
                    # 必須チェック
                    for field in COMMITTEES_LIST_FILE_FORMAT:
                        if field['key'] not in row : 
                            logger.error('必須チェックエラー-委員会情報CSVの' + field['key'] + 'が存在しません。')

            logger.info('ファイルチェック-生徒情報更新')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['STUDENT_LIST_FILE'], "r", encoding=PROMOTION['FILE_ENCORD'], errors="", newline="" ) as csv_file:
                f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=PROMOTION['FILE_LINE'], quotechar='"', skipinitialspace=True)
                for row in f:
                    # 必須チェック
                    for field in STUDENT_LIST_FILE_FORMAT:
                        if field['key'] not in row : 
                            logger.error('必須チェックエラー-生徒情報CSVの' + field['key'] + 'が存在しません。')

            logger.info('ファイルチェック-教職員情報更新')
            logger.info('年度更新-クラブ活動情報更新')
            logger.info('年度更新-委員会情報更新')
            logger.info('年度更新-生徒情報更新')
            logger.info('年度更新-教職員情報更新')

            logger.debug(PROMOTION['IMPORT_DIR'] + PROMOTION['STUDENT_LIST_FILE'])

        except UnicodeDecodeError :
            transaction.rollback()
            raise InvalidSourceExcepion('Error: Failed to decode in line {}'.format(idx))
        except Exception as e :
            transaction.rollback()
            raise Exception(e)
        else :
            transaction.commit()
            #print("成功")
        # for target_id in args:
        #     logger.info('target_id: %s' % target_id)
        # years = Years()
        # years.year = 2030
        # years.save()
        #path = os.path.join(IMPORT_DIR, IMPORT_DIR + 'a.csv')
        


