# Generated by Django 2.0.3 on 2018-04-17 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='小区ID')),
                ('title', models.CharField(max_length=255, verbose_name='小区名称')),
                ('link', models.CharField(max_length=255, unique=True, verbose_name='小区链接')),
                ('district', models.CharField(max_length=255, verbose_name='所在行政区')),
                ('bizcircle', models.CharField(max_length=255, verbose_name='所在商圈')),
                ('taglist', models.CharField(db_column='tagList', max_length=255, verbose_name='附近地铁站')),
                ('onsale', models.CharField(max_length=255, verbose_name='在售')),
                ('onrent', models.CharField(blank=True, max_length=255, null=True, verbose_name='在租')),
                ('year', models.CharField(blank=True, max_length=255, null=True, verbose_name='建成年份')),
                ('housetype', models.CharField(blank=True, max_length=255, null=True, verbose_name='建筑类型')),
                ('cost', models.CharField(blank=True, max_length=255, null=True, verbose_name='物业费用')),
                ('service', models.CharField(blank=True, max_length=255, null=True, verbose_name='物业公司')),
                ('company', models.CharField(blank=True, max_length=255, null=True, verbose_name='开发商')),
                ('building_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='楼栋总数')),
                ('house_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='房屋总数')),
                ('price', models.CharField(blank=True, max_length=255, null=True, verbose_name='小区均价')),
                ('validdate', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'community',
                'ordering': ('id',),
                'managed': False,
            },
        ),
    ]
