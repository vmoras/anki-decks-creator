# Generador CSV: Vocabulario Francés en Contexto

Genera un archivo CSV para aprender vocabulario francés con frases contextuales.

## Formato requerido:
```csv
text_es,text_fr,ipa,notes
yo/tener/gato,J'ai un chat,/ʃa/,chat (m) - sustantivo
grande/casa,La maison est grande,/lam(e)zõn‿ɛ gɾɑ̃də/,grand (adj) - variable según género,
yo/no/hablar/ingles,Je ne parle pas français,/ʒə nə paɾlə pa fɾanse/, '',
ellos/lavar/cada dia, Ils font la vaiselle tous les jours,/il fõ la vɛzɛlə tule ʒuɾ/,''
```

## Campos:
- **text_es**: Palabras español que den contexto de lo que se necesita
- **text_fr**: Frase completa en francés
- **ipa**: IPA de la frase en frances (no toda la frase)
- **notes**: Información adicional util no siempre necesaria

## Reglas importantes:
1**Contexto natural**: Frases que realmente dirías

## Formato de notes según tipo:
- Sustantivos: `palabra (m/f) - categoría` → ej: `chat (m) - animal`
- Adjetivos: `palabra (adj) - descripción` → ej: `grand (adj) - tamaño`
- Verbos: `infinitivo (verbo) - categoría` → ej: `manger (verbo) - acción`

## Requisitos técnicos:
✅ Header exacto: `text_es,text_fr,ipa,notes`

✅ Sin espacios extras

✅ UTF-8 encoding

✅ Frases con comillas si contienen comas

✅ Formato CSV puro

---

**MI REQUEST**: 
- Tema: [animales / comida / familia / ropa / etc]
- Cantidad: [10 / 20 / 30 palabras]
- Tipo: [sustantivos / adjetivos / verbos / mixto]

Ejemplo: "10 sustantivos sobre animales domésticos"

**TU RESPUESTA**: Genera el CSV y dame el archivo descargable.