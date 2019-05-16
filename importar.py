import xlrd
import os
from wood.models import familia, cor, madeira, parenquima
from django.core.files import File

def addCores(objeto,lista):
    for i in lista:
        objeto.cor.add(i)

def addParenquima(objeto,lista):
    for i in lista:
        objeto.tipo_parenquima.add(i)

def createCor(lista):
    for i in lista:
        cores = cor.objects.filter(nCor=i)
        if len(cores)==0:
            cor.objects.create(nCor=i)

def createParenquima(lista):
    for i in lista:
        parenquimas = parenquima.objects.filter(tipo_parenquima=i)
        if len(parenquimas)==0:
            parenquima.objects.create(tipo_parenquima=i)




file = 'Software madeira.xlsx'
book = xlrd.open_workbook(file)
first_sheet = book.sheet_by_index(0)

for i in range(1,first_sheet.nrows):
    nc = '{}'.format(first_sheet.cell_value(i,0))#Nome Cientifico
    nv = '{}'.format(first_sheet.cell_value(i,1))#Nome Vulgar
    f = '{}'.format(first_sheet.cell_value(i,2))#Familia
    c = '{}'.format(first_sheet.cell_value(i,3)).split(',')#cor
    cc = '{}'.format(first_sheet.cell_value(i,4))#Cheiro Característico
    t = '{}'.format(first_sheet.cell_value(i,5))#Textura
    p = '{}'.format(first_sheet.cell_value(i,6))#Peso
    par = '{}'.format(first_sheet.cell_value(i,7))#Parenquima
    tPar = '{}'.format(first_sheet.cell_value(i,8)).split(',')#Tipo de parenquima
    dPo = '{}'.format(first_sheet.cell_value(i,9))#Distinção dos póros
    tPo = '{}'.format(first_sheet.cell_value(i,10))#Tamanho dos Poros
    qPo = '{}'.format(first_sheet.cell_value(i,11))#Quantidade dos poros
    disPo = '{}'.format(first_sheet.cell_value(i,12))#Disposição dos poros
    poCR = '{}'.format(first_sheet.cell_value(i,13))#Poros em cadeias radiais
    poOT = '{}'.format(first_sheet.cell_value(i,14))#Poros obstruidos por tilos
    cOR = '{}'.format(first_sheet.cell_value(i,15))#Contém óleo resinas
    rPT = '{}'.format(first_sheet.cell_value(i,16))#Raios no plano transversal
    rPTang = '{}'.format(first_sheet.cell_value(i,17))#Raios no plano tangencial
    cs = '{}'.format(first_sheet.cell_value(i,18))#Canais secretores
    oco = '{}'.format(first_sheet.cell_value(i,19))#Ocorrência
    fl = '{}'.format(first_sheet.cell_value(i,19))#Floresta
    familias = familia.objects.filter(nFamilia=f)
    if len(familias)==0:
        familia.objects.create(nFamilia=f)
    createCor(c)
    cores = cor.objects.filter(nCor__in=c)
    tPar.append(par)
    createParenquima(tPar)
    parenquimas = parenquima.objects.filter(tipo_parenquima__in=tPar)
    madeiras = madeira.objects.create(
        nomeCientifico = nc,
        nomeVulgar = nv,
        familia = familia.objects.filter(nFamilia=f)[0],
        cheiro_carac = cc,
        textura = t,
        peso = p,
        dist_poros = dPo,
        tam_poros = tPo,
        qnt_poros = qPo,
        disp_poros = disPo,
        poros_cadeiasR = poCR,
        poros_obsT = poOT,
        con_ol_res = cOR,
        raioP_trans = rPT,
        raioP_tang = rPTang,
        canais_secrt = cs,
        ocorrencia = oco,
        floresta = fl,
    )
    addCores(madeiras,cores)
    addParenquima(madeiras,parenquimas)


