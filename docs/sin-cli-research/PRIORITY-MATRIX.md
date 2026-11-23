# Matriz inicial de investigação — hipóteses a falsificar

Este quadro é proposta de **ordem de leitura**, não ranking de performance. O inventário integral com 490 linhas continua obrigatório. Em cada item, Claude deve abrir o repositório primário, conferir o commit, ler documentação e arquivos pertinentes, identificar a licença exata e produzir experimento com teste positivo + negativo.

| Referência primária | Técnica a extrair | Contraprova / requisito de aceitação | Domínio candidato |
|---|---|---|---|
| [GitHub Agentic Workflows](https://github.com/github/gh-aw) | Workflows declarativos, permissões reduzidas, safe outputs | A tentativa de alterar recurso não autorizado é barrada | Governance Guard / ECP |
| [isitdone](https://github.com/raimondasl/isitdone) | Evidência vinculada ao estado atual do código | Teste PASS antigo seguido de edição não autoriza DONE | Coliseum |
| [Concord MCP](https://github.com/Get-Concord-AI/concord-mcp) | Claims sobre arquivos, handoff e coordenação | Dois executores sobrepõem o mesmo arquivo: conflito detectado; verificar enforcement real | ECP / AI Wiring |
| [Tianshu Harness](https://github.com/huiliyi37/Tianshu-harness) | Objetivo, contexto, prova e término externalizados | Mensagem 'terminei' sem prova não vira validação | ECP / Coliseum |
| [Dvalin](https://github.com/arthurpanhku/dvalincode) | Rechecagem de vulnerabilidades e registros de correção | Remoção de teste ou supressão de scanner é detectada | CyberSec / Coliseum |
| [zeroshot](https://github.com/the-open-engine/zeroshot) | Grafo executor → revisor → verificador | Autor do patch não aprova sozinho o próprio resultado | Coliseum / ECP |
| [Beads](https://github.com/gastownhall/beads) | Grafo persistente de dependências e fatos | Retomada não perde bloqueios nem duplica efeitos | ECP / SIN Team Ops |
| [Agent Orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) | Worktrees, owner de PR, roteamento de CI | Tarefas paralelas não se sobrepõem silenciosamente | ECP / SIN GitHub Flow |
| [Symphony](https://github.com/openai/symphony) | Issue → executor isolado → prova | Agente não promove PR sem checks, revisão e autoridade | ECP / SIN GitHub Flow |
| [Headroom](https://github.com/headroomlabs-ai/headroom) | Compressão/retrieval de contexto | Regras críticas preservadas com menor consumo real | Context Engineering |
| [OpenWiki](https://github.com/langchain-ai/openwiki) | Wiki derivada do código e proveniência | Docs antigas não prevalecem sobre testes/código | Knowledge Curator |
| [Agent Executor](https://github.com/google/ax) | Sessão isolada e retomável | Retomada não repete operação com efeito externo | ECP / Data Integrity |
| [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Políticas de sandbox para agentes | Exfiltração ou acesso fora do allowlist falha | CyberSec |
| [OneCLI](https://github.com/onecli/onecli) | Gateway de credenciais e aprovações | Agente não lê segredo bruto nem ultrapassa o grant | Governance Guard / CyberSec |
| [OpenViking](https://github.com/volcengine/OpenViking) | Conhecimento, Skills e memória em filesystem virtual | Recalls corretos sem vazamento interprojeto; avaliar AGPL | Context Engineering |
| [Docker Agent](https://github.com/docker/docker-agent) | Declaração de equipes/agentes e ferramentas | Restrição por agente e portabilidade comprovadas | AI Wiring / Agentic Integration |
| [OpenCodeReview](https://github.com/alibaba/open-code-review) | Revisão de diff com modelo e ferramentas | Falha introduzida é identificada sem falso positivo elevado | Coliseum |
| [ralph-harness / LoopGate](https://github.com/rxdt/py_ralph_frame) | Loop de agentes sob gates locais | Sem progresso ou iterações excessivas interrompe | ECP |
| [MartinLoop](https://github.com/Keesan12/martin-loop) | Orçamentos, limites, stop conditions, recibos | Orçamento excedido causa parada segura | ECP / Observability |
| [agent-browser](https://github.com/vercel-labs/agent-browser) | Testes de navegação real e evidência visual | Resultado DOM não é confundido com layout/E2E aprovado | Browser Director / UX Guider |
| [Kimi Code](https://github.com/MoonshotAI/kimi-code) | Subagentes, hooks, resumibilidade e protocolos | Subagente sem permissão não ganha acesso indireto | ECP / AI Wiring |
| [gitagent](https://github.com/open-gitagent/gitagent) | Estado/configuração de agente versionados | Mudança não autorizada no contrato gera alerta | SEE / Governance Guard |
| [Codewhale](https://github.com/Hmbown/CodeWhale) | Roteamento por papel/modelo/custo, undo | Economia existe sem queda material da qualidade | ECP / Observability |
| [Prime Agent](https://github.com/PrimeIntellect-ai/prime-agent) | Aprendizado e refinamento por evidência | Erro não é incorporado automaticamente como regra | SEE / ECP |
| [molt](https://github.com/solvyxtech/molt) | Recusa de término sem prova material | Recibo falso ou desatualizado não aprova | Coliseum |
| [MoCode](https://github.com/wanxunyang/mocode) | Hash gate para Skills e corpus de avaliações | Skill adulterada é rejeitada | SEE / CyberSec |
| [h5i](https://github.com/h5i-dev/h5i) | Revisores independentes e replay de candidatos | Votação entre IAs não substitui replay determinístico | Coliseum |
| [deja-vu](https://github.com/vshulcz/deja-vu) | Busca local entre históricos de agentes | Segredos e contextos privados não vazam | Context Engineering |
| [saver-audit](https://github.com/VladUZH/saver-audit) | Auditoria reproduzível de economia de tokens | Separar medição real, replay e estimativa | ECP / Observability |

## Sequência de investigação recomendada

**Wave 1:** filas prioritárias acima, iniciando pelos bloqueios de falso DONE, sobreposição de arquivos, provas e permissões. A existência na Wave 1 não autoriza instalar.

**Wave 2:** itens restantes com indícios de múltiplas técnicas úteis.

**Wave 3:** demais agentes/infraestrutura e casos de baixo sinal — ainda exigem leitura e desfecho registrado (`USE_EXISTING|EVOLVE|ADAPTER|CREATE|DEFER|REJECT|OUT`).

## Contradições a procurar

- Readme agregador desatualizado em relação ao README/código primário.
- Licença declarada diferente da licença de subcomponentes/modelos/dependências.
- 'Open Source' que é apenas source-available.
- Trabalho 'parallel' que isola diretórios, mas não impede conflitos lógicos.
- 'Autonomous' que só repete prompts sem novas evidências.
- 'Verified' que significa 'tests passed' antes de última alteração.
- Métricas de economia de tokens sem manter exatidão factual.
- RAG/memória que aumenta recall sem separar dados de diferentes usuários.
- Agentes que copiam instruções não confiáveis como se fossem política.
- Host compatível no papel, mas incapaz de executar a ferramenta.
