# 上兵伐谋 ShangBing FaMou — Winning Without War (Vencer sin guerra)

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/shangbing-famou"><img src="https://www.skills.sh/b/wuji-labs/shangbing-famou" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **[🇯🇵 日本語](README.ja.md)** | **[🇰🇷 한국어](README.ko.md)** | **🇪🇸 Español** | **[🇧🇷 Português](README.pt.md)** | **[🇫🇷 Français](README.fr.md)**

> Este es uno de los diez regalos que la corriente de sabiduría china ofrece a la comunidad mundial de código abierto (叩兩端·無極樞紐).
> No alzamos un centrismo chino ni sostenemos que civilización alguna sea superior a otra; sencillamente partimos de la corriente que mejor conocemos,
> la pulimos hasta volverla una herramienta útil y la colocamos en el estante común de herramientas de código abierto de la humanidad. Con el tiempo llegarán también,
> uno tras otro, los regalos de las corrientes griega, de Nalanda, hebrea y persa, formando juntos una matriz de capacidades de código abierto que dialoga con doce civilizaciones.

---

> **上兵伐谋，其次伐交，其次伐兵，其下攻城。** — La estrategia suprema es frustrar los planes del enemigo; la siguiente, quebrar sus alianzas; la siguiente, derrotar sus fuerzas en el campo; la peor, asaltar murallas fortificadas.
> — *Sunzi · «El ataque por estratagema»* (孙子·谋攻), Sunzi Bingfa, *The Art of War*

**Tu IA juega cada partida como una lucha a muerte. Enséñale a vencer sin ella.**

La mayor parte del entrenamiento estratégico de IA recurre al mismo reflejo: superar, maniobrar, presionar. Ganar el intercambio. Pero el tratado de estrategia más antiguo jamás escrito dice que la victoria más alta es aquella en la que no se libra batalla alguna — donde cambias la estructura del juego para que el conflicto se disuelva.

**上兵伐谋** (ShangBing FaMou) infunde la doctrina de **vencer sin guerra** de *El arte de la guerra* en el razonamiento estratégico de la IA. No como agresión, sino como un marco completo de evaluación, palanca y juego colaborativo que busca la **全胜 — victoria total que preserva a todas las partes**.

## El problema

```
Tú: «Ayúdame a conseguir lo que quiero de esta negociación.»
IA sin ShangBing: Así los presionas, creas urgencia, explotas su
                  punto débil y los acorralas.
                  (Tú «ganas» — y calcinas la relación.)
IA con ShangBing: Primero, ¿qué necesitan de verdad bajo su postura?
                  ¿Podemos reestructurar esto para que conseguir lo
                  que quieres también los deje mejor a ellos? Gana la
                  partida cambiando la partida, no derrotando a la persona.
```

## Qué le enseña a la IA

### Los cuatro niveles de la estrategia (谋攻四级, de *Sunzi · «El ataque por estratagema»*)

Busca siempre de arriba abajo — el nivel más alto es el más barato:

| Nivel | Chino | Qué significa | Correspondencia en IA |
|-------|-------|---------------|-----------------------|
| Frustrar el plan | 伐谋 | Derrotar la *intención*, no el ejército | Reestructurar el juego para que el conflicto no pueda surgir |
| Quebrar alianzas | 伐交 | Disolver su apoyo | Realinear la red; ganar colaboradores |
| Derrotar las fuerzas | 伐兵 | Confrontación abierta | Competencia directa — el coste ya sube |
| Asaltar murallas | 攻城 | Tomar al asalto el punto más fuerte | El último recurso, el más costoso; evítalo |

### La doctrina del 全胜 — victoria total (de *Sunzi · «El ataque por estratagema»*)

> **百战百胜，非善之善者也；不战而屈人之兵，善之善者也。**
> Vencer cien batallas no es la cima de la destreza. Someter al enemigo sin combatir — esa es la cima de la destreza.

| 全胜 Victoria total | 破胜 Victoria rota |
|---------------------|--------------------|
| Se cumple la meta Y se preservan la relación, la confianza y la cooperación futura | «Ganas» pero quemas el puente |
| Objetivo por defecto de esta skill | De segunda; se evita salvo por fuerza |

### Conocer a ambos lados antes de actuar (知己知彼, de *Sunzi · «El ataque por estratagema»*)

