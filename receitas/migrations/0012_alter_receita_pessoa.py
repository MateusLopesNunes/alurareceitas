# Generated by Django 3.2.9 on 2021-12-07 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0011_rename_auth_user_receita_pessoa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
        ),
    ]
