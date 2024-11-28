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

## Design Patterns

1. Design Pattern Criacional: Singleton
      - O que é?
         - O Singleton garante que uma classe tenha apenas uma única instância, fornecendo um ponto global de acesso a ela.

      - Como usar no nosso projeto?
         - No sistema de autenticação, o Singleton pode ser usado para gerenciar tokens de autenticação, garantindo que apenas uma instância da classe responsável por geração e validação de tokens exista.


2. Design Pattern Comportamental: Strategy
      - O que é?
         - O Strategy define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis. Ele permite que o algoritmo varie independentemente dos clientes que o utilizam.

      - Como usar no nosso projeto?
         - O Strategy será usado para permitir diferentes métodos de autenticação. Por exemplo:
         - Login por senha (via banco de dados)
         - Login por token (JWT)


3. Design Pattern Estrutural: Adapter
      - O que é?
         - O Adapter converte a interface de uma classe para outra que o cliente espera. Ele é útil para integrar sistemas que possuem interfaces incompatíveis.

      - Como usar no nosso projeto?
         - Se o sistema precisar integrar com um serviço de autenticação externo (como OAuth ou Google Auth), o Adapter pode ser usado para ajustar a interface da API externa ao sistema existente.

---

# Estrutura do Projeto

```bash
app/  
├── common/  
│   ├── user_model.py             - Arquivo que define a classe mãe `UserModel`.
│   ├── user_signin_form.py       - Arquivo que lida com a lógica de login para usuário geral.
│   └── user_signup_form.py       - Arquivo que lida com a lógica de registro para usuário geral.
│
├── customer/    
│   ├── services/
│   │   ├── form_validations.py   - Arquivo que lida com a validação de login e cadastro.
│   │   ├── signin_form.py        - Arquivo que lida com a lógica de login para clientes.
│   │   └── signup_form.py        - Arquivo que lida com a lógica de registro para clientes.
│   ├── model.py                  - Arquivo que define a classe `Customer`.         
│   └── routes.py                 - Arquivo que define as rotas específicas para os clientes.
│
├── employee/  
│   ├── services/
│   │   ├── form_validations.py   - Arquivo que lida com a validação de login e cadastro.
│   │   ├── signin_form.py        - Arquivo que lida com a lógica de login para funcionários.
│   │   └── signup_form.py        - Arquivo que lida com a lógica de registro para funcionários.
│   ├── model.py                  - Arquivo que define a classe `Employee`.         
│   └── routes.py                 - Arquivo que define as rotas específicas para os funcionários.
│
├── home/  
│   └── routes.py                 - Arquivo que define a rota específica para a página home.
│
├── templates/
│   ├── base.html                 - Template base que serve como estrutura para as outras páginas.
│   ├── customer_signin.html      - Página de login para clientes.
│   ├── customer_signup.html      - Página de cadastro para clientes.
│   ├── employee_signin.html      - Página de login para funcionários.
│   ├── employee_signup.html      - Página de cadastro para funcionários.
│   └── home.html                 - Template básico para a página home (apenas demonstração).
│
├── __init__.py                   - Arquivo de inicialização do pacote Flask.
└── jwt_helper.py                 - Criação do Token de autenticação.

config.py                         - Onde configurações básicas são definidas.
run.py                            - Arquivo principal que inicia o servidor Flask.
```   
  
## Funcionalidades

- **Página de Login**: Permite que os usuários façam login com seu email e senha. Inclui um link para a página de cadastro e um link para recuperação de senha.
- **Página de Cadastro**: Permite que os usuários se registrem com informações como nome, email, senha, confirmação de senha. Inclui validação de campos para garantir que o email seja válido e que as senhas coincidam e que tenha no mínimo 6 dígitos.

---

# **Documentação dos Endpoints - Autenticação**

Este documento descreve os endpoints disponíveis para autenticação de funcionários e clientes, além de exemplos para integração.

## **Base URL**
`http://127.0.0.1:5000/`


## **Endpoints de Funcionários (Employee)**

### **1. Login do Funcionário**
- **Endpoint**: `POST /employee-signin`
- **Descrição**: Autentica um funcionário no sistema.
- **Headers**:
  - `Content-Type: application/x-www-form-urlencoded`
- **Body (Form Data)**:
  ```text
  username=<seu_username>
  password=<sua_senha>
- Resposta (200 - OK):
   - Usuário autenticado e redirecionado
- Erros:
   - 401: Credenciais inválidas

 ### **2. Registro de Funcionário**
 - **Endpoint**: `POST /employee-signup`
- **Descrição**: Registra um funcionário no sistema.
- **Headers**:
  - `Content-Type: application/x-www-form-urlencoded`
- **Body (Form Data)**:
  ```text
  username=<seu_username>
  email=<seu_email>
  password=<sua_senha>
- Resposta (200 - OK):
   - Funcionário registrado com sucesso
- Erros:
   - 400: Dados inválidos
   - 409: Usuário já existe



## **Endpoints de CLientes (Customer)**

### **1. Login do Cliente**
- **Endpoint**: `POST /customer-signin`
- **Descrição**: Autentica um cliente no sistema.
- **Headers**:
  - `Content-Type: application/x-www-form-urlencoded`
- **Body (Form Data)**:
  ```text
  username=<seu_username>
  password=<sua_senha>
- Resposta (200 - OK):
   - Usuário autenticado e redirecionado
- Erros:
   - 401: Credenciais inválidas

 ### **2. Registro de Funcionário**
 - **Endpoint**: `POST /customer-signup`
- **Descrição**: Registra um cliente no sistema.
- **Headers**:
  - `Content-Type: application/x-www-form-urlencoded`
- **Body (Form Data)**:
  ```text
  username=<seu_username>
  email=<seu_email>
  password=<sua_senha>
- Resposta (200 - OK):
   - Cliente registrado com sucesso
- Erros:
   - 400: Dados inválidos
   - 409: Usuário já existe

---

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

![uml_comportamental-2](https://github.com/user-attachments/assets/1ee42a53-f13f-43cb-9f1d-4606b27e927a)

## Diagrama de classe

![Diagrama de Classes drawio](https://github.com/user-attachments/assets/dcffc968-b256-4cf8-bc18-2dc6c5f68856)



## Slides da apresentação 1

[Apresentação Arq Software.pptx](https://github.com/user-attachments/files/17639491/Apresentacao.Arq.Software.pptx)


