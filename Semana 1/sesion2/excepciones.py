try:
 numero = int(input("Ingresar un numero"))
 numero/0
except ValueError :
  print('Tiene que se un numero')
except ZeroDivisionError:
    print('No se puede hacer la division entre cero')
except:
  print('huno un error')
else:
  print('todo fue bien')
finally:
  print('Yo siempre me ejecuto') 
  print('yo soy otra linea de codigo') 
