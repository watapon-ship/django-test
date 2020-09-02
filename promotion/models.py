from django.db import models

# 学級
class Classes(models.Model):
    db_table = 'CLASSES'
    verbose_name = '学級'
    sverbose_name_plural = verbose_name
    name = models.CharField('クラス名', max_length=50)
    teachar = models.CharField('担任', max_length=50)
    sub_teachar = models.CharField('副担任', max_length=50)
    detail = models.CharField('学級紹介', max_length=200)

    def __str__(self):
        return self.name

# グループ
class Groups(models.Model):
    db_table = 'GROUP'
    verbose_name = 'グループ'
    sverbose_name_plural = verbose_name
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    number = models.IntegerField('斑数')

    def __str__(self):
        return str(self.number)

# クラブ活動
class Clubs(models.Model):
    db_table = 'CLUB'
    verbose_name = 'クラブ活動'
    sverbose_name_plural = verbose_name
    name = models.CharField('クラブ名', max_length=50)
    advisor = models.CharField('顧問', max_length=50)
    detail = models.CharField('クラブ紹介', max_length=200)

    def __str__(self):
        return self.name

# 委員会
class Committees(models.Model):
    db_table = 'COMMITTEE'
    verbose_name = '委員会'
    sverbose_name_plural = verbose_name
    name = models.CharField('委員会名',max_length=50)
    advisor = models.CharField('顧問', max_length=50)
    detail = models.CharField('委員会説明', max_length=200)

    def __str__(self):
        return self.name

# 生徒
class Students(models.Model):
    db_table = 'STUDENT'
    verbose_name = '生徒'
    sverbose_name_plural = verbose_name
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    club = models.ForeignKey(Clubs, on_delete=models.CASCADE)
    committee = models.ForeignKey(Committees, on_delete=models.CASCADE)
    name = models.CharField('学生名',max_length=50)
    age = models.CharField('性格',max_length=200)

    def __str__(self):
        return self.name

