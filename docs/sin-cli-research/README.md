# SIN · Auditoria de agentes CLI e harnesses — missão para Claude/GPT

**Natureza:** material de pesquisa pública no fork; não é Skill instalada, plugin, orquestrador ativo, aprovação de produto nem concessão de privilégios.

## Como começar

- [Missão operacional detalhada para Claude](CLAUDE-MISSION.md)
- [Inventário das 490 entradas do README](INVENTORY.csv)
- [Matriz de fontes e experimentos prioritários](PRIORITY-MATRIX.md)
- [Mission Lock e escopo de segurança](MISSION-LOCK.md)
- [Handoff e estado real](HANDOFF.md)
- [Validador determinístico do inventário](validate_inventory.py)

## Fonte de verdade e limites

- Catálogo: [README.md](../../README.md), blob Git `6c2a529e97ff152ba12b83509f70e0f2542186f4` no commit inicial do fork `5ebe902b5f8ec3deaf59f87c9cee9dbd1211f5c9`.
- 490 entradas; 485 URLs distintas; grupos: Open Source 131, OpenClaw ecosystem 12, Closed Source 18, Session managers & parallel runners 116, Orchestrators & autonomous loops 62, Agent infrastructure 151.
- Classificação `W1/W2/W3` é uma fila inicial construída por heurísticas e nomes, **não** pontuação de confiabilidade. Todos os itens entram na cobertura, inclusive W3.
- Cinco URLs repetidas; `duplicate_of` referencia a primeira ocorrência.
- Técnica, domínio SIN e impacto são hipóteses extraídas do sumário; software, capacidade, compatibilidade e licença das fontes não foram verificados individualmente.
- A presença em seção 'Open Source' não valida a licença de cada componente; pode haver projetos source-available.
- Repositório público: não incluir caminhos privados, hashes de releases internas, dados de clientes, credenciais ou detalhes de PRs privados.

## Entrega pretendida

1. Investigação progressiva de cada URL única e registro da cobertura das 490 entradas.
2. Comparação `baseline SIN → técnica externa → mecanismo transferível → risco → teste→ decisão`.
3. Recomendação `USE_EXISTING / EVOLVE_SKILL / NEW_ADAPTER / CREATE_CANDIDATE / DEFER / REJECT / OUT`.
4. Experimentos e contraprovas verificáveis antes de qualquer promoção.
5. Handoff com contador, fontes fixadas, lacunas, próxima ação e instrução de retomada.

Rodar verificador documental: `python3 docs/sin-cli-research/validate_inventory.py --self-test`.

**Status:** proposta documental, inventário extraído do catálogo; revisão primária e experimentos das ferramentas listadas permanecem `NOT_RUN`.
