# SETUP PARA UM BOM PROJETO EM PYTHON E MODULARIZAÇÃO

Para início de tudo, é preciso ter uma versão do Python atualizada, evitando que a segurança seja comprometida, pois a não atualização pode gerar riscos nesse sentido.

Como primeiro passo, crie uma pasta onde será armazenado seu projeto. Neste guia usamos a pasta **AULAN** e o editor **VSCode**.

---

## SETUP INICIAL

### 1º Passo – Arquivo `.python-version`
Neste arquivo, você deve inserir a versão do Python utilizada. Isso evita que a famosa frase *“na minha máquina roda”* se torne um problema.

**Comando**  
No terminal do VSCode, execute:  
```bash
pyenv local 3.12.1
```

---

### 2º Passo – Instalar e configurar o Poetry
O Poetry gerencia dependências e ambientes virtuais.

**Comandos**  
```bash
pip install poetry
poetry config virtualenvs.in-project true
poetry init
```

Durante o `poetry init`, responda:  
- **Package name:** AULAN  
- **Version:** 0.1.0  
- **Python version:** >=3.12  
- Responda **yes** para definir dependências interativamente.

Isso gera o arquivo `pyproject.toml`, que armazena suas dependências e configurações.

---

### 3º Passo – Criar ambiente virtual
No terminal, ative o shell do Poetry com:  
```bash
poetry shell
```
Isso cria a pasta oculta `.venv/` na raiz do projeto.

---

### 4º Passo – Instalar pacotes
Exemplo: instalar o Pandas  
```bash
poetry add pandas
```
O `pyproject.toml` e o `poetry.lock` são atualizados automaticamente.

---

## CONFIGURAÇÃO DO GIT

### 1º Passo – Iniciar repositório
```bash
git init
```

Para visualizar a pasta `.git` no VSCode, crie ou edite o arquivo `.vscode/settings.json` com o conteúdo:  
```json
{
  "files.exclude": {
    "**/.git": false
  }
}
```

---

### 2º Passo – Criar `.gitignore`
Use o gerador do [Toptal](https://www.toptal.com/developers/gitignore) para Python e cole o resultado em `.gitignore`.  
Isso evita versionar arquivos temporários, tokens, senhas e o ambiente virtual.

---

### Modularização:

Modularizar traz mais seriedade, organização e torna seu projeto reutilizavel, embora seja mais trabalhoso rsrsrs. Permite escalabilidade e facilita os testes.

Para criar módulos, crie uma pasta onde será gerado seus códigos para o projeto. No meu caso, um projeto de ETL, criei as pastas:

app = > onde ficará os programas do ETL e os testes
 |--- pipeline = > irá contar o extrator, transformador e o carregador do dados
 |--- test => onde armazenará os arquivos .py para teste com o pytest. 

para cada pasta é importante ter o __init__.py, que permite que as pastas pipeline e testes sejam reconhecidas como pacote, em versões mais atuais ele não é necessário, todavia continua sendo uma boa prática.

## CONCLUSÃO

Com este setup, seu projeto terá:  
- **Padronização:** Python fixo via `.python-version`.  
- **Isolamento:** ambiente virtual no `.venv/`.  
- **Versionamento:** Git configurado corretamente.  
- **Reprodutibilidade:** dependências definidas em `pyproject.toml`/`poetry.lock`.

---

### ⚠️ Observações

1. O comando `pyenv local` funciona apenas com o Pyenv instalado.  
2. O ajuste em `settings.json` vale para VSCode.  
3. Após o `git init`, adicione o remoto do GitHub:  
   ```bash
   git remote add origin <URL-do-repositório>
   ```
