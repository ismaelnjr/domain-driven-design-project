# Projeto: Carros Antigos - Design Driven Development (DDD)

## Descrição Geral
Este projeto implementa um sistema baseado no paradigma de Domain-Driven Design (DDD) para gerenciar informações de carros antigos. Ele é composto por camadas bem definidas para garantir separação de responsabilidades, facilidade de manutenção e expansão do código.

## Estrutura do Projeto
O projeto segue a divisão clássica de DDD:

### 1. **Domínio (`domain`)**
Responsável por conter as regras de negócio e abstrações principais.

- **Entities:**
  - `car.py`: Representa um carro com atributos como marca, modelo, ano, e especificações.
  - `car_model.py`: Representa um modelo de carro.
- **Value Objects:**
  - `car_specification.py`: Define especificações detalhadas do carro (ex: cor, tipo de motor).
- **Interfaces:**
  - `model_repository_interface.py`: Define um contrato para os repositórios que gerenciam modelos de carro.

### 2. **Serviços de Aplicação (`application/services`):**
Camada responsável por coordenar casos de uso e interagir com os repositórios e entidades.

- `car_model_service.py`: Contém lógica para gerenciar modelos de carro.
- `car_service.py`: Fornece serviços para gerenciar informações de carros.

### 3. **Infraestrutura e Repositórios (`repositories`):**
Implementações específicas para persistência de dados.

- `sqlite_model_repository.py`: Repositório para manipulação de modelos de carro em um banco SQLite.

### 4. **Banco de Dados (`database`):**
Configurações e modelo de persistência.

- `database.py`: Conexão e manipulação do banco de dados SQLite.
- `orm/models.py`: Mapeamento das entidades para o banco de dados.

### 5. **Caso de Uso (`main.py`):**
Demonstra a utilização das camadas e serviços para executar operações no sistema, como:
- Criação de modelos de carros.
- Listagem de carros.
- Consulta detalhada com base nas especificações.

## Requisitos
- Python 3.9 ou superior.
- SQLite.
- Pacotes adicionais listados em `requirements.txt` (gerar o arquivo com `pip freeze > requirements.txt`, caso ainda não exista).

## Como Executar

1. **Instalação dos Pacotes:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configuração do Banco de Dados:**
   Execute `migrate.py` para criar e popular as tabelas no SQLite:
   ```bash
   python migrate.py
   ```

3. **Executar o Caso de Uso:**
   Rode o script principal para interagir com o sistema:
   ```bash
   python main.py
   ```

## Estrutura de Pastas
```
/
|-- application/
|   |-- services/
|-- database/
|-- domain/
|   |-- entities/
|   |-- interfaces/
|   |-- value_objects/
|-- repositories/
|-- main.py
|-- migrate.py
|-- carros.db
```

## Explicação do Design DDD

1. **Separar Responsabilidades:**
   O projeto está organizado em camadas bem definidas para que as regras de negócio fiquem isoladas de detalhes de infraestrutura.

2. **Camada de Domínio:**
   Foca nas abstrações essenciais, como entidades e objetos de valor. Isso facilita a compreensão e expansão das regras de negócio.

3. **Camada de Aplicação:**
   Essa camada é responsável por coordenar operações, mantendo a simplicidade e garantindo que o domínio não seja sobrecarregado com detalhes de implementação.

4. **Camada de Infraestrutura:**
   Define a persistência dos dados e os repositórios que implementam interfaces do domínio, permitindo substituição sem impacto nas outras camadas.

## Contribuições
Pull requests e issues são bem-vindos para melhorias no design e implementação.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

