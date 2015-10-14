# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "MANUEL"
__date__ = "$14-oct-2015 10:03:02$"

#Contro del vacunas 

vacunas =  1000

while vacunas >= 200:
    pedidos = input ("cantidad de vacunas:")
    vacunas = vacunas - pedidos
    
print ("Las vacunas son menos de 200")    