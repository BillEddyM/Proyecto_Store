# Generated by Django 4.0 on 2022-10-06 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_marca_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='talla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.talla'),
        ),
    ]
