# -*- coding: UTF-8 -*-

import os
import commands
from folders import NamesFolders
from transfer import TransfersFolders
import inspect

a = inspect.getmembers(NamesFolders,predicate=inspect.ismethod)


print(type(a))
print(type(a[0]))
print(a)

diretorios = NamesFolders()
nome_do_diretorio = diretorios.names()

print(nome_do_diretorio)

transferencia = TransfersFolders()
transferencia.transfers(nome_do_diretorio)



#folder = TransfersFolders.names()
#print(folder)

#var = commands.getoutput("ifconfig")

#print(var)



#scp __init__.py arthuralves@domain:/arquivo-remoto.txt


'''
Copiando um arquivo remoto para máquina local:
scp user@domain:/pasta-remota/arquivo-remoto.txt /pasta-local/arquivo-local.txt

Enviando um arquivo local para um servidor remoto:
scp /pasta-local/arquivo-local.txt user@domain:/pasta-remota/arquivo-remoto.txt

Copiando pastas e subpastas do servidor remoto para máquina local:
scp -r user@domain:/pasta-remota/ /pasta-local/

Enviando pastas e subpastas da máquina local para o servidor remoto:
scp -r /pasta-local/ user@domain:/pasta-remota/

'''