# Generated by Django 3.2.9 on 2021-11-14 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ueid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('real_title', models.CharField(max_length=500)),
                ('image_uri', models.CharField(max_length=500)),
                ('high_res_image_uri', models.CharField(max_length=500, null=True)),
                ('bells_sell', models.IntegerField(null=True)),
                ('fake_image_uri', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Critter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ueid', models.CharField(max_length=20)),
                ('critter_type', models.CharField(choices=[('F', 'Fish'), ('B', 'Bug'), ('S', 'Sea')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('icon_uri', models.CharField(max_length=500, null=True)),
                ('image_uri', models.CharField(max_length=500, null=True)),
                ('bells_sell', models.IntegerField()),
                ('source', models.CharField(max_length=500)),
                ('spawn_rates', models.CharField(max_length=500)),
                ('catches_to_unlock', models.IntegerField()),
                ('shadow_size', models.CharField(max_length=500, null=True)),
                ('speed', models.CharField(max_length=500, null=True)),
                ('difficulty', models.CharField(max_length=500, null=True)),
                ('vision', models.CharField(max_length=500, null=True)),
                ('weather', models.CharField(max_length=500, null=True)),
                ('nh_jan', models.CharField(max_length=500)),
                ('nh_feb', models.CharField(max_length=500)),
                ('nh_mar', models.CharField(max_length=500)),
                ('nh_apr', models.CharField(max_length=500)),
                ('nh_may', models.CharField(max_length=500)),
                ('nh_jun', models.CharField(max_length=500)),
                ('nh_jul', models.CharField(max_length=500)),
                ('nh_aug', models.CharField(max_length=500)),
                ('nh_sep', models.CharField(max_length=500)),
                ('nh_oct', models.CharField(max_length=500)),
                ('nh_nov', models.CharField(max_length=500)),
                ('nh_dec', models.CharField(max_length=500)),
                ('sh_jan', models.CharField(max_length=500)),
                ('sh_feb', models.CharField(max_length=500)),
                ('sh_mar', models.CharField(max_length=500)),
                ('sh_apr', models.CharField(max_length=500)),
                ('sh_may', models.CharField(max_length=500)),
                ('sh_jun', models.CharField(max_length=500)),
                ('sh_jul', models.CharField(max_length=500)),
                ('sh_aug', models.CharField(max_length=500)),
                ('sh_sep', models.CharField(max_length=500)),
                ('sh_oct', models.CharField(max_length=500)),
                ('sh_nov', models.CharField(max_length=500)),
                ('sh_dec', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fossil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ueid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('image_uri', models.CharField(max_length=500, null=True)),
                ('bells_sell', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gyroid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ueid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('variation', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=500)),
                ('source_notes', models.CharField(max_length=500)),
                ('icon_uri', models.CharField(max_length=500, null=True)),
                ('image_uri', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ueid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=500)),
                ('source_notes', models.CharField(max_length=500)),
                ('icon_uri', models.CharField(max_length=500, null=True)),
                ('image_uri', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]
