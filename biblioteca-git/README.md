# BIBLIOTECÁRIO — Auditoria e integração da Biblioteca Git

O BIBLIOTECÁRIO transforma uma coleção de repositórios em um portfólio técnico auditável e alinhado à formação em Engenharia de IA e à arquitetura industrial JIE/AIOX/CIOS.

## Conteúdo
- `.github/agents/bibliotecario.agent.md`: instruções do agente personalizado para uso em ambientes compatíveis com agentes de repositório.
- `catalogo.yaml`: inventário de referências recebidas, com status de identificação e prioridade inicial.
- `PLANTILLA-AUDITORIA.md`: ficha padronizada de auditoria por repositório.
- `RELATORIO-VERIFICACAO-INICIAL.md`: triagem inicial do primeiro lote.
- `RELATORIO-VERIFICACAO-LOTE-2.md`: triagem e decisões iniciais deste segundo lote.
- `PRINCIPIOS-ASSIMILADOS.md`: padrões de engenharia selecionados para JIE/AIOX/CIOS.

## Fluxo operacional
1. Validar e normalizar o catálogo, incluindo duplicatas e links quebrados.
2. Auditar um repositório por vez com evidências e versão/commit identificados.
3. Priorizar projetos por aderência, valor industrial, esforço, maturidade e redução de risco.
4. Elaborar SPEC para qualquer integração proposta.
5. Fazer PoC isolada, sem credenciais reais, com dependências fixadas.
6. Executar testes e verificações de segurança; documentar lacunas.
7. Propor mudanças em branch e pull request para revisão humana.

## Limite importante
Adicionar um projeto ao catálogo não significa que foi auditado, considerado seguro ou aprovado para uso. As triagens são avaliações iniciais, não revisão completa de código, auditoria de CVEs ou homologação industrial.

## Próxima etapa recomendada
Priorizar a comparação de skills de engenharia e a criação de uma PoC própria de supervisor de jobs de agentes, usando SPEC-first, idempotência, isolamento por tarefa, observabilidade, permissões mínimas e revisão independente. Não adotar outro orquestrador completo sem benchmark.
