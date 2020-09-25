# Generated by Django 2.2 on 2020-09-25 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cuidador',
            fields=[
                ('personal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Zoo.Personal')),
                ('horas', models.IntegerField(max_length=5)),
            ],
            bases=('Zoo.personal',),
        ),
        migrations.CreateModel(
            name='Limpiador',
            fields=[
                ('personal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Zoo.Personal')),
                ('horas', models.IntegerField(max_length=5)),
            ],
            bases=('Zoo.personal',),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector', models.CharField(max_length=1)),
                ('limpiadores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zoo.Limpiador')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=50)),
                ('sc_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Saludable', 'Saludable'), ('En_Veterinario', 'En_Veterinario')], default='Saludable', max_length=20)),
                ('cuidadores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Zoo.Cuidador')),
            ],
        ),
    ]