# Generador CSV: Verbos Franceses con Cloze

Genera un archivo CSV para practicar conjugaciones de verbos en francés usando el método cloze.

## Formato requerido:
```csv
text_cloze,translation,notes
Je {{c1::parle}} français,Yo hablo francés,parler - je - presente - /paʁl/
Tu {{c1::parles}} espagnol,Tú hablas español,parler - tu - presente - /paʁl/
```

## Campos obligatorios:
- **text_cloze**: Frase en francés con el verbo oculto usando `{{c1::verbo}}`
- **translation**: Traducción completa al español
- **notes**: Formato: `infinitivo - sujeto - tiempo - IPA`

## Reglas de cloze:
1. **Siempre** usar `{{c1::verbo_conjugado}}`
2. **Un solo hueco** por frase (el verbo conjugado)
3. **Frase completa y natural**
4. **6 filas por verbo** (una para cada sujeto: je, tu, il/elle, nous, vous, ils/elles)

## Formato de notes:
`infinitivo - sujeto - tiempo_verbal - /IPA/`

Ejemplos:
- `parler - je - presente - /paʁl/`
- `être - tu - presente - /ɛ/`
- `avoir - nous - presente - /avɔ̃/`

## Requisitos técnicos:
✅ Header exacto: `text_cloze,translation,notes`

✅ Usar comillas para frases con comas: `"Je mange, donc je suis"`

✅ IPA del verbo conjugado (no de toda la frase)

✅ UTF-8 encoding

✅ Formato CSV puro

---

**MI REQUEST**:
- Verbo(s): [parler / être / avoir / manger / etc]
- Tiempo: [presente / pasado / futuro]
- Sujetos: [todos / solo je,tu,il / etc]

Ejemplo: "Verbo 'parler' en presente, todos los sujetos"

**TU RESPUESTA**: Genera el CSV con 6 filas (una por sujeto) y dame el archivo descargable.