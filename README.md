# arquitetura_mvc

Projeto em **Python** utilizando o padrão **MVC (Model-View-Controller)**, implementado para organização de rotas, conexão com banco de dados e boas práticas de desenvolvimento.

## 📂 Estrutura do Projeto

```
arquitetura_mvc/
│── .vscode/                  # Configurações do VSCode
│── init/                     # Configurações de inicialização do projeto
│── scripts/                  # Scripts auxiliares
│── src/                      # Código-fonte principal
│   ├── models/               # Modelos e entidades
│   ├── controllers/          # Controladores
│   ├── views/                # Interfaces e tipos de resposta
│── .gitignore                # Arquivos ignorados pelo Git
│── .pre-commit-config.yaml   # Hooks de pré-commit
│── .pylintrc                 # Configuração do Pylint
│── case.py                   # Configuração de sessão para banco de dados
│── ex_pylint.py              # Exemplo de uso com Pylint
│── requirements.txt          # Dependências do projeto
│── run.py                    # Arquivo principal para rodar a aplicação
```

## ⚙️ Tecnologias Utilizadas

- **Python 3.10+**
- **Flask** (framework web)
- **SQLAlchemy** (ORM e conexão com banco)
- **PyLint** (análise estática de código)
- **Pre-commit hooks** (garantir qualidade de código)

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/Guihauck/arquitetura_mvc.git
   cd arquitetura_mvc
   ```

2. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o projeto:
   ```bash
   python run.py
   ```

5. Acesse no navegador:
   ```
   http://localhost:5000
   ```

## 🧪 Testes e Qualidade de Código

Rodar os testes e validações de estilo:

```bash
pytest
pylint src/
```

## 📌 Funcionalidades

- Estrutura organizada em **MVC**
- Rotas para gerenciamento de **pets** e **pessoas**
- Conexão com banco de dados via SQLAlchemy
- Configuração de **hooks de pré-commit**
- Integração com **Pylint**

## 📄 Licença

Este projeto está sob a licença MIT – sinta-se livre para usar e modificar.
