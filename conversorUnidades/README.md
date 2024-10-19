>Ammy Zúñiga
# Conversor de Moneda USD a CRC

Esta es una aplicación gráfica simple construida con **Tkinter** que permite convertir dólares estadounidenses (USD) a colones costarricenses (CRC) utilizando una tasa de conversión fija. La aplicación tiene una interfaz intuitiva donde el usuario puede ingresar un valor en USD y obtener el equivalente en CRC.

## Características

- Conversión de USD a CRC con una tasa de conversión fija.
- Validación de la entrada para asegurar que solo se ingresen valores numéricos.
- Mensaje de error si el campo está vacío o el valor no es numérico.
- Funcionalidad para limpiar el campo de entrada y el resultado.
- Confirmación antes de cerrar la ventana.

## Instrucciones de Uso

1. Ingresa el valor en dólares (USD) en el campo de texto.
2. Haz clic en el botón "Convertir" para realizar la conversión.
3. El resultado en colones costarricenses (CRC) se mostrará debajo.
4. Si deseas limpiar el campo de entrada y el resultado, haz clic en el botón "Limpiar".
5. Para salir de la aplicación, haz clic en la "X" de la ventana y confirma tu elección.

## Tasa de Conversión

La tasa de conversión utilizada es: 513.70 colones

## Funcionalidades del Código

1. **convertir()**: Convierte el valor ingresado en USD a CRC utilizando una tasa fija y muestra el resultado.
2. **limpiar()**: Limpia el campo de entrada y restablece el valor del resultado a "0.00 CRC".
3. **salir()**: Cierra la ventana de la aplicación después de confirmar con el usuario.

## Imágenes
*Interfaz principal*

![Interfaz del conversor de moneda](.\Imagenes\VentanaConversor.png)

*Aviso de error*

![Interfaz del conversor de moneda](.\Imagenes\ValorNoValido.png)

*Verificación de salida*

![Interfaz del conversor de moneda](.\Imagenes\Salir.png)
