# Projeto Flask - Sistema de Autenticação e Cadastro

Este projeto é um sistema simples de autenticação e cadastro desenvolvido em Flask. O aplicativo permite que os usuários se registrem e façam login, com validação de campos de entrada e mensagens de erro.

## Funcionalidades

- **Página de Login**: Permite que os usuários façam login com seu email e senha. Inclui um link para a página de cadastro e um link para recuperação de senha.
- **Página de Cadastro**: Permite que os usuários se registrem com informações como nome, email, senha, confirmação de senha. Inclui validação de campos para garantir que o email seja válido e que as senhas coincidam e que tenha no mínimo 6 dígitos.

# Estrutura do Projeto

- **`run.py`**: Arquivo principal que inicia o servidor Flask.
- **`instante/`**: Diretório que contém os bancos de dados.
  - **`auth.db`**: Arquivo de banco de dados SQLite que armazena as informações de autenticação e registro dos usuários.
- **`app/`**: Diretório principal que contém os módulos da aplicação.
  - **`customer/`**: Diretório responsável pelas funcionalidades relacionadas aos clientes.
    - **`templates/`**: Diretório que contém os templates HTML específicos para clientes.
      - **`login.html`**: Página de login para clientes.
      - **`register.html`**: Página de cadastro para clientes.
    - **`route.py`**: Arquivo que define as rotas específicas para os clientes (login e cadastro).
    - **`model.py`**: Arquivo que define a classe `Customer`, representando o modelo de dados dos clientes.
    - **`login.py`**: Arquivo que lida com a lógica de login para clientes.
    - **`register.py`**: Arquivo que lida com a lógica de registro para clientes.
  - **`employee/`**: Diretório responsável pelas funcionalidades relacionadas aos funcionários.
    - **`templates/`**: Diretório que contém os templates HTML específicos para funcionários.
      - **`login.html`**: Página de login para funcionários.
      - **`register.html`**: Página de cadastro para funcionários.
    - **`route.py`**: Arquivo que define as rotas específicas para os funcionários (login e cadastro).
    - **`model.py`**: Arquivo que define a classe `Employee`, representando o modelo de dados dos funcionários.
    - **`login.py`**: Arquivo que lida com a lógica de login para funcionários.
    - **`register.py`**: Arquivo que lida com a lógica de registro para funcionários.
  - **`common_templates/`**: Diretório que contém os templates HTML comuns a toda a aplicação.
    - **`base.html`**: Template base que serve como estrutura para as outras páginas do projeto.
  - **`home/`**: Diretório que contém os itens básicos apenas para demonstração.
    - **`home.html`**: Template básico para página home.
    - **`route.py`**: Arquivo que define a rota específica para a págine home.
  

## Configuração

1. **Instale as dependências**:
   - Certifique-se de ter o [Python](https://www.python.org/) instalado.
   - Instale Flask e outras dependências necessárias usando comando abaixo:
     ```bash
     pip install -r requirements.txt
     ```

2. **Estrutura de Diretórios**:
   - Crie o diretório do projeto e a estrutura de diretórios conforme mostrado:
     ```
     projeto/
     ├── main.py
     └── app
         ├── routes.py
         ├── forms.py
         ├── models.py
         └── templates/
             ├── login.html
             ├── register.html
             ├── home.html
             └── base.html
     ```

3. **Executando o Projeto**:
   - Navegue até o diretório do projeto e execute o aplicativo Flask:
     ```bash
     python main.py
     ```
   - O aplicativo estará disponível em `http://localhost:5000`.

## Detalhes das Páginas

### `home.html`

- Botões: "Fazer Login" (redireciona para a página de login), "Cadastrar" (redireciona para a página de cadastro).

### `login.html`

- Campos: Email, senha.
- Botões: "Esqueci minha senha", "Fazer Login", "Cadastrar" (redireciona para a página de cadastro).

### `register.html`

- Campos: Nome, email, senha, confirmação de senha.
- Validações: Verificação de email e igualdade de senhas, comprimento mínimo de 6 dígitos para senha.

## Desenho Arquitetural

<img width="641" alt="Screenshot 2024-09-19 at 18 44 05" src="https://github.com/user-attachments/assets/75eaed4a-c14b-44c3-9261-bef8155bb09c">
