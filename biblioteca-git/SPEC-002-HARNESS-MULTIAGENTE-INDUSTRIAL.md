# SPEC-002 — PoC de Harness Multiagente Industrial

- **Status:** proposta pronta para revisão humana; implementação não iniciada
- **Versão:** 1.0
- **Contexto:** Biblioteca Git / JIE / AIOX / CIOS
- **Referências de benchmark:** `ShawnCholeva/orca` (identidade confirmada pelo usuário), `cleonhp88/herder`, `obra/superpowers`, `Kulaxyz/self-learning-skills`, `ikyriak/IdempotentAPI`
- **Regra de uso:** referências orientam decisões; não copiar código de repositórios com licença ausente ou não esclarecida.

## 1. Objetivo

Definir uma prova de conceito própria, pequena e verificável, para supervisionar jobs de agentes e demonstrar os controles necessários antes de integrar capacidades ao JIE/AIOX/CIOS. O sistema deve tornar a execução **controlável, observável e verificável** antes de tentar aumentar a autonomia dos agentes.

## 2. Problema e hipótese

Jobs de agentes podem falhar, repetir ações, perder estado ou produzir conclusões sem evidências. A hipótese é que uma camada determinística de controle — estados explícitos, persistência, idempotência, permissões, logs e validação independente — reduz falhas operacionais e torna os resultados auditáveis.

## 3. Escopo da PoC

### Incluído
- Criar, consultar, iniciar, cancelar e concluir jobs com identificador único.
- Máquina de estados explícita: `QUEUED`, `RUNNING`, `WAITING_APPROVAL`, `SUCCEEDED`, `FAILED`, `CANCELLED`.
- Persistir estado e eventos em banco local de desenvolvimento.
- Registrar tentativas, timestamps, causa de falha, resultado e referências a evidências.
- Retry limitado e configurável; backoff; prevenção de execução simultânea indevida.
- Idempotência para comandos repetíveis e alterações de estado.
- Heartbeat/lease para detectar jobs abandonados; recuperação documentada após reinício.
- Limites de tempo, tamanho de saída e concorrência.
- Separação de papéis: Orchestrator/Planner, Executor e Validator.
- Aprovação humana antes de qualquer ação fora do escopo seguro da simulação.
- Um fluxo demonstrativo de Qualidade Industrial com dados inteiramente fictícios: recebimento de uma não conformidade, classificação, sugestão de análise FMEA/DMAIC e validação por agente revisor.
- Testes automatizados, logs estruturados e instruções de reprodução.

### Excluído
- Execução de código de terceiros como parte do runtime.
- Acesso a sistemas industriais, ERP/MES/SCADA, máquinas, dispositivos ou dados reais.
- Credenciais, tokens, segredos e chamadas a provedores pagos.
- Deploy em produção, execução privilegiada, autoaprovação ou alteração autônoma de registros oficiais.
- Treinamento/fine-tuning de modelos.
- Construir uma nova plataforma desktop completa antes de validar o núcleo.

## 4. Usuários e cenário principal

**Usuário primário:** desenvolvedor/operador da arquitetura JIE/AIOX/CIOS.

**Cenário:** o operador submete um job simulado de análise de não conformidade. O Planner define etapas; o Executor produz artefatos fictícios; o Validator verifica esquema, completude e evidências. Se uma etapa falha, o supervisor registra o evento e aplica retry limitado. O job só é concluído se os critérios de aceite forem satisfeitos.

## 5. Arquitetura proposta

1. **API/CLI local:** entrada validada por esquema; autenticação local se houver superfície de rede.
2. **Job Controller:** máquina de estados determinística, transições permitidas e cancelamento.
3. **Queue/Scheduler:** concorrência limitada, leases/heartbeats, retry e timeout.
4. **Execution Adapter:** interface substituível; inicialmente executa funções simuladas, não shell arbitrário.
5. **Persistence:** SQLite local para jobs, tentativas, eventos e chaves de idempotência.
6. **Evidence Store:** artefatos de saída e metadados com hashes; sem segredos nos logs.
7. **Validator:** verifica contrato de saída, critérios de aceite, evidências e invariantes.
8. **Human Approval Gate:** bloqueia transições que exijam aprovação.
9. **Observability:** logs estruturados correlacionados por `task_id`, `run_id` e `attempt_id`; métricas de duração, retries e falhas.

### Fluxo

`Input → Schema Validation → Planner → DAG/Job Plan → Approval Gate (quando aplicável) → Executor → Evidence Capture → Independent Validator → State Commit → Audit Trail`

O LLM não deve ser a fonte de verdade do estado. A persistência e as transições são controladas por lógica determinística.

## 6. Contratos de dados mínimos

- `task_id`: identificador estável da tarefa lógica.
- `run_id`: identificador de uma execução.
- `attempt_id`: identificador de cada tentativa.
- `idempotency_key`: chave para impedir efeitos duplicados.
- `status`: estado atual validado pelo controlador.
- `created_at`, `started_at`, `finished_at`: timestamps.
- `input_ref`, `output_ref`: referências a artefatos, não segredos.
- `error_code`, `error_summary`: falha sanitizada.
- `approval_status`, `approved_by`, `approved_at`: trilha de aprovação quando necessária.
- `events`: eventos append-only para auditoria.

## 7. Requisitos não funcionais e controles

