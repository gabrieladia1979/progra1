"""TP04-02 | TEXTO CENTRADO EN PANTALLA
Leer una cadena de caracteres e imprimirla centrada rellenando a izquierda y
derecha con guiones para cubrir toda la pantalla.
Suponer que la pantalla tiene 80 columnas.
En el mismo programa hacer 3 versiones:

1- Una sin utilizar facilidades de Python,
2- Otra usando la facilidad de función o método incorporado,
3- Y otra usando la facilidad de f-strings."""

"1 - una sin utilizar facilidades de Python"
cad = "Hola"
total = 80
"2 - otra usando la facilidad de función o método incorporado"
cad = "Hola"
print(cad.center(80,"-"))
"3 - usando la facilidad de f-strings"
cad = "Hola"
print(f"{cad:-^80}")