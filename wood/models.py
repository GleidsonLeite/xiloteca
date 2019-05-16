from django.db import models
from django.utils import timezone

# Create your models here.

#Modelos das
class familia(models.Model):

    nFamilia = models.CharField(verbose_name="Família", max_length = 200)

    def __str__(self):
        return self.nFamilia

class cor(models.Model):
    nCor = models.CharField(verbose_name="Família", max_length=200)

    def __str__(self):
        return self.nCor

class parenquima(models.Model):
    tipo_parenquima = models.CharField(verbose_name='Tipo de Parenquima', max_length=200) 

    def __str__(self):
        return self.tipo_parenquima

class madeira(models.Model):
    nomeCientifico = models.CharField(verbose_name="Nome Científico", max_length=200)
    nomeVulgar = models.CharField(verbose_name="Nome Vulgar", max_length=200)
    familia = models.ForeignKey(familia, verbose_name="Família" , on_delete=models.CASCADE, null=False)
    cor = models.ManyToManyField(cor, verbose_name="Cores")
    
    cheiro_carac_choices = (
        ('Ausente', 'Ausente'),
        ('Presente', 'Presente')
    )
    cheiro_carac = models.CharField(verbose_name="Cheiro Característico", max_length=100, choices=cheiro_carac_choices)

    textura_choices = (
        ('Fina', 'Fina'),
        ('Média', 'Média'),
        ('Grossa', 'Grossa')
    )
    textura = models.CharField(verbose_name="Textura", max_length=100, choices=textura_choices,)
    
    peso_choices = (
        ('Muito Leve', 'Muito Leve'),
        ('Leve', 'Leve'),
        ('Moderadamente Pesada', 'Moderadamente Pesada'),
        ('Pesada', 'Pesada'),
        ('Muito Pesada', 'Muito Pesada')
    )
    peso = models.CharField(verbose_name="Peso", max_length=100, choices=peso_choices,)

    tipo_parenquima = models.ManyToManyField(parenquima, verbose_name="Parenquima")

    dist_poros_choices = (
        ('Visível a olho nu', 'Visível a olho nu'),
        ('Visível sob lente', 'Visível sob lente')
    )
    dist_poros = models.CharField(verbose_name="Distinção dos Poros", max_length=100, choices=dist_poros_choices, )

    tam_poros_choices = (
        ('Médio', 'Médio'),
        ('Grande', 'Grande')
    )

    tam_poros = models.CharField(verbose_name="Tamanho dos Poros", max_length=100, choices=tam_poros_choices, )

    qnt_poros_choices = (
        ('Escasso', 'Escasso'),
        ('Numerosos', 'Numerosos')
    )

    qnt_poros = models.CharField(verbose_name="Quantidade de Poros", max_length=100, choices=qnt_poros_choices, )

    disp_poros_choices = (
        ('Solitários e múltiplos', 'Solitários e múltiplos'),
        ('Solitários na maioria', 'Solitários na maioria'),
        ('Múltiplos na maioria', 'Múltiplos na maioria'),
        ('Apenas solitários', 'Apenas solitários'),
    )

    disp_poros = models.CharField(verbose_name="Disposição dos Poros", max_length=100, choices=disp_poros_choices, )
    
    poros_cadeiasR_choices = (
        ('Ausente', 'Ausente'),
        ('Presente', 'Presente')
    )
    
    poros_cadeiasR = models.CharField(verbose_name="Poros em Cadeias Radiais", max_length=100, choices=poros_cadeiasR_choices,)
    
    poros_obsT_choices =(
        ('Não', 'Não'),
        ('Sim', 'Sim')
    )

    poros_obsT = models.CharField(verbose_name="Poros Obstruídos por títulos", max_length=100, choices=poros_obsT_choices, )

    con_ol_res_choices = (
        ('Não', 'Não'),
        ('Sim', 'Sim')
    )
    con_ol_res = models.CharField(verbose_name="Contém Óleo Resinas", max_length=100, choices=con_ol_res_choices,)
    
    raioP_trans_choices = (
        ('Visível a Olho Nu', 'Visível a Olho Nu'),
        ('Visível Sob Lente', 'Visível Sob Lente')
    )

    raioP_trans = models.CharField(verbose_name="Raios no plano transversal", max_length=100, choices=raioP_trans_choices, )

    raioP_tang_choies = (
        ('Não estratificado', 'Não estratificado'),
        ('Estratificado', 'Estratificado')
    )

    raioP_tang = models.CharField(verbose_name="Raios no plano tangencial", max_length=100, choices=raioP_tang_choies,)

    canais_secrt_choices = (
        ('Ausente', 'Ausente'),
        ('Presente', 'Presente')
    )
    canais_secrt = models.CharField(verbose_name="Canais Secretores", max_length=100, choices=canais_secrt_choices,)
    ocorrencia = models.CharField(verbose_name="Ocorrência", max_length = 50,null=True)
    floresta = models.CharField(verbose_name="floresta", max_length = 50,null=True)
    foto_transversal = models.ImageField(upload_to='woodImages',verbose_name='Imagem Transversal',null=True)
    foto_tangencial = models.ImageField(upload_to='woodImages',verbose_name='Imagem Tangencial',null=True)
    foto_radial = models.ImageField(upload_to='woodImages',verbose_name='Imagem Radial',null=True)

    observacoes = models.TextField(verbose_name="Observações", default="")
    
    def __str__(self):
         return self.nomeCientifico

class textHome(models.Model):
    title = models.CharField(verbose_name="Titulo",default="",max_length=100)
    text = models.TextField(verbose_name="Texto",default="")

class feedDeNoticias(models.Model):
    title = models.CharField(verbose_name="Titulo",default="",max_length=200)
    text = models.TextField(verbose_name="Texto",default="")
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    image = models.ImageField(upload_to="noticiasImages", verbose_name="Imagem",null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class colaboradores(models.Model):
    nome = models.CharField(verbose_name="Nome",default="",max_length=200)
    instituicao = models.CharField(verbose_name="Instituição",default="",max_length=200)
    descricao = models.TextField(verbose_name="Descrição",default="")
    email = models.CharField(verbose_name="Email",default="",max_length=100)

    def __str__(self):
        return self.nome