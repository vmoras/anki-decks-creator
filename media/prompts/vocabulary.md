# Generador CSV: Vocabulario Francés

Genera un archivo CSV para aprender vocabulario francés (español → francés) con flashcards.

## Formato requerido:

```csv
create_img,img_name,word_spanish,word_french,audio_script,audio_ipa,notes
```

## Campos:

- **create_img**: `true` si la palabra es concreta/visual y se beneficia de una imagen (ej: objetos, animales, comida, ropa, lugares). `false` si es abstracta, un conector, adverbio, o no tiene representación visual clara (ej: "sin embargo", "aunque", "rápidamente").
- **img_name**: Si `create_img` es `true`, la palabra traducida al inglés (ej: `dog`, `potato`, `red dress`). Si `create_img` es `false`, dejar como string vacío `""`.
- **word_spanish**: Palabra en español. Ejemplo: `gato`
- **word_french**: Palabra en francés con TODOS los determinantes que apliquen. Incluir artículo definido + partitivo/indefinido si corresponde. Ejemplos:
  - `le chat` (solo definido)
  - `le pain / du pain` (definido + partitivo)
  - `la viande / de la viande` (definido + partitivo)
  - `l'eau (f) / de l'eau` (definido con género explícito + partitivo)
- **audio_script**: La palabra con su determinante principal. Ejemplo: `le pain`, `la viande`, `l'eau`
- **audio_ipa**: Transcripción IPA de audio_script. Ejemplo: `/lə pɛ̃/`, `/la vjɑ̃d/`, `/lo/`
- **notes**: Información adicional útil. Incluir:
  - Género (m/f) — obligatorio cuando el artículo tiene género.
  - Falsos amigos o confusiones con español (ej: "la robe ≠ roba, significa vestido")
  - Expresiones comunes donde aparece la palabra
  - Plurales irregulares si aplica
  - Dejar como string vacío `""` si no hay nada relevante que agregar

## Reglas:

1. Marcar `create_img` como `true` para sustantivos concretos, objetos físicos, animales, comida, ropa, lugares visuales. Marcar como `false` para palabras abstractas, conectores, adverbios, verbos sin representación visual clara, y adjetivos genéricos.
2. En `img_name`, usar la traducción al inglés de la palabra (no del francés, sino del concepto). Usar minúsculas. Si es una expresión de varias palabras, separar con espacios (ej: `red dress`).
3. En `word_french`, SIEMPRE incluir el artículo definido (le/la/l'/les) para sustantivos. Si aplica partitivo o indefinido, agregarlo separado con ` / `.
4. En `audio_script`, poner solo la palabra con su determinante principal (ej: `le pain`, no una frase).
5. En `audio_ipa`, transcribir exactamente lo que está en `audio_script`.

## Requisitos técnicos:

- Header exacto: `create_img,img_name,word_spanish,word_french,audio_script,audio_ipa,notes`
- Usar comillas para campos con comas o caracteres especiales
- UTF-8 encoding
- Formato CSV puro

---

## MI REQUEST:

- **Opción A — Lista de palabras**: [lista de palabras en español o francés]
- **Opción B — Tema + cantidad**: [tema] + [número de palabras]

Ejemplos:
- "20 palabras sobre comida"
- "15 palabras: conectores y transiciones"
- "gato, perro, pájaro, pez, tortuga"
- "10 palabras sobre ropa"

## TU RESPUESTA:

Genera el CSV y dame el archivo descargable.
