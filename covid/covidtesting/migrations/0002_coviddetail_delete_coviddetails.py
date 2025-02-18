# Generated by Django 4.1.3 on 2023-05-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidtesting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breathing_problem', models.BooleanField()),
                ('fever', models.BooleanField()),
                ('dry_cough', models.BooleanField()),
                ('sore_throat', models.BooleanField()),
                ('running_nose', models.BooleanField()),
                ('asthma', models.BooleanField()),
                ('chronic_lung_disease', models.BooleanField()),
                ('headache', models.BooleanField()),
                ('heart_disease', models.BooleanField()),
                ('diabetes', models.BooleanField()),
                ('hyper_tension', models.BooleanField()),
                ('fatigue', models.BooleanField()),
                ('gastrointestinal', models.BooleanField()),
                ('abroad_travel', models.BooleanField()),
                ('contact_with_covid_patient', models.BooleanField()),
                ('attended_large_gathering', models.BooleanField()),
                ('visited_public_exposed_places', models.BooleanField()),
                ('family_working_in_public_exposed_places', models.BooleanField()),
                ('wearing_masks', models.BooleanField()),
                ('sanitization_from_market', models.BooleanField()),
                ('covid_19', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='CovidDetails',
        ),
    ]
