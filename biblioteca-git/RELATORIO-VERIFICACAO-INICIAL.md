# BIBLIOTECÁRIO — Relatório inicial de verificação

**Data:** 2026-10-09. **Escopo:** metadados GitHub, leitura de README e amostras de licença/manifests. Esta é uma triagem inicial, não auditoria de segurança completa. Não foram clonados nem executados projetos de terceiros, nem rodados testes automatizados.

## Resumo executivo
A biblioteca deve ser assimilada por padrões, não instalada como um pacote único. Prioridade inicial: Superpowers e Self-Learning Skills para metodologia; Harness de subagentes para estudo; Microsoft AI Agents for Beginners para formação; IdempotentAPI para princípios de confiabilidade; AIOX Core e Hermes Agent como candidatos a comparação arquitetural; MCP Servers como referências educacionais, não componentes prontos para produção.

## Auditoria inicial e decisão

| Projeto | Evidência consultada | Decisão | Risco/lacuna |
|---|---|---|---|
| [obra/superpowers](https://github.com/obra/superpowers) | README descreve metodologia de desenvolvimento baseada em skills, especificação, plano, TDD e YAGNI; licença MIT consultada | P0 — assimilar o fluxo; fazer PoC de processo | Verificar compatibilidade e configurações antes de instalar |
| [Kulaxyz/self-learning-skills](https://github.com/Kulaxyz/self-learning-skills) | README descreve captura de golden paths e falhas; licença MIT consultada | P0 — adotar gates de promoção de conhecimento | Revisar escopo de escrita automática e revisão das skills |
| [betta-tech/ejemplo-harness-subagentes](https://github.com/betta-tech/ejemplo-harness-subagentes) | README descreve CLI Python, leader/implementer/reviewer, checkpoints, feature list e testes | P0 — referência didática; reproduzir conceitos, não copiar código ainda | Arquivo LICENSE não encontrado no caminho consultado; confirmar licença e inspecionar init.sh |
| [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | README confirma curso introdutório multilíngue sobre agentes | P1 — trilha de estudo | Avaliar módulos individualmente; não é dependência de produção |
| [ikyriak/IdempotentAPI](https://github.com/ikyriak/IdempotentAPI) | README explica idempotência em APIs distribuídas e identifica versão 2.6.0 | P1 — assimilar requisito no Execution Engine; PoC .NET apenas se aplicável | Confirmar licença, manutenção e arquitetura; manifesto consultado não foi encontrado no caminho esperado |
| [SynkraAI/aiox-core](https://github.com/SynkraAI/aiox-core) | README descreve framework CLI-first; package.json indica @aiox-squads/core 5.4.1 e Node >=18; licença MIT menciona derivação do BMad Method | P1 — comparar arquitetura antes de adotar | Superfície funcional ampla e namespace npm em transição; evitar duplicar o orquestrador atual sem benchmark |
| [anthropics/skills](https://github.com/anthropics/skills) | README descreve skills autocontidas com SKILL.md, instruções e recursos | P1 — referência para estrutura de skills | Conferir licença de cada skill; não presumir licença uniforme |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | README alerta que são implementações de referência, não necessariamente prontas para produção; política de licença em transição MIT/Apache-2.0 | P1 — estudo de protocolos e SDKs | Avaliar cada servidor, permissões, autenticação e licença por contribuição |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | README descreve agente com skills, memória e ciclo de aprendizagem; licença MIT; pyproject declara Python >=3.11,<3.15 e dependências diretas fixadas | P2 — benchmark arquitetural, não substituição automática | Muitas integrações e grande superfície operacional; avaliar custo, permissões, dados e isolamento |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Repositório localizado; README excedeu limite de leitura do conector nesta consulta | P2 — índice para descoberta apenas | Cada servidor requer auditoria independente |
| [thalena-lima/deskcomm](https://github.com/thalena-lima/deskcomm) | README descreve CRM de vendas/WhatsApp com Next.js 16, TypeScript e Supabase | P3 para adoção industrial imediata; estudar padrões transferíveis | Domínio não é qualidade/PCP; revisar privacidade, API WhatsApp e segurança |

## Padrões assimilados para JIE/AIOX/CIOS

1. **Spec-first:** nenhuma implementação relevante sem escopo, I/O, arquitetura, dependências, critérios de aceite, threat model, testes e rollback.
2. **TDD e revisão independente:** separar Orchestrator/Leader, Implementer e Reviewer/Validator; RED → GREEN → REFACTOR quando aplicável.
3. **Isolamento por tarefa:** branch/worktree próprio, Task ID/Agent ID, versões fixadas, ambiente isolado e ausência de segredos reais.
4. **Aprendizagem verificada:** promover golden paths somente após procedimento reproduzível, evidência de validação, falha nomeada/caminho descartado quando aplicável, revisão e rollback.
5. **Idempotência nativa:** ações mutáveis devem resistir a retries e duplicação; registrar chave/estado/resultado. Operações não idempotentes exigem compensação ou aprovação humana.
6. **MCP com privilégio mínimo:** autenticação, autorização por ferramenta, validação de entradas, timeouts, limites, logs sem segredos e isolamento.
7. **Observabilidade:** registrar Task ID, agente, branch, ferramentas, tentativas, custo/latência, testes e resultado sem registrar segredos.
8. **Menor composição útil:** não adicionar vários orquestradores completos com funções sobrepostas; comparar benefício medido, custo e superfície de risco.
9. **Licença antes de reutilizar código:** sem licença clara, não copiar/distribuir. Repositórios awesome e exemplos não são homologação.
10. **Human-in-the-loop:** sem merge, deploy, gastos, provisionamento ou ações industriais críticas sem autorização explícita.

## Inventário de metadados

Os seguintes repositórios responderam à consulta de metadados GitHub; isso confirma que foram localizados, não que sejam seguros ou aprovados: DonutShinobu/claude-code-fork; kyegomez/OpenMythos; microsoft/ai-agents-for-beginners; public-apis/public-apis; obra/superpowers; modelcontextprotocol/servers; NousResearch/hermes-agent; obra/private-journal-mcp; punkpeye/awesome-mcp-servers; sipeed/picoclaw; 666ghj/MiroFish; ikyriak/IdempotentAPI; betta-tech/ejemplo-harness-subagentes; thalena-lima/deskcomm; renatoasse/opensquad; fathah/hermes-desktop; gooseworks-ai/goose-skills; SynkraAI/aiox-core; adrianoviana/claude-code-demos; teng-lin/notebooklm-py; anthropics/skills; sickn33/agentic-awesome-skills; alexzhang13/rlm; mattpocock/skills; Kulaxyz/self-learning-skills; ultraworkers/claw-code; garrytan/gstack; Jhonatan-de-Souza/LinkedInAutomator-Code; rafaelquintanilha/skills; ComposioHQ/awesome-claude-skills.

### Tratamento especial
- Jhonatan-de-Souza/LinkedInAutomator-Code está arquivado; não priorizar e revalidar termos da plataforma, privacidade e manutenção antes de qualquer uso.
- URLs de organizações como ComposioHQ/repositories e tech-leads-club/repositories são índices de organização, não projetos únicos para pontuação.
- O Gist de Karpathy é uma referência isolada; avaliar contexto, licença e objetivo separadamente.
- Hermes Agent aparece duplicado no catálogo; manter uma identidade canônica.
- A lista awesome é para descoberta, não aprovação.

## Próximos passos
1. Validar YAML/Markdown automaticamente em CI.
2. Criar SPEC para uma PoC Python que demonstre leader/implementer/reviewer sem importar código externo.
3. Adicionar idempotência, logging estruturado e testes antes de conectar ferramentas com efeitos colaterais.
4. Só selecionar framework completo após benchmark contra a arquitetura atual.

## Limites desta verificação
Não concluídos: auditoria profunda de todos os 35 itens, análise de dependências transitivas/CVEs, testes locais, execução de projetos ou homologação jurídica. Essas tarefas continuam pendentes e não devem ser interpretadas como aprovação.