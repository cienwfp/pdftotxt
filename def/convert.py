
#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Created on Jul 2021.
@author: Wanderson Neto
"""

import pdftotext

class convert():
    
    def pdf(file):
               
        with open (file, "rb") as f: 
            pdf = pdftotext.PDF (f)
        # Leia todo o texto em uma string 
        pdftotext_text = "\n\n" .join (pdf)

        return (pdftotext_text)