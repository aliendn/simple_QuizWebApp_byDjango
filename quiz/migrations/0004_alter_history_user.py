# Generated by Django 4.0 on 2021-12-18 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quiz_alter_history_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.user'),
        ),
    ]