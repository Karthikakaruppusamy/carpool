# Generated by Django 5.0.4 on 2024-07-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=255)),
                ('service_duration', models.IntegerField()),
                ('service_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('selected_day', models.CharField(max_length=50)),
                ('selected_time', models.CharField(max_length=50)),
                ('payment_status', models.CharField(default='success', max_length=50)),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
