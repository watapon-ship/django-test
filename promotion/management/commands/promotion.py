import logging
import os
import csv
from django.db import transaction
from django.core.management.base import BaseCommand, CommandError
from promotion.models import Years
from portfolio.settings import IMPORT_DIR, CLAB_LIST_FILE, COMMITTEES_LIST_FILE, STUDENT_LIST_FILE, TEACHAR_LIST_FILE, FILE_ENCORD, FILE_LINE

#IMPORT_DIR = os.path.dirname(os.path.abspath(__file__)) + '/import/'
#logger = logging.getLogger('development')
logger=logging.getLogger(__name__)

#@django.db.transaction.commit_manually
class Command(BaseCommand): 
    args = '<target_id target_id ...>'
    help = u'年度を更新する。'

    def handle(self, *args, **options):
        logger.info('年度更新バッチを起動')
        try:
            print(IMPORT_DIR + STUDENT_LIST_FILE)
            # with open(IMPORT_DIR + STUDENT_LIST_FILE, "r", encoding=FILE_ENCORD, errors="", newline="" ) as csv_file:
            #     f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator=FILE_LINE, quotechar='"', skipinitialspace=True)
            #     for row in f:
                    

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
        


