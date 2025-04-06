import schedule
import time
import requests
import os
import json
import logging
from pathlib import Path

""" 
VERSAO NAO VERIFICA STATUS
 """

# Configurar o sistema de logs
logging.basicConfig(
    filename='scheduler.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Criar um logger específico para sucessos (log_success.log)
success_logger = logging.getLogger('success_logger')
success_logger.setLevel(logging.INFO)
success_handler = logging.FileHandler('log_success.log')
success_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
success_logger.addHandler(success_handler)


# Variável global para armazenar as configurações
config = None
# Variável para armazenar o último timestamp de modificação
ultima_modificacao = None

# Caminho fixo relativo (sempre /db/config.json)
config_path = Path('db') / 'config.json'


# Função para carregar o arquivo JSON
def carregar_config():
    global config, ultima_modificacao

    try:
        # with open(config_path, 'r') as file:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
            logging.info("Arquivo config.json carregado com sucesso.")
            print("Configurações carregadas com sucesso!")
            print(config)
            # Atualiza o timestamp da última modificação
            ultima_modificacao = os.path.getmtime(config_path)
    except FileNotFoundError:
        logging.error("Arquivo config.json não encontrado.")
        print(f"ERRO: Crie o arquivo {config_path} ou ajuste o caminho")
    except json.JSONDecodeError:
        logging.error("Erro ao decodificar o arquivo config.json.")
    except Exception as e:
        logging.error(f"Erro inesperado ao carregar config.json: {e}")

# Função para verificar se o arquivo foi modificado
def verificar_modificacao():
    global ultima_modificacao
    try:
        # Obtém o timestamp atual do arquivo
        modificacao_atual = os.path.getmtime(config_path)
        if modificacao_atual != ultima_modificacao:
            logging.info("Arquivo config.json modificado. Recarregando...")
            carregar_config()
            recarregar_agendamentos()  # Recarrega os agendamentos após modificar o config.json
    except FileNotFoundError:
        logging.error("Arquivo config.json não encontrado durante a verificação.")
    except Exception as e:
        logging.error(f"Erro ao verificar modificação do config.json: {e}")

# Função para fazer a requisição GET
def fazer_get(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f"Requisição para {url} realizada com sucesso!")
            logging.info(f"Requisição para {url} realizada com sucesso!")
            success_logger.info(f"Response from {url} - {resposta.text}")
        else:
            print(f"Falha na requisição para {url}. Código de status: {resposta.status_code}")
            logging.warning(f"Falha na requisição para {url}. Código de status: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição para {url}: {e}")
        logging.error(f"Erro ao fazer a requisição para {url}: {e}")

# Função para agendar as requisições
def agendar_requisicoes():
    if config and 'tasks' in config:
        for task in config['tasks']:
            url = task.get('url')
            hora = task.get('hora')
            if url and hora:
                schedule.every().day.at(hora).do(fazer_get, url=url)
                logging.info(f"Requisição para {url} agendada para {hora}.")
                print(f"Requisição para {url} agendada para {hora}.")

# Função para recarregar os agendamentos
def recarregar_agendamentos():
    logging.info("Recarregando agendamentos...")
    schedule.clear()  # Limpa todos os agendamentos existentes
    agendar_requisicoes()  # Agenda as requisições com as novas configurações

# Inicializar o carregamento do config.json e agendar as requisições
carregar_config()
agendar_requisicoes()

# Loop principal para verificar modificações e rodar o agendador
if __name__ == "__main__":
    intervalo_verificacao = 5  # Verificar a cada 5 segundos
    try:
        while True:
            verificar_modificacao()  # Verifica se o config.json foi modificado
            schedule.run_pending()  # Executa as tarefas agendadas
            time.sleep(1)  # Espera 1 segundo para evitar uso excessivo da CPU
    except KeyboardInterrupt:
        logging.info("Script interrompido pelo usuário.")