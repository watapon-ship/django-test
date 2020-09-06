from django.db import models

# 年度
class Years(models.Model):
    db_table = 'YEARS'
    verbose_name = '年度'
    sverbose_name_plural = verbose_name
    year = models.IntegerField('年度')

    def __str__(self):
        return str(self.year) + "年度"

# 先生
class Teachars(models.Model):
    #  性別を選択する選択肢を宣言
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (10, 'その他'),
    )

    db_table = 'TEACHAR'
    verbose_name = '学級'
    sverbose_name_plural = verbose_name
    code = models.CharField('教師コード', max_length=8)
    name = models.CharField('名前', max_length=50)
    position = models.CharField('担当教科', max_length=50)
    sex = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
    birth_day = models.DateField(verbose_name='誕生日', blank=True, null=True)
    personality = models.CharField('先生紹介',max_length=200, blank = True, null = True )

    def __str__(self):
        return self.code + ':' + self.name + '先生'

# 生徒
class Students(models.Model):
    #  性別を選択する選択肢を宣言
    GENDER_CHOICES = (
        (1, '男性'),
        (2, '女性'),
        (10, 'その他'),
    )

    db_table = 'STUDENT'
    verbose_name = '生徒'
    sverbose_name_plural = verbose_name
    code = models.CharField('学生コード', max_length=10)
    name = models.CharField('学生名',max_length=50)
    sex = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, blank=True, null=True)
    birth_day = models.DateField(verbose_name='誕生日', blank=True, null=True)
    personality = models.CharField('生徒紹介',max_length=200, blank = True, null = True )

    def __str__(self):
        return self.code +':' + self.name

# 学級
class Classes(models.Model):
    db_table = 'CLASSES'
    verbose_name = '学級'
    sverbose_name_plural = verbose_name
    code = models.CharField('クラスコード', max_length=8)
    grade = models.IntegerField('学年')
    class_number = models.IntegerField('組')
    name = models.CharField('クラス名', max_length=50)
    detail = models.CharField('学級紹介', max_length=200, blank = True, null = True)

    def __str__(self):
        return self.code + ':' + self.name

# クラブ活動
class Clubs(models.Model):
    db_table = 'CLUB'
    verbose_name = 'クラブ活動'
    sverbose_name_plural = verbose_name
    code = models.CharField('クラブコード', max_length=8)
    name = models.CharField('クラブ名', max_length=50)
    detail = models.CharField('クラブ紹介', max_length=200, blank = True, null = True)

    def __str__(self):
        return self.code + ':' + self.name

# 委員会
class Committees(models.Model):
    db_table = 'COMMITTEE'
    verbose_name = '委員会'
    sverbose_name_plural = verbose_name
    code = models.CharField('委員会コード', max_length=8)
    name = models.CharField('委員会名',max_length=50)
    detail = models.CharField('委員会説明', max_length=200, blank = True, null = True)

    def __str__(self):
        return self.code + ':' + self.name

# 教師役職
class TeacharPodiitons(models.Model):
    #  担任・副担任を選択する選択肢を宣言
    CLASS_TEACHAR_CHOICES = (
        (1, '担任'),
        (2, '副担任'),
        (10, 'その他'),
    )

    db_table = 'TEACHAR_POSITIONS'
    verbose_name = '教師役職'
    sverbose_name_plural = verbose_name
    years = models.ForeignKey(Years, verbose_name="年度", on_delete=models.CASCADE)
    teachar = models.ForeignKey(Teachars, verbose_name="教師", on_delete=models.CASCADE, related_name='student_podiitons')
    classes = models.ForeignKey(Classes, verbose_name="担当クラス", on_delete=models.CASCADE, blank = True, null = True)
    classes_type = models.IntegerField(verbose_name='担任・副担任', choices=CLASS_TEACHAR_CHOICES, blank=True, null=True)
    clubs = models.ForeignKey(Clubs, verbose_name="クラブ顧問", on_delete=models.CASCADE, blank = True, null = True)
    committees = models.ForeignKey(Committees, verbose_name="委員会顧問", on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.teachar.name + "の役職"

# 生徒役職
class StudentPodiitons(models.Model):
    #  部活役職を選択する選択肢を宣言
    CLAB_TYPE_CHOICES = (
        (1, '一般'),
        (2, '部長'),
        (3, '副部長'),
        (4, 'マネージャー'),
        (10, 'その他'),
    )

    #  委員会役職を選択する選択肢を宣言
    COMMITTEES_TYPE_CHOICES = (
        (1, '一般'),
        (2, '委員長'),
        (3, '副委員長'),
        (4, '会計'),
        (5, '初期'),
        (10, 'その他'),
    )

    db_table = 'STUDENT_POSITIONS'
    verbose_name = '生徒役職'
    sverbose_name_plural = verbose_name
    years = models.ForeignKey(Years, verbose_name="年度", on_delete=models.CASCADE)
    students = models.ForeignKey(Students, verbose_name="生徒", on_delete=models.CASCADE, blank = True, null = False, related_name='student_podiitons')
    classes = models.ForeignKey(Classes, verbose_name="所属クラス", on_delete=models.CASCADE, blank = True, null = True)
    grade = models.IntegerField('グループ（1班,2班）')
    number = models.IntegerField('クラス番号')
    clubs = models.ForeignKey(Clubs, verbose_name="クラブ活動", on_delete=models.CASCADE, blank = True, null = True)
    clubs_type = models.IntegerField(verbose_name='クラブ役職', choices=CLAB_TYPE_CHOICES, blank=True, null=True)
    committees = models.ForeignKey(Committees, verbose_name="委員会", on_delete=models.CASCADE, blank = True, null = True)
    committees_type = models.IntegerField(verbose_name='委員会役職', choices=COMMITTEES_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.students.name + "の役職"

