# BIBLIOTECÁRIO — Auditoria e integração da Biblioteca Git

O BIBLIOTECÁRIO transforma uma coleção de repositórios em um portfólio técnico auditável e alinhado à formação em Engenharia de IA e à arquitetura industrial JIE/AIOX/CIOS.

## Conteúdo
- `.github/agents/bibliotecario.agent.md`: instruções do agente personalizado para uso em ambientes compatíveis com agentes de repositório.
- `catalogo.yaml`: inventário de referências recebidas, com status de identificação e prioridade inicial.
- `PLANTILLA-AUDITORIA.md`: ficha padronizada de auditoria por repositório.
- `RELATORIO-VERIFICACAO-INICIAL.md`: triagem inicial do primeiro lote.
- `RELATORIO-VERIFICACAO-LOTE-2.md`: triagem e decisões iniciais deste segundo lote.
- `PRINCIPIOS-ASSIMILADOS.md`: padrões de engenharia selecionados para JIE/AIOX/CIOS.
- `SPEC-002-HARNESS-MULTIAGENTE-INDUSTRIAL.md`: especificação da PoC própria de supervisor de jobs multiagente, com estados, idempotência, recuperação, evidências, testes e gates humanos.

## Fluxo operacional
1. Validar e normalizar o catálogo, incluindo duplicatas e links quebrados.
2. Auditar um repositório por vez com evidências e versão/commit identificados.
3. Priorizar projetos por aderência, valor industrial, esforço, maturidade e redução de risco.
4. Elaborar e revisar uma SPEC antes de qualquer integração proposta.
5. Fazer PoC isolada, sem credenciais reais, com dependências fixadas e dados sintéticos.
6. Executar testes e verificações de segurança; documentar lacunas.
7. Fazer revisão independente e propor mudanças em branch e pull request para revisão humana.
8. Promover princípios/skills à biblioteca somente com evidência reproduzível, falhas nomeadas, alternativas descartadas e possibilidade de rollback.

## Princípios de governança
- O estado real de jobs deve ser controlado por lógica determinística e persistência, não apenas pela memória do LLM.
- Toda ação mutável repetível deve ter idempotência, rastreabilidade e política de retry explícita.
- Cada job deve ter IDs correlacionáveis, eventos auditáveis, limites e tratamento de falhas.
- Worktree é isolamento de workspace, não sandbox de segurança.
- Menor privilégio, logs sem segredos e aprovação humana para merge, deploy, gastos, provisionamento e ações industriais críticas.
- Verificar licenças por artefato e dependência antes de copiar ou redistribuir código.
- Não adicionar orquestradores sobrepostos sem benchmark que demonstre benefício.

## Estado da PoC
A SPEC-002 está documentada como proposta para revisão; a implementação ainda não foi iniciada. A primeira versão deve usar apenas adaptadores simulados e dados fictícios de Qualidade Industrial. Não executar código de terceiros nem conectar sistemas industriais reais nesta fase.

## Limite importante
Adicionar um projeto ao catálogo não significa que foi auditado, considerado seguro ou aprovado para uso. As triagens são avaliações iniciais, não revisão completa de código, auditoria de CVEs ou homologação industrial. Uma licença não encontrada deve ser tratada como pendência: não copiar nem distribuir código até esclarecer.

## Pendências conhecidas
- `Omarship` e `Mander Diffling`: identidades não confirmadas; nenhum repositório será inferido sem URL ou nome exato.
- `ShawnCholeva/orca`: identidade confirmada pelo usuário; usar como benchmark documental de control plane, não como dependência aprovada, até esclarecer licença e concluir as revisões necessárias.
- `deepseek-ai/deepseek-harness`: developer preview conforme a triagem documental; restrito a laboratório isolado, não é dependência da PoC.
- `diegosouzapw/OmniRoute`: não integrar na primeira PoC; avaliar apenas se houver necessidade mensurável de roteamento multi-provedor.

## Próxima etapa recomendada
Revisar e aprovar a SPEC-002. Depois, implementar apenas a Fase 1 (máquina de estados, persistência e testes), sem LLM e sem execução arbitrária de comandos. Avançar por gates de aceite, com revisão independente antes de ampliar o escopo.
