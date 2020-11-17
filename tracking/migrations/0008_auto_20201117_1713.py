# Generated by Django 3.0.5 on 2020-11-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0007_auto_20201117_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_area1',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_area2',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_area3',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_area4',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_consgruction_other',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_construction_iron',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_construction_steel',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_construction_wooden',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_1dk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_1k',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_1ldk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_2dk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_2k',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_2ldk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_3dk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_3k',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_3ldk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_4dk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_4k',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_4ldk',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_layout_one_room',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_other_conditions_bath_toilet',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_other_conditions_city_gas',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_other_conditions_pet',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='bol_other_conditions_second_floor',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_line1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_line2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_line3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_max_rental_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_min_rental_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_school_area1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_school_area2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_school_area3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_school_area4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_station1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_station2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_station3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerrequirement',
            name='int_tracking_potential_customers_id',
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]
