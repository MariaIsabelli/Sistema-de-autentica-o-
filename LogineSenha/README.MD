# 📋 Cadastro de Usuários com Flask e SQLite

Este projeto é um aplicativo web simples desenvolvido em **Python** usando o framework **Flask**, que permite cadastrar usuários com **nome**, **login** e **senha**, salvando as informações em um banco de dados **SQLite**.  
O sistema também registra automaticamente a **data do cadastro** e exibe mensagens de sucesso ou erro.

---

## 🚀 Tecnologias utilizadas
- **Python 3**
- **Flask** (framework web)
- **SQLite** (banco de dados)
- **Bootstrap 5** (estilização do front-end)

---

## 📂 Estrutura do projeto
meu_cadastro/
│
├── app.py # Arquivo principal da aplicação Flask
├── usuarios.db # Banco de dados SQLite (criado automaticamente)
├── requirements.txt # Dependências do projeto
└── templates/
├── index.html # Página inicial com formulário de cadastro
└── sucesso.html # Página de sucesso após cadastro


---

## ⚙️ Funcionalidades
- Cadastro de usuário com:
  - Nome
  - Login (único)
  - Senha
- Registro automático da **data de cadastro**
- Validação para evitar logins duplicados
- Mensagens de feedback para o usuário
- Interface responsiva com **Bootstrap 5**

---

## 📦 Como instalar e rodar
### 1️⃣ Clonar este repositório

    git clone https://github.com/seu-usuario/meu_cadastro.git
    cd meu_cadastro

### 2️⃣ Criar ambiente virtual
    ython -m venv venv

### 3️⃣ Ativar o ambiente virtual
    Windows
    venv\Scripts\activate
    Linux/Mac
    source venv/bin/activate

### 4️⃣ Instalar as dependências
    pip install -r requirements.txt

### 5️⃣ Rodar o projeto
    python app.py


