# Generated by Django 3.1 on 2020-09-05 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='detail',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='学級紹介'),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='detail',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='クラブ紹介'),
        ),
        migrations.AlterField(
            model_name='committees',
            name='detail',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='委員会説明'),
        ),
        migrations.AlterField(
            model_name='studentpodiitons',
            name='classes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.classes', verbose_name='所属クラス'),
        ),
        migrations.AlterField(
            model_name='studentpodiitons',
            name='clubs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.clubs', verbose_name='クラブ活動'),
        ),
        migrations.AlterField(
            model_name='studentpodiitons',
            name='committees',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.committees', verbose_name='委員会'),
        ),
        migrations.AlterField(
            model_name='studentpodiitons',
            name='students',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_podiitons', to='promotion.students', verbose_name='生徒'),
        ),
        migrations.AlterField(
            model_name='students',
            name='personality',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='生徒紹介'),
        ),
        migrations.AlterField(
            model_name='teacharpodiitons',
            name='classes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.classes', verbose_name='担当クラス'),
        ),
        migrations.AlterField(
            model_name='teacharpodiitons',
            name='clubs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.clubs', verbose_name='クラブ顧問'),
        ),
        migrations.AlterField(
            model_name='teacharpodiitons',
            name='committees',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.committees', verbose_name='委員会顧問'),
        ),
        migrations.AlterField(
            model_name='teachars',
            name='personality',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='先生紹介'),
        ),
    ]
