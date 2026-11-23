# Handoff — SIN CLI intelligence

**ID:** `SIN-CLI-SOURCE-MINING-20261123-001`
**Estado:** `DRAFT / RESEARCH_ONLY / NOT_INSTALLED / NO_MERGE / RUNTIME_NOT_RUN`

## Evidência documental disponível

- Fork GitHub, baseline commit `5ebe902b5f8ec3deaf59f87c9cee9dbd1211f5c9`.
- README blob `6c2a529e97ff152ba12b83509f70e0f2542186f4`.
- 490 entradas em seis categorias; 485 URLs distintas; cinco URLs repetidas.
- `INVENTORY.csv` é o mapa completo inicial, preenchido por padrões do README. O campo `review_state` de todas as linhas é `DISCOVERED_README_ONLY`, com fonte primária, licença e testes pendentes.
- `CLAUDE-MISSION.md` especifica investigação, critérios e formato de entregáveis.
- `PRIORITY-MATRIX.md` é uma shortlist heurística, sem homologação.

## Não realizado

- Revisão do código de todas as 485 fontes; licença por dependência; instalação; testes em sandbox; benchmarks; integração a hosts; chamadas de múltiplos agentes; atualização ou homologação de Skill; aprovação independente do Coliseum; publicação.
- Não transportar para o fork resultados internos, documentação confidencial ou dados de clientes.

## Próxima ação reproduzível

1. Ler Mission Lock, CLAUDE-MISSION, README do fork e INVENTORY.
2. Rodar `python3 docs/sin-cli-research/validate_inventory.py --self-test` e salvar o resultado com SHA do commit da execução.
3. Começar investigação profunda pela Wave 1 da matriz; usar caminhos e commits primários, não a descrição do agregador como prova.
4. Para cada URL, atualizar o registro de fonte em um anexo/PR de pesquisa; não substituir o inventário-base sem verificar consistência e manter os IDs estáveis.
5. Reportar fonte examinada, veredito, owner candidato, requisito de prova e status; não marcar `PASS` sem rodar os testes.
6. Consultar regras e PRs ativos do repositório operacional privado ANTES de propor atualização ali. Não submeter nova PR privada sem decisão específica de prioridade.
7. Quando interrompido, guardar último ID examinado, mudanças realizadas, pendências e a próxima fonte a ser lida.

## Reversibilidade

PR exclusivamente documental no fork. Fechar sem merge preserva a main do fork e todo o ecossistema operacional.
