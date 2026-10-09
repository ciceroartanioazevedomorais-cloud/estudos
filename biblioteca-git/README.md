# BIBLIOTECÁRIO — Auditoria e integração da Biblioteca Git

O BIBLIOTECÁRIO transforma uma coleção de repositórios em um portfólio técnico auditável e alinhado à formação em Engenharia de IA e à arquitetura industrial JIE/AIOX/CIOS.

## Conteúdo
- `.github/agents/bibliotecario.agent.md`: instruções do agente personalizado para uso em ambientes compatíveis com agentes de repositório.
- `catalogo.yaml`: inventário inicial de 35 referências recebidas.
- `PLANTILLA-AUDITORIA.md`: ficha padronizada de auditoria por repositório.

## Fluxo operacional
1. Validar e normalizar o catálogo, incluindo duplicatas e links quebrados.
2. Auditar um repositório por vez com evidências e versão/commit identificados.
3. Priorizar projetos por aderência, valor industrial, maturidade, esforço e redução de risco.
4. Elaborar SPEC para qualquer integração proposta.
5. Fazer PoC isolada, sem credenciais reais, com dependências fixadas.
6. Executar testes e verificações de segurança; documentar lacunas.
7. Propor mudanças em branch e pull request para revisão humana.

## Limite importante
Adicionar um projeto ao catálogo não significa que foi auditado, considerado seguro ou aprovado para uso. Este commit cria a estrutura e as regras do agente; não representa a auditoria completa dos 35 projetos nem a instalação/implementação dos repositórios de terceiros.

## Próxima etapa recomendada
Auditar primeiro os fundamentos de desenvolvimento e orquestração (por exemplo, AIOX Core, Superpowers, MCP Servers, Hermes Agent e self-learning-skills), comparar sobreposições e selecionar uma única prova de conceito de baixo risco para implementação incremental.
