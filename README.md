
SETUP PARA UM BOM PROJETO EM PYTHON E MODULARIZAÇÃO

Para inicio de tudo, é preciso ter uma versão do python atualizada, evitando que a segurança seja comprometida, pois a não atualização pode gerar riscos nesse sentido.

Como primeiro passo, crie uma pasta onde será armazenada seu projeto, neste projeto foi a Pasta AULAN, e foi utilizado o VSCode para a criação do projeto

---- SETUP INICIAL ----

1º Passo - Arquivo - python-version

 - Neste arquivo, você deve inserir a versão do python utilizada, isso também evita que a famosa frase "na minha máquina roda" seja uma realidade no seu projeto.
 
 Comando:

  Para realizar essa tarefa, vá no terminal do seu VScode
  - pyenv local x.xx.x, onde x é a versão, que neste meu caso foi 3.12.1


2º Instalar seu gerenciador, no caso o poetry

Dentro da sua pasta do projeto, utilize os comandos:

 - pip install => instala o poetry
 
 - poetry config virtualenvs.in-project true => permite a criação de ambientes virtuais no seu projeto
 
 - poetry init => iniciar o gerenciamento

 Após o init, será perguntado:

  - Package name ['nome_da_sua_pasta']:
  - Version [0.1.0]:  
  - Description []:  
  - Author [DANIEL-BONFIM, n to skip]:   
  - License []:  
  - Compatible Python versions [>=3.12]:  
  - Would you like to define your main dependencies interactively? (yes/no) [yes]
  - Package to add or search for (leave blank to skip):
  - Would you like to define your development dependencies interactively? (yes/no)
  - Do you confirm generation? (yes/no) 

  Você pode adicionar uma descrição, licença e etc, de modo geral, responda yes para todas as demais perguntas


Será criado um arquivo pyproject.toml onde ele será alterado dinamicamente quando vocÊ adicionar uma biblioteca com a versão xxx, logo de cara você poderá ver a sua versão do python usada.

3º Poetry Shell para criar o venv

Para criar seu ambiente virtual, basta, ainda no termninal do VSCODE, digitar o comando poetry sheel e uma pasta chamada ".venv" será criada, onde vocÊ irá instalar seus pacotes como pandas e etc.

Agora seu projeto vai rodar independentemente da máquina que o rodar, mas não é o fim...

4º Instalar pacotes com o venv

Agora para instalar seus pacotes, utilize o comando poetry add, por exemplo:

  poetry add pandas

O pandas, neste exemplo, seria instalado no seu ambiente virtual, garantindo que quando baixar seu repositório será possível rodar o programa sem a necessidade de instalar novamente o pacote.

---- GIT ----

Para um bom projeto, versionamento é fundamental, por isso, vamos trabalhar com GIT a partir de agora:

1º Com o git instalado, rode o comando:

 - git init

 Será gerado uma pasta .git, porém ela pode estar oculta! para que sempre esteja aparente crie um arquivo:

  config.json

 Cujo conteúdo será:

{
  "files.exclude"{
    "**/git":false
  }
}

2º gitignore

O gitignore permite voê ignorar arquivos desnecessários de se subir no repositorio como o ambiente virtual ou informações criticas como token e senhas.

Para isso, basta criar este arquivo .gitignore e inserir o que não se quer versionar e subir no repositorio.

no site: https://www.toptal.com/developers/gitignore você pode pegar um padrão de ignores para o seu git, pesquisando por python, copiando e colando o resultado da pesquisa em seu gitignore.



