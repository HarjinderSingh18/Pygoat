# Generated by Django 4.0.2 on 2022-06-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0016_alter_blogs_blog_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CF_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
