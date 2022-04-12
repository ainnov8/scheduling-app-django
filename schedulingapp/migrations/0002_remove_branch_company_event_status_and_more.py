# Generated by Django 4.0.3 on 2022-04-11 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedulingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='company',
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='company',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
