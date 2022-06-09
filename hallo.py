#!/usr/bin/python3 
"""
hello world program muitple linguagens

"""
__version__ = "0.0.1" 
__author__ = "Rubem Carvalho"

import os   

current_lenguage = os.getenv("LANG", "en_US")[:5]

msg = "Hello World!"

if current_lenguage == "pt_BR":
    msg = "Olá Mundo!"
elif current_lenguage == "it_IT":
    msg = "Ciao Mondo!"
elif current_lenguage == "fr_FR":
    msg = "Bonjour Monde!"
elif current_lenguage == "es_ES":
    msg = "Hola Mundo!"   


print(msg)
print('rubem'.upper()) # RUBEM
