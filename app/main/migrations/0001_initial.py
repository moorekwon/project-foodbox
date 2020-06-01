# Generated by Django 3.0.6 on 2020-06-01 04:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('keeping_days', models.PositiveIntegerField()),
                ('kcalories', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='images/ingredients/')),
                ('fridger', models.CharField(choices=[('F', 'Freezer'), ('R', 'Refrigerator'), ('T', 'Room Temperature')], max_length=2)),
                ('type', models.CharField(blank=True, choices=[('vegetables', '채소/과일'), ('meat', '육류'), ('marine', '수산물'), ('grain', '곡물/견과류'), ('sauce', '양념/소스'), ('milk', '가공/유제품'), ('others', '기타')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients_detail', models.CharField(max_length=200)),
                ('recipe', models.TextField()),
                ('type', models.CharField(choices=[('broth', '육수'), ('vegetables', '채소'), ('marine', '해산물'), ('meat', '고기/계란'), ('rice', '밥/쌀'), ('kimchi', '김치/발효'), ('dessert', '간식/디저트')], max_length=30)),
                ('ingredient', models.ManyToManyField(blank=True, to='main.Ingredient')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyStoredIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_date', models.DateField(default=datetime.date.today)),
                ('ingredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyMemoIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('checked', 'checked'), ('not_checked', 'not_checked')], default='not_checked', max_length=20)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
