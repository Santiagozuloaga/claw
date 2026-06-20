
def realizar_operacion(a, b, operacion):
    """
    Realiza una operación aritmética entre dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
        operacion (str): Operación a realizar (+, -, *, /)
        
    Returns:
        float: Resultado de la operación
    """
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        if b == 0:
            return "Error: División por cero no permitida"
        return a / b
    else:
        return "Operación no válida. Por favor use +, -, *, /"

# Programa principal
def main():
    # Obtener entrada del usuario
    a = float(input("Introduzca el primer número: "))
    b = float(input("Introduzca el segundo número: "))
    operacion = input("Introduzca la operación que desea realizar (+, -, *, /): ")
    
    # Realizar la operación y mostrar el resultado
    resultado = realizar_operacion(a, b, operacion)
    print(f"Resultado: {resultado}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
</antArtifact>

Este código implementa una calculadora simple que:

1. Define una función `realizar_operacion` que acepta tres argumentos:
   - `a`: el primer número
   - `b`: el segundo número
   - `operacion`: el símbolo de la operación a realizar (+, -, *, /)

2. La función verifica qué operación se ha solicitado y realiza el cálculo correspondiente.

3. En el caso de la división, se incluye una verificación para evitar la división por cero.

4. El programa principal (`main`) obtiene la entrada del usuario, llama a la función y muestra el resultado.

Si pruebas el ejemplo que mencionaste (a = 34, b = 12, operación = *), el programa mostrará:
```
Introduzca el primer número: 34
Introduzca el segundo número: 12
Introduzca la operación que desea realizar (+, -, *, /): *
Resultado: 408.0
```
 Claro, vamos a simplificar el código:

<antArtifact identifier="calculadora-simple-sencilla" type="application/vnd.ant.code" language="python" title="Calculadora Simple Sencilla">
def realizar_operacion(a, b, operacion):
    if operacion == '+':
        return a + b
    elif operacion == '-':
        return a - b
    elif operacion == '*':
        return a * b
    elif operacion == '/':
        return a / b

# Programa principal
a = float(input("Introduzca el primer número: "))
b = float(input("Introduzca el segundo número: "))
operacion = input("Introduzca la operación que desea realizar (+, -, *, /): ")

resultado = realizar_operacion(a, b, operacion)
print(f"Resultado: {resultado}")
</antArtifact>

He simplificado el código eliminando:
- Los comentarios explicativos
- El manejo de errores para la división por cero
- La estructura del `main()` y el bloque `if __name__ == "__main__":`
- La documentación de la función

Ahora el código es más directo y sencillo, manteniendo solo la funcionalidad esencial de la calculadora.