# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "MANUEL"
__date__ = "$07-oct-2015 11:17:39$"
articulo = str(raw_input("Nombre del articulo:"))
clave = int(input("clave del articulo 01 o 02:"))
pre = int(input("precio:"))
num=1
if clave == num:
    des = pre-(pre*0.1)   
else: 
    descuento= precio-(precio*0.20)
    
print "nombre del articlo", articulo
print "la clave es", clave
print "Precio", pre
print "Precio con descuento", des