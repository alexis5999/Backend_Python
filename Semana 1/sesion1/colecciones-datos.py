#Listas
meses = ['Enero', 'Febrero', 'Marzo','Abril','Mayo']
#print(meses[3])

# Si usamos posiciones negativas contará de atraz hacia adelante 
#print(meses[-4])

# para traer elementos con limites, el primero indica donde y el segundo hasta que se 
#menor
#print(meses[0:1])
# Para agregar elementos a la lista
#meses.append(['Junio','Julio'])
#print(meses[-1][1])

#para poder quitar elemento de la lista
#meses.remove('Febrero')
#meses.remove('Marzo')
#print(meses)
#para limpiar toda lista
#meses.clear()

#print(meses)
#tuplas
#colecciones de datos ordenadas no se pueden modificar
datos_sensibles= (42694686, 'Jose', 42694686, 42694686, 42694686)
#print(datos_sensibles[2])
#para ver cuantos valores repetidos tenemos en la tupla
#print(datos_sensibles.count(42694686))

#Diccionarios
#colleccion de elementos que estan indexados, no estan ordenados y se modificar sus
#valores. Esta conformado por una clave -valor
persona = {
 'id':42694857,
 'nomb_per':'Jose',
 'fec_nac':'2000-02-12',
 'sex_per': 'M',
 'tipo_per': {
     'tipo_id':1,
     'tipo_desc':'Empleado'
      }

}

# Para ver el valor de la clave en especifico
print(persona['sex_per'])
print(persona['fec_nac' ])
