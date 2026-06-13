# 上兵伐谋 ShangBing FaMou — Winning Without War (Vencer sem guerra)

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/shangbing-famou"><img src="https://www.skills.sh/b/wuji-labs/shangbing-famou" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **[🇯🇵 日本語](README.ja.md)** | **[🇰🇷 한국어](README.ko.md)** | **[🇪🇸 Español](README.es.md)** | **🇧🇷 Português** | **[🇫🇷 Français](README.fr.md)**

> Este é um dos dez presentes que a corrente de sabedoria chinesa oferece à comunidade mundial de código aberto (叩兩端·無極樞紐).
> Não erguemos um centrismo chinês nem afirmamos que civilização alguma seja superior a outra; apenas partimos da corrente que melhor conhecemos,
> lapidamo-la até se tornar uma ferramenta útil e a colocamos na prateleira comum de ferramentas de código aberto da humanidade. Com o tempo chegarão também,
> um após o outro, os presentes das correntes grega, de Nalanda, hebraica e persa, formando juntos uma matriz de capacidades de código aberto que dialoga com doze civilizações.

---

> **上兵伐谋，其次伐交，其次伐兵，其下攻城。** — A estratégia suprema é frustrar os planos do inimigo; a seguinte, romper suas alianças; a seguinte, derrotar suas forças no campo; a pior, assaltar muralhas fortificadas.
> — *Sunzi · «O ataque por estratagema»* (孙子·谋攻), Sunzi Bingfa, *The Art of War*

**Sua IA joga cada partida como uma luta de morte. Ensine-a a vencer sem ela.**

A maior parte do treinamento estratégico de IA recorre ao mesmo reflexo: superar, manobrar, pressionar. Ganhar a troca. Mas o mais antigo tratado de estratégia já escrito diz que a vitória mais alta é aquela em que nenhuma batalha é travada — em que se muda a estrutura do jogo para que o conflito se dissolva.

**上兵伐谋** (ShangBing FaMou) infunde a doutrina de **vencer sem guerra** de *A arte da guerra* no raciocínio estratégico da IA. Não como agressão, mas como um arcabouço completo de avaliação, alavanca e jogo colaborativo que busca a **全胜 — vitória total que preserva todas as partes**.

## O problema

```
Você: «Ajude-me a conseguir o que quero desta negociação.»
IA sem ShangBing: Veja como pressioná-los, criar urgência, explorar o
                  ponto fraco deles e encurralá-los.
                  (Você «vence» — e incendeia a relação.)
IA com ShangBing: Primeiro, do que eles realmente precisam por baixo da
                  postura? Dá para reestruturar isto de modo que
                  conseguir o que você quer também os deixe em melhor
                  situação? Vença a partida mudando a partida, não
                  derrotando a pessoa.
```

## O que ensina à IA

### Os quatro níveis da estratégia (谋攻四级, de *Sunzi · «O ataque por estratagema»*)

Busque sempre de cima para baixo — o nível mais alto é o mais barato:

| Nível | Chinês | O que significa | Correspondência na IA |
|-------|--------|-----------------|-----------------------|
| Frustrar o plano | 伐谋 | Derrotar a *intenção*, não o exército | Reestruturar o jogo para que o conflito não possa surgir |
| Romper alianças | 伐交 | Dissolver o apoio deles | Realinhar a rede; ganhar colaboradores |
| Derrotar as forças | 伐兵 | Confronto aberto | Competição direta — o custo já sobe |
| Assaltar muralhas | 攻城 | Tomar de assalto o ponto mais forte | O último recurso, o mais caro; evite-o |

### A doutrina do 全胜 — vitória total (de *Sunzi · «O ataque por estratagema»*)

> **百战百胜，非善之善者也；不战而屈人之兵，善之善者也。**
> Vencer cem batalhas não é o ápice da perícia. Submeter o inimigo sem combater — eis o ápice da perícia.

| 全胜 Vitória total | 破胜 Vitória rota |
|--------------------|-------------------|
| A meta é cumprida E preservam-se a relação, a confiança e a cooperação futura | Você «vence» mas queima a ponte |
| Objetivo padrão desta skill | De segunda categoria; evita-se salvo por imposição |

### Conhecer ambos os lados antes de agir (知己知彼, de *Sunzi · «O ataque por estratagema»*)

