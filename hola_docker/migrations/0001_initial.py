# Generated by Django 4.2.6 on 2023-10-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AGG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ATT', models.CharField(max_length=50)),
                ('TX_Grupos_AGG', models.CharField(max_length=50)),
                ('TX_Detalle_AGG', models.CharField(max_length=50)),
                ('Control', models.CharField(max_length=50)),
                ('Fecha', models.CharField(max_length=10)),
                ('POC', models.CharField(max_length=50)),
                ('Observaciones', models.CharField(max_length=50)),
                ('ID_DOS', models.CharField(max_length=50)),
                ('ID_ATandT', models.CharField(max_length=50)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('LATITUD', models.CharField(max_length=50)),
                ('LONGITUD', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=50)),
                ('Municipio', models.CharField(max_length=50)),
                ('Mercado', models.CharField(max_length=50)),
                ('Mercado_FO', models.CharField(max_length=50)),
                ('Region_Celular', models.CharField(max_length=50)),
                ('AGREGADOR', models.CharField(max_length=50)),
                ('AÑO', models.CharField(max_length=50)),
                ('PROYECTO', models.CharField(max_length=50)),
                ('TOPOLOGÍA', models.CharField(max_length=50)),
                ('SEGMENTO_IPBH', models.CharField(max_length=50)),
                ('STATUS', models.CharField(max_length=50)),
                ('TX', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'agg',
            },
        ),
        migrations.CreateModel(
            name='Origen_FO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TXGRUPOS', models.CharField(max_length=255)),
                ('TXDETALLE', models.CharField(max_length=255)),
                ('CONTROL', models.CharField(max_length=255)),
                ('FECHA', models.DateField(max_length=10)),
                ('POC', models.CharField(max_length=255)),
                ('OBSERVACIONES', models.CharField(max_length=255)),
                ('ID', models.CharField(max_length=255)),
                ('IDATT', models.CharField(max_length=255)),
                ('NOMBRE', models.CharField(max_length=255)),
                ('LATITUD', models.CharField(max_length=255)),
                ('LONGITUD', models.CharField(max_length=255)),
                ('ESTADO', models.CharField(max_length=255)),
                ('MUNICIPIO', models.CharField(max_length=255)),
                ('MERCADO', models.CharField(max_length=255)),
                ('MERCADOFO', models.CharField(max_length=255)),
                ('REGIONCELULAR', models.CharField(max_length=255)),
                ('AGREGADOR', models.CharField(max_length=255)),
                ('AÑO', models.CharField(max_length=255)),
                ('PROYECTO', models.CharField(max_length=255)),
                ('TOPOLOGIA', models.CharField(max_length=255)),
                ('SEGMENTOIPBH', models.CharField(max_length=255)),
                ('STATUS', models.CharField(max_length=255)),
                ('TX', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'fibraoptica',
            },
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ATT', models.CharField(max_length=50)),
                ('Proyección', models.CharField(max_length=50)),
                ('TX_Grupos_Proyeccion', models.CharField(max_length=50)),
                ('TX_Detalle_Proyecccion', models.CharField(max_length=50)),
                ('Control_Fecha', models.CharField(max_length=50)),
                ('POC', models.CharField(max_length=50)),
                ('Observaciones', models.CharField(max_length=50)),
                ('ID_DOS', models.CharField(max_length=50)),
                ('ID_ATandT', models.CharField(max_length=50)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('LATITUD', models.CharField(max_length=50)),
                ('LONGITUD', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=50)),
                ('Municipio', models.CharField(max_length=50)),
                ('Mercado', models.CharField(max_length=50)),
                ('Mercado_FO', models.CharField(max_length=50)),
                ('Region_Celular', models.CharField(max_length=50)),
                ('AGREGADOR', models.CharField(max_length=50)),
                ('AÑO', models.CharField(max_length=4)),
                ('PROYECTO', models.CharField(max_length=50)),
                ('TOPOLOGÍA', models.CharField(max_length=50)),
                ('SEGMENTO_IPBH', models.CharField(max_length=50)),
                ('status_anterior', models.CharField(max_length=50)),
                ('status_actual', models.CharField(max_length=50)),
                ('Control_de_cambios_RAN', models.CharField(max_length=50)),
                ('Master', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'proyeccion',
            },
        ),
        migrations.CreateModel(
            name='SitiosTotales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TRACKER', models.CharField(max_length=50)),
                ('ATTID', models.CharField(max_length=50)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('IDLTE', models.CharField(max_length=50)),
                ('IDROJO', models.CharField(max_length=50)),
                ('IDNARANJA', models.CharField(max_length=50)),
                ('IDEN', models.CharField(max_length=50)),
                ('LATITUD', models.CharField(max_length=50)),
                ('LONGITUD', models.CharField(max_length=50)),
                ('ESTADO', models.CharField(max_length=50)),
                ('MUNICIPIO', models.CharField(max_length=50)),
                ('MERCADO', models.CharField(max_length=50)),
                ('REGIONCELULAR', models.CharField(max_length=50)),
                ('REGION', models.CharField(max_length=50)),
                ('VENDOR', models.CharField(max_length=50)),
                ('COBERTURA', models.CharField(max_length=50)),
                ('TIPO', models.CharField(max_length=50)),
                ('PROYECTO', models.CharField(max_length=50)),
                ('CLASIFICACION', models.CharField(max_length=50)),
                ('CONFIGURACION3G', models.CharField(max_length=50)),
                ('CONFIGURACIONLTE', models.CharField(max_length=50)),
                ('CONFIGURACION5G', models.CharField(max_length=50)),
                ('IOT', models.CharField(max_length=50)),
                ('TDD', models.CharField(max_length=50)),
                ('TRAFICO3GLTE5G', models.CharField(max_length=50)),
                ('TRAFICO3G', models.CharField(max_length=50)),
                ('TRAFICO4G', models.CharField(max_length=50)),
                ('TRAFICO5G', models.CharField(max_length=50)),
                ('SL', models.CharField(max_length=50)),
                ('CONSOLIDADO', models.CharField(max_length=50)),
                ('REUBICACION', models.CharField(max_length=50)),
                ('NOTAS', models.CharField(max_length=50)),
                ('COMENTARIOOPERACIONES', models.CharField(max_length=50)),
                ('PLAN', models.CharField(max_length=50)),
                ('B26_800', models.CharField(max_length=50)),
                ('B5_850', models.CharField(max_length=50)),
                ('B2_PCS', models.CharField(max_length=50)),
                ('B4_AWS', models.CharField(max_length=50)),
                ('B7_2600', models.CharField(max_length=50)),
                ('B38_2600', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'sitiostotales',
            },
        ),
    ]
