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
            
            logger.info('クラス情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['CLASSES_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['CLASSES_LIST_FILE'])
                w1.writerows([['CL000001', '1', '1', '1年1組','ここにクラスの特徴を記載します'],['CL000002', '1', '2', '1年2組','ここにクラスの特徴を記載します'],['CL000003', '1', '3', '1年3組','ここにクラスの特徴を記載します'],['CL000004', '1', '4', '1年4組','ここにクラスの特徴を記載します'],['CL000005', '1', '5', '1年5組','ここにクラスの特徴を記載します'],['CL000006', '2', '1', '2年1組','ここにクラスの特徴を記載します'],['CL000007', '2', '2', '2年2組','ここにクラスの特徴を記載します'],['CL000008', '2', '3', '2年3組','ここにクラスの特徴を記載します'],['CL000009', '2', '4', '2年4組','ここにクラスの特徴を記載します'],['CL000010', '2', '5', '2年5組','ここにクラスの特徴を記載します'],['CL000011', '3', '1', '3年1組','ここにクラスの特徴を記載します'],['CL000012', '3', '2', '3年2組','ここにクラスの特徴を記載します'],['CL000013', '3', '3', '3年3組','ここにクラスの特徴を記載します'],['CL000014', '3', '4', '3年4組','ここにクラスの特徴を記載します'],['CL000015', '3', '5', '3年5組','ここにクラスの特徴を記載します'],['CL000016', '4', '1', '4年1組','ここにクラスの特徴を記載します'],['CL000017', '4', '2', '4年2組','ここにクラスの特徴を記載します'],['CL000018', '4', '3', '4年3組','ここにクラスの特徴を記載します'],['CL000019', '4', '4', '4年4組','ここにクラスの特徴を記載します'],['CL000020', '4', '5', '4年5組','ここにクラスの特徴を記載します'],['CL000021', '5', '1', '5年1組','ここにクラスの特徴を記載します'],['CL000022', '5', '2', '5年2組','ここにクラスの特徴を記載します'],['CL000023', '5', '3', '5年3組','ここにクラスの特徴を記載します'],['CL000024', '5', '4', '5年4組','ここにクラスの特徴を記載します'],['CL000025', '5', '5', '5年5組','ここにクラスの特徴を記載します'],['CL000026', '6', '1', '6年1組','ここにクラスの特徴を記載します'],['CL000027', '6', '2', '6年2組','ここにクラスの特徴を記載します'],['CL000028', '6', '3', '6年3組','ここにクラスの特徴を記載します'],['CL000029', '6', '4', '6年4組','ここにクラスの特徴を記載します'],['CL000030', '6', '5', '6年5組','ここにクラスの特徴を記載します'],])
            
            logger.info('部活情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['CLAB_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['CLAB_LIST_FILE'])
                w1.writerows([['CLB00001', 'サッカー部', 'ボールは友達'],['CLB00002', '野球部', '将来のジャイアンズ'],['CLB00003', 'ソフトテニス部', '初心者歓迎'],['CLB00004', 'ドッジボール部', '今勢いがあります'],['CLB00005', '陸上部', 'ゆったりしてます'],['CLB00006', 'ラグビー部', '運動部のパワー派'],['CLB00007', '水泳部', '自分のペースでいきましょう'],['CLB00008', 'チアリーディング部', 'かわいい子が多いです'],['CLB00009', 'バスケ部', '競争率高い'],['CLB00010', '剣道部', '身も心も強くなろう'],])

            logger.info('部活情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['COMMITTEES_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['COMMITTEES_LIST_FILE'])
                w1.writerows([['IIK00001', '生徒会', '学校行事を取り仕切ります'],['IIK00002', '保健委員', '体調不良の生徒がいた場合、保健室と連携を取ります'],['IIK00003', '生活委員', '学校の服装や素行を見張ります'],['IIK00004', '新聞委員', '学校新聞を作り校内活動を知らせます'],['IIK00005', '図書委員', '図書室を管理します'],['IIK00006', '飼育委員', '学校の動物の世話します'],['IIK00007', '福祉委員', '町内と連携を取りボランティア活動を行います'],['IIK00008', '文化委員', '文化部を管理します'],['IIK00009', '体育委員', '体育部を管理します'],['IIK00010', '園芸委員', '学校の花壇の世話します'],])
            
            logger.info('入学者情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['ENROLLEES_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['ENROLLEES_LIST_FILE'])
                w1.writerows([['S000000001', '青山　喜一', '1','1994-04-01','元気な生徒です。','CL000001','1','1','CLB00001','1','IIK00002','1'],['S000000002', '赤神　竜也', '1','1994-06-22','頭のいい生徒です。','CL000001','2','2','CLB00002','1','IIK00003','1'],['S000000003', '黄瀬　智子', '2','1994-08-21','思いやりにあふれる生徒です。','CL000001','3','3','CLB00003','1','IIK00002','1'],['S000000004', '佐藤　京子', '2','1994-07-11','精一杯な努力家。','CL000001','2','4','CLB00002','1','IIK00005','1'],['S000000005', '田村　栄一', '1','1994-12-21','冷静な生徒です。','CL000001','5','5','CLB00004','1','IIK00004','1'],['S000000006', '遠山　東子', '2','1994-11-11','ユーモアにあふれる生徒です。','CL000001','3','6','CLB00002','1','IIK00003','1'],['S000000007', '中上　隆一', '1','1995-03-03','クラスのリーダーとして頑張っております。','CL000001','2','7','CLB00002','1','IIK00002','1'],['S000000008', '野村　佐助', '1','1994-04-22','がむしゃらな生徒です。','CL000001','1','8','CLB00005','1','IIK00005','1'],['S000000009', '堀内　梓', '2','1994-09-13','明るい性格の生徒です。','CL000001','2','9','CLB00002','1','IIK00006','1'],['S000000010', '八神　東三郎', '1','1994-08-21','独自の視点を持つ生徒です。','CL000001','3','10','CLB00006','1','IIK00003','1'],])

            logger.info('進級者情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['PROMOTION_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['PROMOTION_LIST_FILE'])
                w1.writerows([['S000000001','CL000001','1','1','CLB00001','2','IIK00002','2'],['S000000002','CL000001','2','2','CLB00002','2','IIK00003','2'],['S000000003','CL000001','3','3','CLB00003','2','IIK00002','2'],['S000000004','CL000001','2','4','CLB00002','2','IIK00005','2'],['S000000005','CL000001','5','5','CLB00004','2','IIK00004','2'],['S000000006','CL000001','3','6','CLB00002','2','IIK00003','2'],['S000000007','CL000001','2','7','CLB00002','2','IIK00002','2'],['S000000008','CL000001','1','8','CLB00005','2','IIK00005','2'],['S000000009','CL000001','2','9','CLB00002','2','IIK00006','2'],['S000000010','CL000001','3','10','CLB00006','2','IIK00003','2'],])

            logger.info('教師情報を出力')
            with open(PROMOTION['IMPORT_DIR'] + PROMOTION['TEACHAR_LIST_FILE'], 'w', encoding=PROMOTION['FILE_ENCORD'], newline='') as f:
                w1 = csv.writer(f)
                w1.writerow(CSV_HEAD['TEACHAR_LIST_FILE'])
                w1.writerows([['T0000001', '一ノ瀬　隆二', '算数', '1','1971-02-13','生徒によりそう指導を行います。','CL000001','1','CLB00001','IIK00001',],['T0000002', '双葉　真紀', '国語', '2','1983-12-21','生徒の可能性を伸ばします。','CL000001','2','CLB00002','IIK00002',],['T0000003', '三作　桜', '社会', '2','1980-05-04','勉強の楽しさを教えます。','CL000002','1','CLB00003','IIK00003',],['T0000004', '四宮　太郎', '算数', '1','1968-08-01','生徒の思い出を重視します。','CL000002','2','CLB00004','IIK00004',],['T0000005', '五藤　花子', '家庭科', '2','1966-01-01','生徒に一人で生きる手段を考えます。','CL000003','1','CLB00005','IIK00005',],['T0000006', '六邑　次郎', '国語', '1','1977-03-21','生徒に厳しくも優しく。','CL000004','1','CLB00006','IIK00006',],['T0000007', '七瀬　　栄太', '理科', '1','1987-06-20','生徒の考える力を増やせます。','CL000004','2','CLB00007','IIK00007',],['T0000008', '八木　昭', '理科', '1','1971-05-01','生徒の悩みに真剣にあたります。','CL000005','1','CLB00008','IIK00008',],['T0000009', '田中　九郎', '英語', '1','1973-03-14','生徒の可能性を信じます','CL000006','2','CLB00009','IIK00009',],['T0000010', '大塚　十子', '保健', '1','1976-11-11','生徒の才能を意識します。','CL000007','1','CLB00010','IIK00010',],])

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
        


