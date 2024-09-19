# Projeto Flask - Sistema de Autenticação e Cadastro

Este projeto é um sistema simples de autenticação e cadastro desenvolvido em Flask. O aplicativo permite que os usuários se registrem e façam login, com validação de campos de entrada e mensagens de erro.

## Funcionalidades

- **Página de Login**: Permite que os usuários façam login com seu nome de usuário e senha. Inclui um link para a página de cadastro e um link para recuperação de senha.
- **Página de Cadastro**: Permite que os usuários se registrem com informações como nome, email, confirmação de email, senha, confirmação de senha e data de nascimento. Inclui validação de campos para garantir que os emails e senhas coincidam e que a senha tenha no mínimo 8 dígitos.

## Estrutura do Projeto

- **`app.py`**: Arquivo principal do Flask que define as rotas e inicia o servidor.
- **`templates/`**: Diretório que contém os arquivos HTML do projeto.
  - **`login.html`**: Página de login.
  - **`signup.html`**: Página de cadastro.
- **`static/`**: Diretório que contém arquivos estáticos, como CSS e imagens.
  - **`css/styles.css`**: Arquivo de estilo para as páginas HTML.

## Configuração

1. **Instale as dependências**:
   - Certifique-se de ter o [Python](https://www.python.org/) instalado.
   - Instale Flask e outras dependências necessárias usando pip:
     ```bash
     pip install flask
     ```

2. **Estrutura de Diretórios**:
   - Crie o diretório do projeto e a estrutura de diretórios conforme mostrado:
     ```
     projeto/
     ├── app.py
     ├── static/
     │   └── css/
     │       └── styles.css
     └── templates/
         ├── login.html
         └── signup.html
     ```

3. **Executando o Projeto**:
   - Navegue até o diretório do projeto e execute o aplicativo Flask:
     ```bash
     python app.py
     ```
   - O aplicativo estará disponível em `http://localhost:5000`.

## Detalhes das Páginas

### `login.html`

- Campos: Nome de usuário, senha.
- Botões: "Fazer Login", "Cadastrar" (redireciona para a página de cadastro).

### `signup.html`

- Campos: Nome, email, confirmação de email, senha, confirmação de senha, data de nascimento.
- Validações: Verificação de igualdade entre emails e senhas, comprimento mínimo de 8 dígitos para senha.

## Contribuindo

Contribuições são bem-vindas! Para contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações.
3. Faça um commit e envie suas alterações.
4. Envie um pull request para revisão.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT). Veja o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato com [seu-email@example.com](mailto:seu-email@example.com).
