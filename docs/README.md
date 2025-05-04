# SETUP FOR A GOOD PYTHON PROJECT AND MODULARIZATION ([🇧🇷 Leia em Português](README_PT.md))

To begin with, you need to have an updated version of Python to avoid compromising security, as not updating can pose risks in this regard.

As a first step, create a folder where your project will be stored. In this guide, we use the **AULAN** folder and the **VSCode** editor.

---

## INITIAL SETUP

### Step 1 – `.python-version` file  
In this file, you should insert the Python version used. This prevents the infamous phrase *“it works on my machine”* from becoming a problem.

**Command**  
In the VSCode terminal, run:  
```bash
pyenv local 3.12.1
```

---

### Step 2 – Install and configure Poetry  
Poetry manages dependencies and virtual environments. This way, library versions, for example, will be registered in the generated file, without the need for you to insert them manually.

**Commands**  
```bash
pip install poetry
poetry config virtualenvs.in-project true
poetry init
```

During `poetry init`, answer:  
- **Package name:** AULAN  
- **Version:** 0.1.0  
- **Python version:** >=3.12  
- Answer **yes** to define dependencies interactively.

This generates the `pyproject.toml` file, which stores your dependencies and settings.

---

### Step 3 – Create virtual environment  
In the terminal, activate Poetry's shell with:  
```bash
poetry shell
```
This creates the hidden `.venv/` folder at the project root. With a venv, you can work with specific versions of packages without creating conflicts between projects that use Django 3.2 and others that use Django 4.0, for example.

---

### Step 4 – Install packages  
Example: installing Pandas  
```bash
poetry add pandas
```
The `pyproject.toml` and `poetry.lock` are updated automatically.

---

## GIT CONFIGURATION

### Step 1 – Initialize repository  
```bash
git init
```

To view the `.git` folder in VSCode, create or edit the `.vscode/settings.json` file with the content:  
```json
{
  "files.exclude": {
    "**/.git": false
  }
}
```

---

### Step 2 – Create `.gitignore`  
Use the [Toptal](https://www.toptal.com/developers/gitignore) generator for Python and paste the result into `.gitignore`.  
This avoids versioning temporary files, tokens, passwords, and the virtual environment, which are not necessary in the repository for security reasons, for example.

---

### Modularization:

Modularizing brings more seriousness, organization, and makes your project reusable, although it is more work lol. It allows scalability and facilitates testing.

To create modules, create a folder where your project code will be generated. In my case, an ETL project, I created the folders:

app => where the ETL programs and tests will be  
 |--- pipeline => will contain the extractor, transformer, and data loader  
 |--- test => where `.py` files for testing with pytest will be stored

For each folder, it is important to have the `__init__.py`, which allows the `pipeline` and `test` folders to be recognized as packages. In more recent versions, it is not necessary, but it remains good practice.

## CONCLUSION

With this setup, your project will have:  
- **Standardization:** Fixed Python via `.python-version`.  
- **Isolation:** Virtual environment in `.venv/`.  
- **Versioning:** Git correctly configured.  
- **Reproducibility:** Dependencies defined in `pyproject.toml`/`poetry.lock`.

---

### ⚠️ Notes

1. The `pyenv local` command only works with Pyenv installed.  
2. The adjustment in `settings.json` applies to VSCode.  
3. After `git init`, add the GitHub remote:  
   ```bash
   git remote add origin <repository-URL>
   ```
