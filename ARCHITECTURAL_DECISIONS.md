# Documentação Técnica e Decisões de Arquitetura

## Arquitetura em Camadas

A API foi refatorada seguindo uma arquitetura em camadas para separar responsabilidades e facilitar a manutenção e testes.

- **`app/api` (Controller)**: Define os endpoints da API usando FastAPI. Responsável por receber requisições HTTP e delegar para os serviços.
- **`app/services` (Service)**: Contém a lógica de negócio. Validações e orquestração entre repositórios acontecem aqui.
- **`app/repositories` (Repository)**: Responsável pelo acesso aos dados. Atualmente utiliza uma implementação em memória, mas pode ser facilmente substituída por um banco de dados real.
- **`app/models` (Domain Model)**: Representa as entidades de domínio da aplicação.
- **`app/schemas` (Data Transfer Objects - DTOs)**: Define os modelos Pydantic para validação de entrada e saída.
- **`app/core`**: Configurações globais e exceções customizadas.

## Princípios SOLID Aplicados

- **S (Single Responsibility Principle)**: Cada classe e módulo tem uma única responsabilidade (ex: `UserRepository` cuida apenas de dados, `UserService` apenas de lógica de negócio).
- **O (Open/Closed Principle)**: O sistema é extensível. Novos tipos de persistência podem ser adicionados sem alterar a lógica de negócio.
- **L (Liskov Substitution Principle)**: As abstrações permitem que implementações sejam trocadas sem quebrar o sistema.
- **I (Interface Segregation Principle)**: As interfaces (ou classes com métodos específicos) garantem que os clientes dependam apenas do que usam.
- **D (Dependency Inversion Principle)**: O `UserService` depende de uma abstração do repositório, facilitando a injeção de dependências e testes.

## Tratamento de Exceções

Foi implementado um tratamento global de exceções no `app/main.py` usando `exception_handlers`. Isso garante respostas consistentes da API em caso de erros de negócio, como idade inválida.

## Sugestões de Melhoria de Performance

1. **Persistência Real**: Substituir a lista em memória por um banco de dados como PostgreSQL ou Redis para persistência real e consultas mais rápidas.
2. **Asincronicidade**: Utilizar `async` e `await` em todas as operações de I/O (repositório e serviço) para não bloquear o loop de eventos do FastAPI.
3. **Caching**: Implementar cache (ex: Redis) para endpoints de leitura frequente como `GET /users`.
4. **Paginação**: Adicionar paginação ao endpoint `GET /users` para evitar sobrecarga ao retornar grandes volumes de dados.
5. **Gunicorn/Uvicorn**: Em produção, utilizar Gunicorn com workers Uvicorn para gerenciar múltiplos processos e aumentar o throughput.

## Testes

Os testes foram escritos utilizando `pytest` e `httpx`, cobrindo os casos de sucesso e erro da API.
