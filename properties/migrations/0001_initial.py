# Generated by Django 4.2.9 on 2024-01-19 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(default='Describe your property. It increases the chances to be shortlisted')),
                ('rental_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('brokerage', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('maintenance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('security_deposit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True)),
                ('furnishing_type', models.CharField(choices=[('Unfurnished', 'Unfurnished'), ('Semi Furnished', 'Semi Furnished'), ('Fully Furnished', 'Fully Furnished')], default='Unfurnished', max_length=256)),
                ('carpet_area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_location', models.CharField(max_length=256)),
                ('availability', models.CharField(choices=[('Immediately', 'Immediately'), ('Within 15 days', 'Within 15 days'), ('Within 30 days', 'Within 30 days'), ('After a month', 'After a month')], default='Immediately', max_length=256)),
                ('tenant_type', models.CharField(choices=[('Any', 'Any'), ('Bachelor', 'Bachelor'), ('Family', 'Family')], default='Any', max_length=256)),
                ('property_age', models.CharField(default='New', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='properties/2/')),
                ('image_url', models.URLField(default='https://upload.wikimedia.org/wikipedia')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.properties')),
            ],
        ),
    ]