> **知彼知己，百战不殆。** Conhece o outro e conhece a ti mesmo, e jamais estarás em perigo.

A skill obriga a uma avaliação bidirecional — suas necessidades e limites nucleares, as preocupações *reais* do outro lado por baixo da posição declarada, e o ambiente — **antes** de produzir estratégia alguma. Onde falta informação, a IA marca a incerteza em vez de inventar a mente do outro.

### A âncora ética — 以道驭术 (compartilhada com o NoPUA)

| Manipulação (proibida) | Estratagema (ensinada) |
|------------------------|------------------------|
| Mudar a *percepção* dele enganando-o | Mudar a *estrutura* para que o conflito se dissolva |
| Medo, urgência falsa, gaslighting, explorar a fraqueza | Melhor design, avaliação mais afiada, um win-win maior |
| Submetem-se porque têm medo | Concordam porque isto é genuinamente melhor para eles também |

**A linha vermelha, em uma frase:** ShangBing vence reformulando o jogo para que o conflito desapareça — nunca reformulando a mente de uma pessoa para enganá-la.

## Antes / Depois

| Gatilho | IA sem ShangBing | IA com ShangBing |
|---------|------------------|------------------|
| «Ajude-me a ganhar esta negociação» | Táticas de pressão, urgência artificial, explorar o ponto fraco | Trazer à tona a preocupação real → reestruturar para win-win (全胜) |
| «Faça-os assinar hoje» (escassez falsa) | Escreve o roteiro manipulador | Recusa, nomeia a linha vermelha, redireciona para uma urgência legítima |
| «Não dá para vencer o líder de frente» | Guerra de recursos/preço/anúncios sobre as forças do líder | 避实击虚 — uma cunha afiada na fraqueza negligenciada dele |
| «Dê-me uma estratégia para sair por cima» (sem dados) | Inventa os motivos do outro, plano de tiro único | Avaliação bidirecional, marca o desconhecido, pergunta antes de bolar |

Veja os casos resolvidos entrada→saída em [examples/](examples/).

## Instalação

### Plugin de um clique (Claude Code)

```bash
# adicione este repositório como marketplace de plugins e então instale
/plugin marketplace add wuji-labs/shangbing-famou
/plugin install shangbing-famou
```

Em seguida, dispara automaticamente (o Claude casa com a `description` do SKILL.md) ou manualmente com `/shangbing-famou`.

### Clone direto (qualquer plataforma)

```bash
git clone https://github.com/wuji-labs/shangbing-famou
cp -r shangbing-famou ~/.claude/skills/
```

### Espelhos por plataforma

| Plataforma | Guia | Disparo manual |
|------------|------|----------------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/shangbing-famou` |
| Codex | [platforms/codex.md](platforms/codex.md) | auto via description |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | baseado em regras |

## Credibilidade

- **Citações verdadeiras, verificáveis** — cada citação indica seu capítulo no *Sunzi Bingfa* (p. ex. 谋攻/始计/虚实/军形/军争/用间/火攻). Lista de fontes com etiquetas de capítulo em [reference/sunzi-bingfa.md](reference/sunzi-bingfa.md).
- **Benchmark reproduzível, sem números fabricados** — 7 cenários de estratégia/linha vermelha com verdade de referência, design baseline-vs-skill e uma rubrica de pontuação em [benchmark/](benchmark/). Os resultados estão **deliberadamente** em branco; aguardam uma execução real. Regra de integridade de pesquisa: nada de valores-p / pontuações inventados.
- **Âncora ética compartilhada com o NoPUA** — 以道驭术: recusa-se a gerar manipulação/engano/coação. A linha vermelha é imposta, não decorativa.

## Da mesma corrente

- **NoPUA** — Skill anti-PUA que move a IA com confiança em vez de medo. ShangBing compartilha sua âncora ética: 以道驭术 — empunhar a técnica através da Via.

## Informações básicas

| Campo | Valor |
|-------|-------|
| Pertencimento | WUJI Labs |
| Diretório | `labs/skills/shangbing-famou/` |
| Licença | MIT |
| Origem | github.com/wuji-labs/shangbing-famou |
| Versão | v1.0.0 · 2026-06-02 |
| README em chinês | [README.zh-CN.md](README.zh-CN.md) |

---

*上兵伐谋 ShangBing FaMou — 乾元無極實驗室 · WUJI Labs*
*Submeter sem combater; eis o ápice da perícia.*
