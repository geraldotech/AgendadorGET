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


## features

<details>
<summary>Features</summary>


1. Controle de Tarefas Individual
✅ Cada tarefa tem configurações independentes no JSON:


```js
{
  "description": "Nome amigável",
  "url": "http://endpoint",
  "status": true/false,
  "hora": "HH:MM"
}
```

✅ Status individual (true/false) para ativar/desativar tarefas específicas

2. Monitoramento de Tempo
⏱️ Tempo de Execução: Medição e log do tempo gasto em cada requisição
Ex.: ✅ netlify | Status: 200 | Tempo: 0.45s

⏳ Verificação Periódica: Checa mudanças no config.json a cada 5 segundos (ajustável)

3. Sistema de Logs
📝 Dois Níveis de Log:

Console: Mensagens visuais coloridas (✅/⚠️/❌)

Arquivo scheduler.log: Registro detalhado para auditoria

✨ Logs Descritivos:


logging.info(f"✅ {description} | Status: {status_code} | Tempo: {tempo}s")

4. Recarregamento Automático
🔄 Atualiza configurações sem reiniciar o script:

Detecta mudanças no config.json

Recarrega tarefas e ajusta agendamentos dinamicamente

5. Controle de Execução
🛑 Cancelamento Inteligente:

Ignora tarefas com "status": false

Verificação em tempo real (mesmo se o status mudar após agendamento)

🚦 Tratamento de Erros:

Timeout de 10 segundos nas requisições

Captura de exceções com mensagens claras

6. Visualização do Status

📅 Tarefas Agendadas:
HORA   | DESCRIÇÃO       | STATUS
----------------------------------------
15:30 | netlify         | 🟢 ATIVA 
15:33 | restful         | 🔴 INATIVA


7. Gerenciamento de Dependências

</details>