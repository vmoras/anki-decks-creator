# Generador CSV: Verbos Franceses - Conjugación Completa

Genera un archivo CSV para practicar conjugaciones completas de verbos en francés. Cada fila es UN verbo con TODA su conjugación.

## Formato requerido:

```csv
verb_spanish,conjugation,notes,audio_script
```

## Campos obligatorios:

- **verb_spanish**: Verbo en español (infinitivo). Ejemplo: `comer`
- **conjugation**: Conjugación completa, cada sujeto en línea nueva usando `<br>`. Formato:
  ```
  manger<br>je mange<br>tu manges<br>il/elle mange<br>nous mangeons<br>vous mangez<br>ils/elles mangent
  ```
- **notes**: Información útil sobre el verbo. Incluir:
  - Preposiciones que cambian el significado (ej: "mettre = poner | se mettre à = ponerse a hacer algo")
  - Preposiciones obligatorias a usar con dicho verso (si existe)
  - Irregularidades importantes
  - Usos idiomáticos frecuentes
  - Confusiones comunes con español (falsos amigos)
  - Grupo verbal (-er, -ir, -re, irregular)
- **audio_script**: SOLO las formas que suenan diferente entre sí, con su pronombre. Separadas por punto y coma. Ejemplo para un verbo regular -er: `je mange; nous mangeons; vous mangez` (porque je/tu/il/ils suenan igual, solo cambian nous y vous). Para un verbo como être donde casi todas suenan distinto: `je suis; tu es; il est; nous sommes; vous êtes; ils sont`

## Reglas:

1. **Una fila por verbo** con la conjugación completa de los 6 sujetos
2. **Siempre presente** (salvo que se indique otro tiempo)
3. **audio_script** debe incluir el pronombre pegado al verbo (como suena en habla real)
4. Para verbos reflexivos, incluir el pronombre reflexivo: `je me lève<br>tu te lèves<br>...`
5. En notes, ser conciso pero útil. No repetir la conjugación.

## Requisitos técnicos:

- Header exacto: `verb_spanish,conjugation,notes,audio_script`
- Usar comillas para campos con comas o `<br>`: `"je mange<br>tu manges<br>..."`
- UTF-8 encoding
- Formato CSV puro

---

**MI REQUEST**:

- Verbo(s): [lista de verbos en francés]
- Tiempo: [presente / passé composé / etc] (default: presente)

**TU RESPUESTA**: Genera el CSV con una fila por verbo y dame el archivo descargable.