# Generated by Django 4.0.3 on 2022-03-28 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=150)),
                ('postal_code', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('date', models.DateField()),
                ('address', models.TextField()),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=25)),
                ('contact_person', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('company_logo', models.ImageField(max_length=200, upload_to='images/')),
                ('description', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedulingapp.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('role', models.CharField(blank=True, max_length=150, null=True)),
                ('profile_image', models.ImageField(max_length=200, upload_to='profile_images/')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedulingapp.branch')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedulingapp.department')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedulingapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=150)),
                ('province', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(max_length=200, upload_to='profile_images/')),
                ('join_date', models.DateField(auto_now_add=True)),
                ('employees', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='schedulingapp.employee')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedulingapp.company'),
        ),
    ]
