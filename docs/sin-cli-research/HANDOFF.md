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

## PR e verificação de integridade da proposta

- PR Draft: https://github.com/Suamarcanotopo/list-of-ai-coding-agents/pull/1
- Commit inicial dos oito arquivos: `07f160dc6f44b91d5ffdb36f728d1849f0237a0a`. O HEAD atual e eventuais revisões devem ser consultados na PR.
- Comparação GitHub da primeira gravação com main: oito novos arquivos, zero alterações em arquivos preexistentes. Main do fork permanece `5ebe902b5f8ec3deaf59f87c9cee9dbd1211f5c9` nesta observação.
- Auditoria estrutural executada via verificação de conteúdo remoto em JavaScript: **PASS** para 490/490 entradas, 485 URLs únicas, categorias e cinco IDs duplicados vinculados corretamente.
- Verificações negativas executadas em memória: **3/3 detectadas** (ID adulterado, URL adulterada e tentativa de falso `SANDBOX_PASS`). São testes da estrutura, não testes reais de ferramentas CLI externas.
- Validador Python versionado: **NOT_RUN** por indisponibilidade de download dos arquivos conectados no executor local. O próximo agente deve executar a própria implementação do script antes de declarar `PYTHON_PASS`.
- GitHub Actions: nenhuma execução associada ao commit inicial foi encontrada. A pasta de workflows preexistente não foi alterada; **CI=NOT_RUN**.
- Status após essa atualização: **DOCUMENTED / DRAFT / RESEARCH_ONLY / SOURCE_CODE_AUDITS=NOT_RUN / HOST_RUNTIME=NOT_RUN / NO_MERGE**.
