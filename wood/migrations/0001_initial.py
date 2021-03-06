# Generated by Django 2.1.1 on 2019-03-17 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nCor', models.CharField(max_length=200, verbose_name='Família')),
            ],
        ),
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nFamilia', models.CharField(max_length=200, verbose_name='Família')),
            ],
        ),
        migrations.CreateModel(
            name='madeira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCientifico', models.CharField(max_length=200, verbose_name='Nome Científico')),
                ('nomeVulgar', models.CharField(max_length=200, verbose_name='Nome Vulgar')),
                ('cheiro_carac', models.CharField(choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=100, verbose_name='Cheiro Característico')),
                ('textura', models.CharField(choices=[('Fina', 'Fina'), ('Média', 'Média'), ('Grossa', 'Grossa')], max_length=100, verbose_name='Textura')),
                ('peso', models.CharField(choices=[('Muito Leve', 'Muito Leve'), ('Leve', 'Leve'), ('Moderadamente Pesada', 'Moderadamente Pesada'), ('Pesada', 'Pesada'), ('Muito Pesada', 'Muito Pesada')], max_length=100, verbose_name='Peso')),
                ('dist_poros', models.CharField(choices=[('Visível a olho nu', 'Visível a olho nu'), ('Visível sob lente', 'Visível sob lente')], max_length=100, verbose_name='Distinção dos Poros')),
                ('tam_poros', models.CharField(choices=[('Médio', 'Médio'), ('Grande', 'Grande')], max_length=100, verbose_name='Tamanho dos Poros')),
                ('qnt_poros', models.CharField(choices=[('Escasso', 'Escasso'), ('Numerosos', 'Numerosos')], max_length=100, verbose_name='Quantidade de Poros')),
                ('disp_poros', models.CharField(choices=[('Solitários e múltiplos', 'Solitários e múltiplos'), ('Solitários na maioria', 'Solitários na maioria'), ('Múltiplos na maioria', 'Múltiplos na maioria'), ('Apenas solitários', 'Apenas solitários')], max_length=100, verbose_name='Disposição dos Poros')),
                ('poros_cadeiasR', models.CharField(choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=100, verbose_name='Poros em Cadeias Radiais')),
                ('poros_obsT', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=100, verbose_name='Poros Obstruídos por títulos')),
                ('con_ol_res', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=100, verbose_name='Contém Óleo Resinas')),
                ('raioP_trans', models.CharField(choices=[('Visível a Olho Nu', 'Visível a Olho Nu'), ('Visível Sob Lente', 'Visível Sob Lente')], max_length=100, verbose_name='Raios no plano transversal')),
                ('raioP_tang', models.CharField(choices=[('Não estratificado', 'Não estratificado'), ('Estratificado', 'Estratificado')], max_length=100, verbose_name='Raios no plano tangencial')),
                ('canais_secrt', models.CharField(choices=[('Ausente', 'Ausente'), ('Presente', 'Presente')], max_length=100, verbose_name='Canais Secretores')),
                ('ocorrencia', models.CharField(max_length=50, null=True, verbose_name='Ocorrência')),
                ('floresta', models.CharField(max_length=50, null=True, verbose_name='floresta')),
                ('foto_transversal', models.ImageField(null=True, upload_to='woodImages', verbose_name='Imagem Transversal')),
                ('foto_tangencial', models.ImageField(null=True, upload_to='woodImages', verbose_name='Imagem Tangencial')),
                ('foto_radial', models.ImageField(null=True, upload_to='woodImages', verbose_name='Imagem Radial')),
                ('observacoes', models.TextField(null=True, verbose_name='Observações')),
                ('cor', models.ManyToManyField(to='wood.cor', verbose_name='Cores')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wood.familia', verbose_name='Família')),
            ],
        ),
        migrations.CreateModel(
            name='parenquima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_parenquima', models.CharField(max_length=200, verbose_name='Tipo de Parenquima')),
            ],
        ),
        migrations.AddField(
            model_name='madeira',
            name='tipo_parenquima',
            field=models.ManyToManyField(to='wood.parenquima', verbose_name='Parenquima'),
        ),
    ]
