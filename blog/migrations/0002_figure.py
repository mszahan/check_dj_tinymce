# Generated by Django 3.2.11 on 2022-04-28 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Figure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('caption', models.TextField()),
                ('image', models.ImageField(upload_to='figures/%Y/%M')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='figures', to='blog.post')),
            ],
        ),
    ]