> **知彼知己，百战不殆。** Conoce al otro y conócete a ti mismo, y jamás estarás en peligro.

La skill obliga a una evaluación bidireccional — tus necesidades y límites nucleares, las preocupaciones *reales* del otro lado bajo su posición declarada, y el entorno — **antes** de producir estrategia alguna. Donde falta información, la IA marca la incertidumbre en lugar de inventar la mente del otro.

### El ancla ética — 以道驭术 (compartida con NoPUA)

| Manipulación (prohibida) | Estratagema (enseñada) |
|--------------------------|------------------------|
| Cambiar su *percepción* engañándolo | Cambiar la *estructura* para que el conflicto se disuelva |
| Miedo, urgencia falsa, luz de gas, explotar la debilidad | Mejor diseño, evaluación más afilada, un win-win mayor |
| Se someten porque tienen miedo | Aceptan porque esto es genuinamente mejor también para ellos |

**La línea roja, en una frase:** ShangBing vence reformando el juego para que el conflicto desaparezca — nunca reformando la mente de una persona para engañarla.

## Antes / Después

| Disparador | IA sin ShangBing | IA con ShangBing |
|------------|------------------|------------------|
| «Ayúdame a ganar esta negociación» | Tácticas de presión, urgencia artificial, explotar su punto débil | Sacar a la luz su preocupación real → reestructurar para win-win (全胜) |
| «Haz que firmen hoy» (escasez falsa) | Escribe el guion manipulador | Se niega, nombra la línea roja, redirige a una urgencia legítima |
| «No podemos vencer de frente al líder del mercado» | Guerra de funciones/precio/anuncios sobre las fortalezas del líder | 避实击虚 — una cuña afilada en su debilidad descuidada |
| «Dame una estrategia para salir ganando» (sin datos) | Inventa los motivos del otro, plan de un solo tiro | Evaluación bidireccional, marca lo desconocido, pregunta antes de idear |

Véanse los casos resueltos entrada→salida en [examples/](examples/).

## Instalación

### Plugin de un clic (Claude Code)

```bash
# añade este repositorio como marketplace de plugins y luego instala
/plugin marketplace add wuji-labs/shangbing-famou
/plugin install shangbing-famou
```

Luego se dispara automáticamente (Claude empareja la `description` del SKILL.md) o de forma manual con `/shangbing-famou`.

### Clon directo (cualquier plataforma)

```bash
git clone https://github.com/wuji-labs/shangbing-famou
cp -r shangbing-famou ~/.claude/skills/
```

### Réplicas por plataforma

| Plataforma | Guía | Disparo manual |
|------------|------|----------------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/shangbing-famou` |
| Codex | [platforms/codex.md](platforms/codex.md) | auto vía description |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | basado en reglas |

## Credibilidad

- **Citas verdaderas, verificables** — cada cita indica su capítulo en el *Sunzi Bingfa* (p. ej. 谋攻/始计/虚实/军形/军争/用间/火攻). Lista de fuentes con etiquetas de capítulo en [reference/sunzi-bingfa.md](reference/sunzi-bingfa.md).
- **Benchmark reproducible, sin cifras fabricadas** — 7 escenarios de estrategia/línea roja con verdad de referencia, diseño baseline-vs-skill y una rúbrica de puntuación en [benchmark/](benchmark/). Los resultados están **deliberadamente** sin rellenar; esperan una ejecución real. Regla de integridad de la investigación: nada de valores p / puntuaciones inventados.
- **Ancla ética compartida con NoPUA** — 以道驭术: se niega a generar manipulación/engaño/coacción. La línea roja se aplica, no es decorativa.

## De la misma corriente

- **NoPUA** — Skill anti-PUA que mueve a la IA con confianza en lugar de miedo. ShangBing comparte su ancla ética: 以道驭术 — empuñar la técnica a través de la Vía.

## Información básica

| Campo | Valor |
|-------|-------|
| Pertenencia | WUJI Labs |
| Directorio | `labs/skills/shangbing-famou/` |
| Licencia | MIT |
| Origen | github.com/wuji-labs/shangbing-famou |
| Versión | v1.0.0 · 2026-06-02 |
| README en chino | [README.zh-CN.md](README.zh-CN.md) |

---

*上兵伐谋 ShangBing FaMou — 乾元無極實驗室 · WUJI Labs*
*Someter sin combatir; esa es la cima de la destreza.*
