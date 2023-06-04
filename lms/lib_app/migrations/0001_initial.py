# Generated by Django 4.2.1 on 2023-05-28 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('author_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('book_pages', models.IntegerField(blank=True, max_length=5, null=True)),
                ('book_rental_by_dy', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('book_rental_period', models.IntegerField(blank=True, max_length=5, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('available', 'available'), ('rented', 'rented'), ('sold', 'sold')], max_length=50, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lib_app.category')),
            ],
        ),
    ]
