# Generated by Django 3.0.5 on 2020-11-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0004_trentalfeedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='UlUnitEquipment',
            fields=[
                ('int_unit_equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('str_unit_equipment', models.CharField(max_length=100)),
                ('str_meaning', models.CharField(blank=True, max_length=100, null=True)),
                ('bol_show', models.BooleanField(blank=True, null=True)),
                ('bol_fixed', models.BooleanField(blank=True, null=True)),
                ('str_export_1', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_2', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_3', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_4', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_5', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_6', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_7', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_8', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_9', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_10', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_11', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_12', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_13', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_14', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_15', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_16', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_17', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_18', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_19', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_20', models.CharField(blank=True, max_length=100, null=True)),
                ('int_order_id', models.IntegerField(blank=True, null=True)),
                ('bol_default_flg', models.BooleanField(blank=True, null=True)),
                ('bol_print', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': '"public"."ul_unit_equipment"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UlUnitEquipmentSelect',
            fields=[
                ('int_unit_equipment_select_id', models.AutoField(primary_key=True, serialize=False)),
                ('int_unit_equipment_id', models.IntegerField()),
                ('int_equipment_id', models.IntegerField()),
                ('str_equipment', models.CharField(blank=True, max_length=100, null=True)),
                ('str_meaning', models.CharField(blank=True, max_length=100, null=True)),
                ('bol_show', models.BooleanField(blank=True, null=True)),
                ('bol_fixed', models.BooleanField(blank=True, null=True)),
                ('str_export_1', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_2', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_3', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_4', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_5', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_6', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_7', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_8', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_9', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_10', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_11', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_12', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_13', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_14', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_15', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_16', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_17', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_18', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_19', models.CharField(blank=True, max_length=100, null=True)),
                ('str_export_20', models.CharField(blank=True, max_length=100, null=True)),
                ('int_order_id', models.IntegerField(blank=True, null=True)),
                ('bol_default_flg', models.BooleanField(blank=True, null=True)),
                ('bol_default_simple_flg', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': '"public"."ul_unit_equipment_select"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerRequirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_tracking_potential_customers_id', models.IntegerField()),
                ('int_min_rental_fee', models.IntegerField()),
                ('int_max_rental_fee', models.IntegerField()),
                ('bol_construction_iron', models.BooleanField(default=False)),
                ('bol_construction_steel', models.BooleanField(default=False)),
                ('bol_construction_wooden', models.BooleanField(default=False)),
                ('bol_consgruction_other', models.BooleanField(default=False)),
                ('bol_layout_one_room', models.BooleanField(default=False)),
                ('bol_layout_1k', models.BooleanField(default=False)),
                ('bol_layout_1dk', models.BooleanField(default=False)),
                ('bol_layout_1ldk', models.BooleanField(default=False)),
                ('bol_layout_2k', models.BooleanField(default=False)),
                ('bol_layout_2dk', models.BooleanField(default=False)),
                ('bol_layout_2ldk', models.BooleanField(default=False)),
                ('bol_layout_3k', models.BooleanField(default=False)),
                ('bol_layout_3dk', models.BooleanField(default=False)),
                ('bol_layout_3ldk', models.BooleanField(default=False)),
                ('bol_layout_4k', models.BooleanField(default=False)),
                ('bol_layout_4dk', models.BooleanField(default=False)),
                ('bol_layout_4ldk', models.BooleanField(default=False)),
                ('int_line1', models.IntegerField()),
                ('int_station1', models.IntegerField()),
                ('int_line2', models.IntegerField()),
                ('int_station2', models.IntegerField()),
                ('int_line3', models.IntegerField()),
                ('int_station3', models.IntegerField()),
                ('bol_area1', models.BooleanField(default=False)),
                ('bol_area2', models.BooleanField(default=False)),
                ('bol_area3', models.BooleanField(default=False)),
                ('bol_area4', models.BooleanField(default=False)),
                ('int_school_area1', models.IntegerField()),
                ('int_school_area2', models.IntegerField()),
                ('int_school_area3', models.IntegerField()),
                ('int_school_area4', models.IntegerField()),
                ('bol_other_conditions_pet', models.BooleanField(default=False)),
                ('bol_other_conditions_city_gas', models.BooleanField(default=False)),
                ('bol_other_conditions_second_floor', models.BooleanField(default=False)),
                ('bol_other_conditions_bath_toilet', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TrackingUnitEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_tracking_potential_customers_id', models.IntegerField()),
                ('int_equipment_id', models.IntegerField()),
                ('int_equipment_select', models.IntegerField()),
                ('str_premise_name', models.CharField(blank=True, max_length=100, null=True)),
                ('str_premise_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
