##Sintaxis
## try
##      codigo
##      codigo 
##      ******
## except ExceptionName
##      cdigo
##      codigo
##      *****
dividendo = 100
while True:
    try:
        edad = int(input('Introduce tu edad: '))
        calculo = dividendo / edad
        print(f'El resultado es {calculo}')
        break
    except ValueError as error:         ## Solo con except, controla cualquier error(pero es mala practica)
        print('Debes introducir una edad válida.')
        #print(type(error))
        #print(error.args)
        #print(error)
    except ZeroDivisionError:
        print('Debes introducir una edad mayor a cero.')
    else:
        print('else se va ejecutar solo cuando no hayan errores')
    finally:
        print('finally se va ejecutar tanto hayan errores como no hayan errores')
        