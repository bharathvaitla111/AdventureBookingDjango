# Generated by Django 4.1.7 on 2023-03-04 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jumpstart', '0003_remove_customer_city_remove_customer_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingDate', models.DateField()),
                ('reserveDate', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('typeOfTicketAndPrice', models.CharField(choices=[('Adult', '1000'), ('Child', '600'), ('FastTrackAdult', '2000'), ('FastTrackChild', '1200'), ('SeniorCitizen', '800'), ('AdultCollegeIdOffer', '900')], max_length=20)),
                ('totalPrice', models.PositiveIntegerField(default=0)),
                ('adultTicketCount', models.PositiveIntegerField(default=0)),
                ('ChildTicketCount', models.PositiveIntegerField(default=0)),
                ('FastTrackAdultTicketCount', models.PositiveIntegerField(default=0)),
                ('FastTrackChildTicketCount', models.PositiveIntegerField(default=0)),
                ('SeniorCitizenTicketCount', models.PositiveIntegerField(default=0)),
                ('AdultCollegeIdOfferTicketCount', models.PositiveIntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jumpstart.customer')),
            ],
        ),
    ]
