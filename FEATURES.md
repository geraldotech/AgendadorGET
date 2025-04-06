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