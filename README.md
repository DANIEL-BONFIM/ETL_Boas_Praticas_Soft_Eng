# SETUP PARA UM BOM PROJETO EM PYTHON E MODULARIZAÇÃO

Para início de tudo, é preciso ter uma versão do Python atualizada, evitando que a segurança seja comprometida, pois a não atualização pode gerar riscos nesse sentido.

Como primeiro passo, crie uma pasta onde será armazenada seu projeto. Neste projeto foi utilizada a Pasta *AULAN*, e o editor escolhido foi o **VSCode**.

---

## SETUP INICIAL

### 1º Passo - Arquivo `.python-version`
Neste arquivo, você deve inserir a versão do Python utilizada. Isso evita que a famosa frase *"na minha máquina roda"* se torne um problema.

**Comando:**  
No terminal do VSCode, execute:  
`pyenv local x.xx.x` (exemplo: `3.12.1`).

---

### 2º Passo - Instalar e configurar o Poetry
O Poetry gerencia dependências e ambientes virtuais.

**Comandos:**  
`pip install poetry` (instala o Poetry)  
`poetry config virtualenvs.in-project true` (cria ambiente virtual dentro do projeto)  
`poetry init` (inicia configuração do projeto)

**Durante o `poetry init`:**  
- **Package name:** Use o nome da pasta (ex: `AULAN`).  
- **Version:** `0.1.0` (padrão).  
- **Python version:** `>=3.12` (ajuste conforme sua versão).  
- Responda `yes` para dependências interativas.  

Será criado o arquivo `pyproject.toml`, que armazena dependências e configurações.

---

### 3º Passo - Criar ambiente virtual
Execute no terminal:  
`poetry shell`  
Isso cria a pasta `.venv` com o ambiente isolado.

---

### 4º Passo - Instalar pacotes
Exemplo de instalação do Pandas:  
`poetry add pandas`  
As dependências serão automaticamente registradas no `pyproject.toml`.

---

## CONFIGURAÇÃO DO GIT

### 1º Passo - Iniciar repositório
`git init`

Para visualizar a pasta `.git` no VSCode, crie um arquivo `.vscode/settings.json` com:
```json
{
  "files.exclude": {
    "**/.git": false
  }
}

## CONFIGURAÇÃO DO GIT

### 2º Passo - Criar `.gitignore`
Use o gerador do [Toptal](https://www.toptal.com/developers/gitignore) para Python.  
Cole o conteúdo no arquivo `.gitignore` para ignorar arquivos temporários, senhas e o ambiente virtual.

---

## CONCLUSÃO
Com esse setup, seu projeto terá:  
- **Padronização:** Versão do Python fixa via `.python-version`.  
- **Isolamento:** Ambiente virtual gerenciado pelo Poetry.  
- **Versionamento:** Git configurado para evitar arquivos sensíveis.  
- **Reprodutibilidade:** `pyproject.toml` garante instalação fácil em qualquer máquina.

---

### ⚠️ Observações Importantes
1. **Pyenv:** O comando `pyenv local` só funciona se você já tiver o Pyenv instalado.  
2. **VSCode:** O ajuste em `settings.json` é específico para esse editor.  
3. **Git Remote:** Após o `git init`, conecte ao GitHub com `git remote add origin <URL>`.