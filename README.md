# Projeto Flask - Sistema de Autenticação e Cadastro

Este projeto é um sistema simples de autenticação e cadastro desenvolvido em Flask. O aplicativo permite que os usuários se registrem e façam login, com validação de campos de entrada e mensagens de erro.

## SOA (Arquitetura Orientada a Serviços)

A Arquitetura Orientada a Serviços (SOA) é um estilo de design de software que permite que diferentes serviços se comuniquem entre si por meio de interfaces bem definidas. Essa abordagem é útil para criar aplicações modulares e escaláveis. 

### Principais características do SOA:

1. **Reusabilidade**: Os serviços podem ser utilizados em diferentes aplicações, promovendo a eficiência no desenvolvimento e na manutenção.
   
2. **Interoperabilidade**: Serviços construídos em diferentes tecnologias podem interagir entre si, facilitando a integração de sistemas legados e novos.

3. **Escalabilidade**: A arquitetura pode ser facilmente escalada, permitindo que serviços individuais sejam atualizados ou ampliados sem impactar toda a aplicação.

4. **Manutenção Simplificada**: As atualizações podem ser feitas em serviços individuais, reduzindo o risco de afetar outras partes da aplicação.

5. **Flexibilidade**: A adição de novos serviços ou a modificação de serviços existentes é facilitada, permitindo a adaptação às necessidades de negócios em constante mudança.

### Aplicação no Projeto:
Neste projeto de autenticação e cadastro, o SOA pode ser aplicado separando as funcionalidades relacionadas a clientes e funcionários em serviços distintos, permitindo que cada um opere de forma independente e interaja por meio de APIs.

---

## SOLID

Os princípios SOLID são cinco diretrizes que visam melhorar a qualidade do software, tornando-o mais legível, reutilizável e fácil de manter. Esses princípios são:

1. **Single Responsibility Principle (SRP)**: Uma classe deve ter uma única responsabilidade, ou seja, deve ter apenas uma razão para mudar. No projeto, cada módulo (como `login.py` e `register.py`) deve ser responsável apenas pela sua funcionalidade específica.

2. **Open/Closed Principle (OCP)**: As classes devem estar abertas para extensão, mas fechadas para modificação. Isso significa que você deve poder adicionar novas funcionalidades sem alterar o código existente. Por exemplo, ao adicionar novos métodos de autenticação, você pode criar novos serviços sem modificar os já existentes.

3. **Liskov Substitution Principle (LSP)**: Objetos de uma classe derivada devem ser substituíveis por objetos da classe base. Isso assegura que as classes derivadas não alterem o comportamento esperado da classe base.

4. **Interface Segregation Principle (ISP)**: Os clientes não devem ser forçados a depender de interfaces que não utilizam. No projeto, você pode criar interfaces específicas para cada tipo de usuário, evitando que todos compartilhem a mesma interface.

5. **Dependency Inversion Principle (DIP)**: Dependa de abstrações, não de concretizações. Isso implica que o código deve depender de interfaces ou classes abstratas em vez de classes concretas. Isso pode ser alcançado usando injeção de dependência para gerenciar instâncias de classes.

### Aplicação no Projeto:
A adoção dos princípios SOLID neste projeto ajuda a manter o código organizado e modular, facilitando a manutenção e a adição de novas funcionalidades ao sistema de autenticação e cadastro.

---

# Estrutura do Projeto

- **`run.py`**: Arquivo principal que inicia o servidor Flask.
- **`instante/`**: Diretório que contém os bancos de dados.
  - **`auth.db`**: Arquivo de banco de dados SQLite que armazena as informações de autenticação e registro dos usuários.
- **`app/`**: Diretório principal que contém os módulos da aplicação.
  - **`customer/`**: Diretório responsável pelas funcionalidades relacionadas aos clientes.
    - **`templates/`**: Diretório que contém os templates HTML específicos para clientes.
      - **`login.html`**: Página de login para clientes.
      - **`register.html`**: Página de cadastro para clientes.
    - **`routes.py`**: Arquivo que define as rotas específicas para os clientes (login e cadastro).
    - **`model.py`**: Arquivo que define a classe `Customer`, representando o modelo de dados dos clientes.
    - **`login.py`**: Arquivo que lida com a lógica de login para clientes.
    - **`register.py`**: Arquivo que lida com a lógica de registro para clientes.
  - **`employee/`**: Diretório responsável pelas funcionalidades relacionadas aos funcionários.
    - **`templates/`**: Diretório que contém os templates HTML específicos para funcionários.
      - **`login.html`**: Página de login para funcionários.
      - **`register.html`**: Página de cadastro para funcionários.
    - **`routes.py`**: Arquivo que define as rotas específicas para os funcionários (login e cadastro).
    - **`model.py`**: Arquivo que define a classe `Employee`, representando o modelo de dados dos funcionários.
    - **`login.py`**: Arquivo que lida com a lógica de login para funcionários.
    - **`register.py`**: Arquivo que lida com a lógica de registro para funcionários.
  - **`common_templates/`**: Diretório que contém os templates HTML comuns a toda a aplicação.
    - **`base.html`**: Template base que serve como estrutura para as outras páginas do projeto.
  - **`home/`**: Diretório que contém os itens básicos para a página home (apenas para demonstração).
    - **`home.html`**: Template básico para página home.
    - **`route.py`**: Arquivo que define a rota específica para a págine home.
  
## Funcionalidades

- **Página de Login**: Permite que os usuários façam login com seu email e senha. Inclui um link para a página de cadastro e um link para recuperação de senha.
- **Página de Cadastro**: Permite que os usuários se registrem com informações como nome, email, senha, confirmação de senha. Inclui validação de campos para garantir que o email seja válido e que as senhas coincidam e que tenha no mínimo 6 dígitos.

## Configuração

1. **Instale as dependências**:
   - Certifique-se de ter o [Python](https://www.python.org/) instalado.
   - Instale Flask e outras dependências necessárias usando comando abaixo:
     ```bash
     pip install -r requirements.txt
     ```

2. **Executando o Projeto**:
   - Navegue até o diretório do projeto e execute o aplicativo Flask:
     ```bash
     python run.py
     ```
   - O aplicativo estará disponível em `http://localhost:5000`.

## Detalhes das Páginas

### `home.html`

- Página apenas para demonstração de como acessar as telas de Login e Registro. (Não fazem parte desse projeto).
- Botões: "Fazer Login" (redireciona para a página de login), "Cadastrar" (redireciona para a página de cadastro).

### `login.html`

- Campos: Username, senha.
- Botões: "Esqueci minha senha", "Fazer Login", "Cadastrar" (redireciona para a página de cadastro).

### `register.html`

- Campos: Nome, email, senha, confirmação de senha.
- Validações: Verificação de email e igualdade de senhas, comprimento mínimo de 6 dígitos para senha.

## Desenho Arquitetural

<img width="641" alt="Screenshot 2024-09-19 at 18 44 05" src="https://github.com/user-attachments/assets/75eaed4a-c14b-44c3-9261-bef8155bb09c">

## Diagrama Comportamental de Atividades

![uml_comportamental-3](https://github.com/user-attachments/assets/5558a319-c052-4615-af37-f9893aa52e61)

![uml_comportamental-2](https://github.com/user-attachments/assets/1ee42a53-f13f-43cb-9f1d-4606b27e927a)


