# Generated by Django 3.2.9 on 2021-12-07 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0009_alter_receita_pessoa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='pessoa',
            new_name='auth_user',
        ),
    ]