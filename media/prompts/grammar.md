# Generador CSV: Gramática Francesa

Genera un archivo CSV para practicar gramática francesa con flashcards. El flujo de estudio es: ver la carta → producir la respuesta en francés → evaluar con un LLM.

## Formato requerido:

```csv
topic,description,instruction
```

## Campos:

- **topic**: Nombre del tema gramatical en español. Debe ser claro y específico para identificar el tema de un vistazo. Si el tema es amplio, especificar el subtema. Ejemplos: `Adjetivos posesivos — je`, `Il y a`, `Preposiciones de tiempo`, `Conectores de causa`.
- **description**: Explicación breve en español de qué es el tema, usando equivalentes en español para que el estudiante entienda de qué se trata sin necesidad de conocimiento previo. Debe:
  - Explicar el concepto en términos simples con su equivalente en español.
  - Dar un ejemplo en español que ilustre el uso.
  - NO incluir las formas correctas en francés.
  - Ejemplos:
    - Para `Adjetivos demostrativos`: `Palabras que señalan algo específico. En español: este, esta, estos, estas.`
    - Para `Il y a`: `Equivalente a 'hay' en español. Se usa para indicar existencia. Ej: 'Hay un gato en la mesa'.`
    - Para `Conectores de causa`: `Palabras que explican la razón de algo. En español: porque, ya que, puesto que, como.`
  - Reglas de la descripción:
    - Siempre en español
    - Máximo 2 frases
    - Dar el equivalente en español del concepto
    - No revelar las formas en francés
- **instruction**: Instrucción en español que le dice al estudiante qué debe producir o practicar. Debe ser una tarea concreta y accionable que se pueda evaluar con un LLM. La instrucción debe:
  - Indicar claramente qué se espera que el estudiante escriba en francés.
  - Incluir una frase de ejemplo en español para traducir cuando el tema lo requiera.
  - Ser lo suficientemente específica para que el LLM pueda evaluar la respuesta.
  - NO incluir las respuestas, formas correctas, ni pistas entre paréntesis. El estudiante debe producir todo de memoria.
  - Ejemplos:
    - `Escribe los adjetivos posesivos para 'yo' (masculino singular, femenino singular, plural) y usa cada uno en una frase.`
    - `Traduce usando 'il y a': 'Hay tres gatos en el jardín' y 'Hay mucho ruido aquí'.`
    - `Escribe 3 frases usando conectores de causa distintos.`
  - Reglas de la instrucción:
    - Siempre en español
    - Debe pedir producción en francés (escribir, traducir, conjugar, construir frases)
    - NUNCA revelar las formas/palabras correctas en francés dentro de la instrucción
    - Puede indicar cuántas formas se esperan (ej: "masculino singular, femenino singular, plural") sin dar la respuesta
    - Si el tema es contextual (como preposiciones o conectores), pedir traducciones o construcción de frases específicas

## Reglas:

1. **Dividir temas amplios en subtemas enfocados.** Si un tema tiene variantes por sujeto, género, o categoría, crear una carta por cada subtema. Ejemplos:
   - Adjetivos posesivos → una carta por sujeto (je, tu, il/elle, nous, vous, ils/elles)
   - Artículos → una carta por tipo (definidos, indefinidos, partitivos, contractos)
   - Conectores → una carta por función (causa, consecuencia, oposición, etc.)
2. La instrucción debe ser autocontenida: al leerla, el estudiante sabe exactamente qué hacer sin necesitar información adicional.
3. No dar respuestas ni pistas en la instrucción ni en la descripción. El ejercicio es de producción pura desde memoria.
4. Adaptar el tipo de ejercicio al tema:
   - **Temas con formas finitas** (determinantes, artículos, conjugaciones): Pedir que listen las formas del subtema específico y escriban un ejemplo con cada una.
   - **Temas contextuales** (preposiciones, conectores): Dar frases en español para traducir o pedir que construyan frases.
   - **Temas estructurales** (il y a, c'est, futur proche): Pedir que expliquen cuándo se usa + producir frases de ejemplo.

## Requisitos técnicos:

- Header exacto: `topic,description,instruction`
- Usar comillas para campos con comas o caracteres especiales
- UTF-8 encoding
- Formato CSV puro

---

## MI REQUEST:

Lista de temas gramaticales a convertir en cartas.

Ejemplos:
- "adjetivos posesivos, adjetivos demostrativos, artículos partitivos"
- "todas las preposiciones"
- "conectores: causa, consecuencia, oposición"
- "il y a, c'est, on, futur proche, impératif"

## TU RESPUESTA:

Genera el CSV y dame el archivo descargable.