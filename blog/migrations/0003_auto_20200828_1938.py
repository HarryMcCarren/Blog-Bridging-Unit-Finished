# Generated by Django 2.2.15 on 2020-08-28 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200828_1721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('can_approve', 'Can approve comments.'),)},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_see_drafts', 'Can view draft posts.'), ('can_publish', 'Can publish draft posts.'))},
        ),
    ]
