# Princípios assimilados da Biblioteca Git

Este documento registra padrões de engenharia selecionados na triagem de 2026-10-09. São diretrizes para JIE/AIOX/CIOS; não significam que os projetos de origem foram integralmente auditados.

1. **Spec-first:** especificação, critérios de aceite, ameaças, testes e rollback antes de implementação significativa.
2. **TDD e revisão independente:** separar planejamento, implementação e validação; usar RED → GREEN → REFACTOR quando aplicável.
3. **Isolamento por tarefa:** branch/worktree dedicado, Task ID/Agent ID, versões fixadas e ambiente sem segredos.
4. **Idempotência por padrão:** ações mutáveis resistem a retries e duplicação; ações não idempotentes exigem compensação ou aprovação humana.
5. **Aprendizagem verificada:** promover golden paths somente com procedimento reproduzível, evidência, falhas/caminhos descartados, revisão e rollback.
6. **MCP com privilégio mínimo:** ferramentas limitadas, autenticação, validação, timeouts, logs seguros e testes de abuso.
7. **Observabilidade:** registrar agente, tarefa, branch, ferramentas, tentativas, duração/custo, testes, decisões e resultado sem segredos.
8. **Menor composição útil:** não introduzir um segundo orquestrador completo sem evidência de benefício.
9. **Licença antes do código:** listas awesome e exemplos de referência não são componentes homologados; licença ausente significa não copiar código.
10. **Human-in-the-loop:** não mesclar, publicar, fazer deploy, gastar recursos ou executar ações industriais críticas sem autorização explícita.

## Referências selecionadas — lote 1
- obra/superpowers: especificação, planejamento, TDD e YAGNI.
- Kulaxyz/self-learning-skills: golden paths, falhas e conhecimento reutilizável.
- betta-tech/ejemplo-harness-subagentes: separação leader/implementer/reviewer, checkpoints e testes; licença ainda precisa ser confirmada.
- ikyriak/IdempotentAPI: idempotência para chamadas repetidas em sistemas distribuídos.
- modelcontextprotocol/servers: referência de protocolo MCP, não promessa de prontidão para produção.
- anthropics/skills: estrutura de skills autocontidas; revisar licença por item.
- microsoft/ai-agents-for-beginners: recurso educacional.
- SynkraAI/aiox-core e NousResearch/hermes-agent: candidatos para benchmark, não adoção automática.

## Referências selecionadas — lote 2
- **Matt Pocock Skills:** skills pequenas e composáveis; selecionar apenas as que agreguem valor frente às já existentes.
- **Archify:** diagramas versionados como documentação auxiliar; validar a fidelidade contra o código.
- **Herder:** fila durável, estados explícitos, lease/heartbeat, retries, cooldown, concorrência e permissões por job; ainda exige avaliação de maturidade.
- **Orca (ShawnCholeva/orca, identidade confirmada):** benchmark de control plane local-first, daemon como fonte de estado, eventos persistidos, workflows, memória por Goal e gates de aprovação. A licença não foi encontrada no caminho padrão; não copiar código até esclarecer. Auditar auth, CORS/WebSocket, PTY, hooks de permissão e sandbox antes de executar.
- **DeepSeek Harness:** plugin architecture como referência, mas o próprio projeto declara preview experimental sem auditoria; laboratório isolado somente.
- **OmniRoute:** roteamento/fallback entre provedores exige política de custos, privacidade, credenciais e termos.
- **AnyDoc:** referência de pesquisa para documentos editáveis; licença de pesquisa não comercial para datasets/checkpoints, sem código de treino/inferência declarado.
- **OpenMontage:** possível ferramenta adjacente para vídeos de treinamento; AGPLv3 e dependências externas exigem análise antes de adaptação.

## Gates de promoção de conhecimento
Promover um padrão apenas com versão/fonte identificadas, hipótese de uso, teste reproduzível, limitações e falhas documentadas, revisão de licença/segurança, aprovação humana, versionamento e rollback. Omarship e Mander Diffling não foram assimilados porque suas identidades não foram confirmadas.
