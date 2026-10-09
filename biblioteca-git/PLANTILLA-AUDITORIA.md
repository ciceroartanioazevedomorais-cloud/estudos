# Plantilha de Auditoria — BIBLIOTECÁRIO

> Uma ficha por repositório. Preencha somente após verificar as fontes. Registre data, commit/tag auditado e links das evidências.

## 1. Identificação
- Nome e URL:
- Data da auditoria:
- Commit/tag/versão examinada:
- Mantenedor/organização:
- Licença e evidência:
- Estado: ativo / lento / arquivado / indisponível / não verificado
- Objetivo declarado e finalidade observada:

## 2. Resumo executivo
- O que faz:
- Problema que resolve:
- Valor educacional para Engenharia de IA:
- Aplicação possível em Qualidade, PCP, Segurança, Meio Ambiente ou SGI:
- Recomendação: adotar / PoC / extrair padrão / estudar / arquivar / bloquear

## 3. Maturidade e evidências
Pontue 0–5, justifique e cite evidência:
| Dimensão | Nota | Evidência | Confiança |
|---|---:|---|---|
| Releases/versionamento | | | |
| Documentação | | | |
| Testes e cobertura disponível | | | |
| CI/CD e qualidade | | | |
| Atividade/manutenção | | | |
| Comunidade e resposta | | | |
| Segurança e política de divulgação | | | |
| Facilidade de reprodução | | | |

## 4. Dependências e operação
- Linguagens e versões:
- Runtime/sistema operacional:
- Dependências diretas:
- Lockfiles e estratégia de fixação:
- Serviços externos/APIs:
- Secrets e permissões necessários:
- Dados enviados a terceiros:
- Custo operacional/licenças de serviço:
- Dependências críticas e risco de abandono:
- Comandos de instalação/teste (não executar antes de revisar):

## 5. Modelo de ameaças e riscos
| Risco | Probabilidade | Impacto | Severidade | Mitigação | Bloqueador? |
|---|---|---|---|---|---|
| Execução de código externo | | | | | |
| Dependência/supply chain | | | | | |
| Credenciais e permissões | | | | | |
| Privacidade/exfiltração | | | | | |
| Prompt injection/instruções não confiáveis | | | | | |
| Licença/atribuição | | | | | |
| Lock-in/custo/indisponibilidade | | | | | |

## 6. Score de decisão
- Maturidade (20%):
- Manutenção (15%):
- Segurança/supply chain (20%):
- Compatibilidade (15%):
- Aderência aos objetivos (20%):
- Custo/reversibilidade (10%):
- Score ponderado 0–100:
- Confiança geral: alta / média / baixa
- Lacunas que podem alterar a decisão:

O score é apoio à decisão, não certificação de segurança. Ausência de evidência não equivale a aprovação.

## 7. Integração com JIE/AIOX/CIOS
- Camada/componente-alvo:
- Interfaces: API / CLI / MCP / biblioteca / serviço / skill / agente:
- Fluxo de dados:
- Autenticação e autorização:
- Observabilidade/logs/tracing:
- Idempotência e tratamento de falhas:
- Isolamento/worktree/container:
- Validação humana:
- Alternativas mais simples:
- Sobreposição com outros projetos:
- Estratégia de rollback/desinstalação:

## 8. Prioridade
Avalie 0–5:
- Aderência aos objetivos (30%):
- Benefício técnico/industrial (25%):
- Prontidão/maturidade (20%):
- Esforço inverso (15%):
- Redução de risco/desbloqueio (10%):
- Prioridade: P0 / P1 / P2 / P3 / BLOQUEADO
- Estimativa de esforço e premissas:

## 9. PoC e critérios de aceite
- Hipótese a validar:
- Escopo mínimo:
- Ambiente isolado:
- Versões/commits fixados:
- Testes e verificações:
- Dados sintéticos/anonimizados:
- Critérios objetivos de sucesso:
- Critérios de parada:
- Plano de rollback:
- Aprovação humana necessária:

## 10. Decisão final e histórico
- Decisão:
- Justificativa:
- O que será reutilizado: código / padrão arquitetural / documentação / nenhum:
- Restrições de licença e atribuição:
- Responsável pela revisão:
- Próxima ação:
- Evidências e fontes:
