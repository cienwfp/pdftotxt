#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Created on Jul 2021.
@author: Wanderson Neto
"""

import os

from convert import convert
    
def inicio():

    print('###################')
    print('  ##############')
    print('    ##########')
    print('      #####')
    print('        #')
    print('      #####')
    print('    ##########')
    print('  ##############')
    print('###################')
    print('Bem-vindo ao programa para converter arquivos pdf para txt')

    file = input('Entre com o caminho do arquivo .pdf para a conversão')

    file = '/media/dgbe/HD/appPdfTotxt/pdftotxt/entrada/MODELO DE PROJETO ACADEPOL.pdf'
    
    head, tail = os.path.split(file)

    text = convert.pdf(file)

    with open('result/' + tail + '.txt', 'w') as f:
        f.write(text)
