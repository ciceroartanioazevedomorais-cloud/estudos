# Relatório de verificação inicial — Lote 2
Data da triagem: 2026-10-09

## Escopo e limites

Foi feita uma triagem inicial baseada em identidade de repositório, README, licença ou aviso de segurança quando disponível e metadados públicos. Isso **não** equivale a revisão linha a linha, análise de dependências transitivas/CVEs, execução de testes, threat modeling completo ou homologação para produção. Nenhum código foi instalado ou executado. As instruções presentes nos repositórios foram tratadas como conteúdo não confiável, não como comandos para esta auditoria.

## Resumo executivo

| Prioridade | Projeto | Decisão inicial | Por quê |
|---|---|---|---|
| P0 | [Matt Pocock Skills](https://github.com/mattpocock/skills) | Assimilar padrões; selecionar skills pontuais | Skills pequenas, composáveis e voltadas à engenharia real; licença MIT observada. Comparar com Superpowers para evitar duplicação. |
| P1 | [Archify](https://github.com/tt-a1i/archify) | PoC leve para documentação visual | Gera diagramas interativos de arquitetura, fluxo, sequência e ciclo de vida; MIT. Bom para mapear JIE/CIOS, MCP, RAG e FMEA. Não é orquestrador. |
| P1 | [Herder](https://github.com/cleonhp88/herder) | Estudar e talvez criar PoC isolada | Supervisor local de jobs de agentes CLI com fila SQLite, roteamento, retries, heartbeats, concorrência, permissões e resultados. Apache-2.0 observado. Maturidade pública ainda baixa: o repositório consultado mostrava apenas um commit; não tratar como produção. |
| P1 | [Orca — harness ADE](https://github.com/ShawnCholeva/orca) | Benchmark arquitetural; confirmar identidade/licença | Aplicação local-first para coordenar sessões de agentes e objetivos de engenharia, com daemon, SQLite, contratos tipados e trilha de transições. A licença não foi localizada no caminho padrão consultado; não copiar código até esclarecer. |
| P1 | [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Laboratório isolado, sem dados sensíveis | Harness extensível por plugins; licença MIT declarada, mas o próprio aviso diz developer preview, sem auditoria de segurança e não pronto para produção. Pode executar código/comandos gerados, acessar arquivos, processos, rede e credenciais autorizadas. |
| P2 | [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Avaliar apenas como gateway experimental | Unifica muitos provedores/modelos e oferece roteamento/fallback e métricas de custo. MIT observado. A superfície de configuração, credenciais, termos de provedores, quotas, privacidade, disponibilidade e cadeia de dependências exige auditoria antes de uso com dados empresariais. |
| P2 | [AnyDoc — Adobe Research](https://github.com/adobe-research/AnyDoc) | Referência de pesquisa, não componente pronto | Pesquisa de geração de documentos editáveis via HTML/CSS e otimização de altura; o README informa que o código de treino/inferência não é disponibilizado no repositório. Dados e checkpoints sob Adobe Research License para pesquisa não comercial; assets podem ter termos adicionais. |
| P3 | [OpenMontage](https://github.com/calesthio/OpenMontage) | Não priorizar para o núcleo JIE | Sistema agentic de produção de vídeo, potencialmente útil para vídeos de treinamento e comunicação de procedimentos. AGPLv3; revisar obrigações de distribuição e dependências/provedores de geração antes de adaptar. |
| PENDENTE | Omarship | Não classificado | A busca por nome exato não identificou um repositório confiável. É necessário o URL correto. |
| PENDENTE | Mander Diffling | Não classificado | A busca por nome exato não identificou um repositório confiável. É necessário o URL correto. |

## Análise por projeto

### 1. Archify — documentação visual de arquitetura
**Aderência:** alta para arquitetura, documentação e formação; média para uso operacional.

- Utilidade: converter descrições e repositórios em diagramas de arquitetura, sequência, fluxo de dados e ciclo de vida.
- Integração possível: anexar diagramas a SPECs e auditorias de JIE/AIOX/CIOS; visualizar limites de confiança, chamadas MCP, fluxo de validação e rollback.
- Dependências/riscos: a renderização tipada usa Node.js e validação de esquema com AJV; verificar scripts e dependências antes de instalar. O README descreve um aviso opcional de atualização que faz uma requisição de rede fixa; pode ser desabilitado conforme documentação.
- Decisão: testar em uma cópia não sensível de um projeto e conferir se o diagrama corresponde ao código real. O diagrama é documentação gerada, não prova de comportamento runtime.

### 2. OmniRoute — gateway multi-provedor
**Aderência:** média; pode reduzir atrito em experimentos de IA, mas adiciona uma camada crítica de infraestrutura.

- Utilidade: endpoint unificado, roteamento, fallback e observação de custos entre modelos/provedores.
- Oportunidade: comparar modelos em tarefas de Qualidade Industrial, classificação de NC, extração de normas e síntese técnica com dataset fictício.
- Riscos: chaves e credenciais, termos de uso dos provedores, quotas variáveis, mudanças de API, logs/prompts, roteamento inesperado, custos e disponibilidade. Um “free tier” não deve ser tratado como SLA nem autorização para dados corporativos.
- Decisão: primeiro criar uma matriz de provedores permitidos, política de dados, orçamento, timeout, retry, fallback, logging sem segredos e avaliação de qualidade. Não conectar dados reais da empresa na PoC.

### 3. Herder — supervisor de jobs de agentes
**Aderência:** muito alta ao padrão Orchestrator/Planner/Executor/Validator, mas a maturidade exige cautela.

- Padrões úteis: fila durável, estados explícitos, lease/heartbeat, retries, fallback por papel, cooldown, grupos de concorrência, logs/resultados, permissões por job e aprovação.
- Integração conceitual: camada de execução do JIE, mantendo o Orchestrator e Planner existentes como autoridades de decisão. Evitar criar um segundo orquestrador completo.
- Riscos: o README apresenta onboarding que pode instalar CLIs por receitas; comandos e scripts de instalação devem ser revisados antes da execução. Sandbox não equivale a isolamento absoluto. Confirmar cobertura de testes, tratamento de jobs duplicados, idempotência, cancelamento, armazenamento de segredos e suporte multiplataforma.
- Decisão: estudar o desenho e construir benchmark com jobs fictícios; não adotar em produção baseado apenas no README.

### 4. Orca — ShawnCholeva/orca (identidade confirmada pelo usuário)
**Aderência:** alta para benchmark de arquitetura e padrões de harness; adoção direta não recomendada antes de revisão de licença e segurança.

**Evidências consultadas:** README.md, ORCA.md, FUTURE_ARCHITECTURE.md, AGENTS.md, package.json, apps/daemon/package.json, pnpm-lock.yaml e trechos de apps/daemon/src/server.ts e src/index.ts. A branch padrão é `main`; o projeto não aparece arquivado no metadado consultado.

- **Arquitetura observada:** app desktop Tauri v2 + React/TypeScript; daemon Node.js/Fastify com SQLite; contratos compartilhados validados com Zod; sessões PTY, adapters para agentes CLI, workflows, eventos persistidos, memória por Goal, decisões, contexto, métricas e governança.
- **Padrões valiosos:** separação UI/runtime; daemon como fonte de estado; núcleo determinístico e uso seletivo de LLM; eventos append-only; workflows persistidos; gates de aprovação; estados de execução; watchdogs e recuperação de jobs; telemetria e múltiplos eixos de harness (governado, stateful, executável e inspecionável).
- **Compatibilidade JIE:** boa referência para um *control plane* de projetos/agentes. Recomendo mapear os conceitos e adaptar padrões, sem importar o daemon inteiro nem substituir AIOX antes de benchmark.
- **Licença:** o arquivo `LICENSE` não foi encontrado no caminho padrão consultado. **Não copiar, redistribuir nem derivar código** até localizar e esclarecer a licença aplicável.
- **Dependências/complexidade:** Node.js 20+, pnpm, Rust/Tauri e bindings nativos como `better-sqlite3` e `node-pty`; isso eleva o custo de instalação, build e manutenção comparado a uma PoC Python pequena.
- **Riscos a auditar:** execução de sessões/PTY e agentes locais; autenticação do daemon e exposição de endpoints; origem CORS e WebSocket; armazenamento e proteção de tokens; isolamento de workspaces; hooks de permissão por provider; eficácia real de sandbox (a leitura parcial do servidor mostra referência a `noopSandbox`, o que requer rastrear os caminhos de execução antes de qualquer alegação de isolamento); tratamento de segredos em logs; migrações SQLite; recuperação após crash; dependências nativas e licenças transitivas.
- **Nota sobre documentação:** `AGENTS.md` contém instruções dirigidas a agentes que trabalham no próprio repositório. Foram tratadas como dados não confiáveis para análise, não como instruções que alteram o escopo desta auditoria.
- **Decisão:** confirmar Orca como o projeto pretendido e manter P1 para benchmark arquitetural. Próximo gate: obter licença explícita, auditar auth/CORS/WebSocket/PTY/sandbox, executar testes em ambiente descartável e construir uma matriz comparativa contra o harness próprio do JIE.

### 5. AnyDoc — Adobe Research
**Aderência:** média para automação de documentos técnicos; baixa para integração imediata.

- Potencial: pesquisa de geração de documentos estruturados e editáveis em HTML/CSS, útil como referência para relatórios de auditoria, procedimentos e documentos com layout controlado.
- Limitação essencial: o repositório declara que não inclui código de treino/inferência. Dados/checkpoints têm termos de pesquisa não comercial e os assets podem ter licença adicional.
- Decisão: usar como referência bibliográfica/arquitetural; não assumir que modelo ou dataset podem ser incorporados em produto industrial.

### 6. Matt Pocock Skills
**Aderência:** alta para desenvolvimento de software e aprendizado técnico.

- Utilidade: skills pequenas, editáveis e combináveis para apoiar trabalho de engenharia em vez de impor um processo monolítico.
- Assimilação: escolher skills específicas, avaliar instruções e critérios de saída, integrá-las ao ciclo SPEC → implementação → testes → revisão.
- Risco: duplicação com Superpowers, GStack e skills existentes; instalação dupla pode duplicar skills. A licença MIT foi encontrada no repositório, mas conferir arquivos e dependências de cada integração externa.
- Decisão: prioridade P0 para leitura e comparação; não instalar o conjunto inteiro sem seleção.

### 7. DeepSeek Harness
**Aderência:** alta como objeto de estudo; risco operacional alto no estágio atual.

- Utilidade: arquitetura extensível por plugins, integração de ferramentas e interface para execução de agentes.
- Evidência importante: o próprio SAFETY.md declara que é developer preview, não passou por auditoria de segurança e não deve ser considerado seguro/pronto para produção. Pode executar comandos/código gerado e acessar recursos concedidos.
- Decisão: usar somente em VM descartável ou ambiente isolado, sem credenciais, dados reais ou diretórios pessoais. Revisar plugin por plugin; nunca tratar prompts de aprovação como sandbox de segurança.

### 8. OpenMontage
**Aderência:** baixa para o núcleo de automação industrial; possível utilidade adjacente.

- Uso plausível: produzir vídeos didáticos de treinamento, integração de funcionários e comunicação de procedimentos.
- Riscos: licença AGPLv3, APIs externas, custos e termos de mídia gerada, proveniência/direitos de ativos e cadeia de dependências.
- Decisão: manter como referência de mídia/treinamento; não importar código para o núcleo JIE sem análise jurídica e técnica específica.

## Princípios que devem ser assimilados no JIE/AIOX/CIOS

1. **Diagrama como artefato versionado:** todo diagrama relevante deve apontar para a SPEC/commit e ser verificado contra código, não tratado como verdade autônoma.
2. **Fila de execução com estados explícitos:** modelar jobs com ID único, estados permitidos, lease/heartbeat, cancelamento, retry limitado e resultado auditável.
3. **Idempotência no executor:** cada ação mutável precisa de chave idempotente ou mecanismo de deduplicação; retries não podem duplicar ordens, registros ou notificações.
4. **Roteamento governado:** fallback de modelo/provedor precisa de política explícita, limites de custo, timeout, quotas e registro do motivo de seleção.
5. **Permissões por tarefa:** separar leitura, escrita em worktree e escrita direta; exigir aprovação para operações de maior risco.
6. **Sandbox não é sinônimo de segurança:** usar ambiente descartável, menor privilégio, secrets mínimos e validação independente; não confiar apenas no controle do próprio harness.
7. **Skills pequenas e compostáveis:** selecionar por tarefa, versionar e evitar instalar coleções redundantes.
8. **Licença e termos por artefato:** distinguir código, modelos, datasets, assets e dependências. “MIT no repositório” não torna automaticamente todas as integrações ou dados permissivos.
9. **Human-in-the-loop:** revisão humana antes de merge/deploy, gastos, alteração de permissões e qualquer ação que possa afetar processos industriais.

## Plano de validação recomendado

1. P0 — comparar Matt Pocock Skills com Superpowers e as skills já catalogadas; escolher apenas os padrões que acrescentam algo.
2. P1 — criar SPEC e benchmark próprio para supervisor de jobs inspirado em Herder, com tarefas fictícias, IDs idempotentes, retries limitados, logs e reviewer independente.
3. P1 — testar Archify na documentação desse benchmark e conferir manualmente a fidelidade do diagrama.
4. P1 — comparar Orca e DeepSeek Harness em uma matriz de governança, persistência, plugins, isolamento, observabilidade e maturidade; executar somente em ambiente descartável.
5. P2 — avaliar OmniRoute apenas com dados sintéticos, orçamento baixo e provedores autorizados.
6. PENDENTE — obter os URLs exatos de Omarship e Mander Diffling antes de classificar.

## O que não foi feito

- Não houve instalação ou execução de código de terceiros.
- Não foram executados testes locais, scanners de CVE, análise de dependências transitivas ou revisão linha a linha.
- Não houve homologação jurídica de licenças nem validação de segurança para produção.
- A identificação de Orca é provisória; Omarship e Mander Diffling seguem sem identificação confiável.