- **Segurança:** menor privilégio; nenhum segredo em prompt, fixture ou log; sem shell arbitrário na primeira versão.
- **Isolamento:** diretório temporário por job e limpeza verificável; se forem adicionados worktrees, lembrar que worktree isola workspace, não é sandbox de segurança.
- **Confiabilidade:** transições atômicas, retry limitado, idempotência, recuperação após crash e tratamento explícito de estados incompletos.
- **Observabilidade:** todos os eventos correlacionáveis; falhas e retries mensuráveis.
- **Reprodutibilidade:** dependências e versões fixadas; comandos de setup/teste documentados.
- **Privacidade:** dados sintéticos; retenção mínima; logs sem conteúdo sensível.
- **Licenciamento:** revisar licenças de código, modelos, datasets, assets e dependências separadamente antes de qualquer reutilização.
- **Human-in-the-loop:** revisão obrigatória para merge, deploy, gastos, provisionamento e ações industriais críticas.

## 8. Idempotência e política de retry

1. Cada comando mutável exige chave de idempotência e resultado persistido.
2. Repetir a mesma chave e o mesmo payload retorna o resultado conhecido; a mesma chave com payload divergente deve falhar de forma explícita.
3. Retries só ocorrem para falhas classificadas como transitórias e dentro do limite configurado.
4. Não repetir automaticamente efeitos externos não idempotentes.
5. Para ações não idempotentes, exigir compensação definida ou aprovação humana.
6. Cada retry gera novo `attempt_id`, sem apagar o histórico anterior.

## 9. Estratégia de testes

- Testes unitários da máquina de estados e das transições proibidas.
- Testes de idempotência para chamadas repetidas e payload divergente.
- Testes de concorrência para impedir que o mesmo job seja executado duas vezes.
- Testes de retry limitado, timeout, cancelamento e heartbeat expirado.
- Teste de reinício/crash com recuperação do estado persistido.
- Testes do Validator com evidência ausente, esquema inválido e resultado inconsistente.
- Teste de sanitização para assegurar que tokens/segredos não apareçam nos logs.
- Testes de integração exclusivamente com adaptadores simulados e dados fictícios.
- Revisão independente do desenho e dos resultados antes de promover padrões para a biblioteca.

## 10. Critérios de aceite (Definition of Done)

- [ ] Todos os estados e transições permitidas/proibidas estão documentados e testados.
- [ ] Repetir um comando mutável com a mesma chave não duplica o efeito.
- [ ] Falhas e retries ficam registrados com IDs correlacionáveis.
- [ ] Um job abandonado é detectado e recuperado ou marcado para revisão, sem execução duplicada silenciosa.
- [ ] Um resultado inválido é rejeitado pelo Validator.
- [ ] O reinício do processo não apaga o histórico nem inventa sucesso.
- [ ] Nenhum segredo ou sistema industrial real é necessário para executar a PoC.
- [ ] Todos os testes passam em ambiente limpo com dependências fixadas.
- [ ] README contém passos reproduzíveis e limitações conhecidas.
- [ ] Reviewer independente verifica evidências, riscos e critérios de aceite.

## 11. Fases de implementação

1. **Fase 0 — Design review:** confirmar escopo, contratos, estados, ameaças e critérios de aceite.
2. **Fase 1 — Núcleo determinístico:** estados, persistência, eventos e testes; sem LLM.
3. **Fase 2 — Idempotência e recuperação:** chaves, retries, leases, crash recovery.
4. **Fase 3 — Simulação multiagente:** Planner/Executor/Validator com adaptadores falsos.
5. **Fase 4 — Observabilidade e threat review:** métricas, sanitização, revisão independente.
6. **Fase 5 — Decisão:** comparar resultados com baseline simples; integrar apenas se houver ganho demonstrável.

Não avançar de fase se critérios da fase anterior falharem.

## 12. Métricas de avaliação

- Taxa de jobs concluídos corretamente.
- Taxa de duplicação de efeitos (meta: zero nos testes de idempotência).
- Taxa de recuperação correta após falha/reinício.
- Número de transições inválidas aceitas (meta: zero).
- Percentual de jobs com evidências completas.
- Retries por job, tempo de execução e taxa de falhas por classe.
- Custo por execução apenas quando houver avaliação posterior com provedores reais autorizados.

## 13. Riscos e decisões em aberto

- Escolha da stack final deve seguir a menor composição útil; começar simples e só introduzir componentes após medir necessidade.
- Orca serve como benchmark de control plane, não como dependência aprovada: licença não localizada na consulta anterior e riscos técnicos ainda pendentes.
- Herder serve como benchmark de filas/heartbeats/retries, não como código aprovado.
- DeepSeek Harness permanece restrito a laboratório isolado, conforme triagem documental; não é dependência desta PoC.
- Não integrar OmniRoute nesta fase; roteamento de modelos aumenta superfície de credenciais, privacidade, quotas e custos sem ser necessário para validar o supervisor.
- Skills de engenharia devem ser selecionadas individualmente e comparadas com Superpowers para evitar duplicação.
- A PoC não será considerada sistema industrial certificado nem apto para produção.

## 14. Evidências exigidas antes de adoção

- SPEC aprovada e threat model revisado.
- Repositório e commit exatos das referências de benchmark registrados.
- Licenças e dependências revisadas para qualquer componente reutilizado.
- Testes reproduzíveis e relatórios de execução.
- Revisão independente de segurança e arquitetura.
- Comparação com baseline sem harness.
- Aprovação humana documentada para qualquer ampliação de escopo.

## 15. Referências

- Orca: https://github.com/ShawnCholeva/orca
- Herder: https://github.com/cleonhp88/herder
- Superpowers: https://github.com/obra/superpowers
- Self-Learning Skills: https://github.com/Kulaxyz/self-learning-skills
- IdempotentAPI: https://github.com/ikyriak/IdempotentAPI
- DeepSeek Harness: https://github.com/deepseek-ai/deepseek-harness
- OmniRoute: https://github.com/diegosouzapw/OmniRoute

**Nota de auditoria:** esta SPEC é um documento de design. Não significa que o código foi implementado, que terceiros foram executados, nem que segurança/licenças foram integralmente auditadas.
