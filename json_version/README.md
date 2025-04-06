# How works

- Agendador de tarefas que apenas faz um GET para uma url específica, desenvolvido para o PHP.


## Backend

1 - compilar o `main.py` para exe incluindo o `config.json`
  - cria scheduler.log, verifica mudanças no `config.json` a cada 5 segundos (nenhum reload é necessário)

<details>
<summary>Como gerar o executável usando a lib</summary>

  - `pip install pyinstaller`

Use o comando abaixo para empacotar o script e incluir o config.json:

- No Windows:
  - `pyinstaller --onefile --add-data "config.json;." main.py`
  - `pyinstaller --onefile --add-data  "./db/config.json;." main.py`

- No Linux/macOS:
  - `pyinstaller --onefile --add-data "config.json:." main.py`

</details>

  
2 - usar o `nssm` para instalar como serviço do Windows, ou usar o .bat

3 - JSON_MANAGER - Javascript recupera os dados do `config.json`
  -  edit, create, delete
  - autosave changes

4 - bat instala o app como serviço no Windows, o executavél definido é `main.exe`

### Melhorias futuras

## config.json contendo:

```js
 "description": "netlify", descrição
  "url": "https://geraldox.netlify.app/src/db/status.json",
  "status": true,
  "hora": "22:30"
```


## Front-end 

- JSON_MANAGER

- autosave changes - melhoria no feedback.
- adicionar bootstrap 5
