# Projeto web para Tarefa 07 do EmbarcaTech

Este guia explica como criar e gerenciar um ambiente virtual Python usando `venv` para isolar as dependências do projeto, evitando conflitos entre diferentes projetos Python.

## Pré-requisitos

*   Python 3.3 ou superior instalado
*   Git instalado (para clonar o repositório)

## Configuração Inicial

1.  **Clone o Repositório:**
    Utilize o Git para clonar o repositório do projeto para sua máquina local.

    ```
    
    git clone https://github.com/HilquiasAbias/embarcatech-tarefa7-web.git
    ```

2.  **Navegue até o Diretório do Projeto:**
    Abra um terminal ou prompt de comando e navegue até o diretório do projeto clonado.

    ```
    
    cd embarcatech-tarefa7-web
    ```


## Criando o Ambiente Virtual

1.  **Crie o Ambiente Virtual:**
    Use o comando `python -m venv nome_do_ambiente` para criar um ambiente virtual. Substitua `nome_do_ambiente` pelo nome desejado para o seu ambiente virtual. Por convenção, usa-se `venv` ou `.venv`.

    ```
    
    python -m venv venv
    ```

    Este comando cria uma pasta chamada `venv` (ou o nome que você escolheu) que conterá o ambiente virtual.

## Ativando o Ambiente Virtual

Ativar o ambiente virtual configura o shell para usar o Python e os scripts instalados dentro do ambiente.

### No Linux/macOS

1.  **Ative o ambiente:**

    ```
    
    source venv/bin/activate
    ```

    Após a ativação, você verá o nome do ambiente virtual no início da linha de comando, indicando que o ambiente está ativo.

### No Windows

1.  **Abra o terminal:**
    Abra o prompt de comando ou PowerShell.

2.  **Ative o ambiente:**

    ```
    
    .\venv\Scripts\activate
    ```

    Da mesma forma que no Linux/macOS, o nome do ambiente virtual aparecerá no início da linha de comando.

## Instalando Dependências

Com o ambiente virtual ativado, você pode instalar as dependências do projeto listadas no arquivo `requirements.txt`.

1.  **Instale as dependências:**

    ```
    
    pip install -r requirements.txt
    ```

    Este comando lê o arquivo `requirements.txt` e instala todas as bibliotecas e suas versões especificadas.

## Desativando o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual.

  ```
  
  deactivate
  ```

## Comandos Comuns em Desenvolvimento Django

Aqui estão alguns comandos comuns que você usará ao desenvolver em Django:

1.  **Iniciar o Servidor de Desenvolvimento:**
    Para iniciar o servidor de desenvolvimento Django, use o seguinte comando:

    ```
    
    python embarcatech/manage.py runserver
    ```

2.  **Após Alterar os Models:**
    Sempre que você modificar os models (modelos de dados) do seu aplicativo, siga estes passos:

    a. **Criar Migrações (`makemigrations`):**
    Use este comando para criar uma migração que registra as mudanças nos seus models.

    ```
    
    python embarcatech/manage.py makemigrations
    ```

    b. **Aplicar Migrações (`migrate`):**
    Para aplicar as migrações e atualizar o esquema do banco de dados, use o comando `migrate`.

    ```
    
    python embarcatech/manage.py migrate
    ```

