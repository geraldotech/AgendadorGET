
# versao nao faz watch do json em caso de alteracoes
import schedule
import time
import requests
import json
import logging

""" 
VERSÃO NAO VERIFICA MUDANCAS NO config.json
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

# Função para fazer a requisição GET
def fazer_get(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            logging.info(f"Requisição para {url} realizada com sucesso!")
            success_logger.info(f"Response from {resposta.text}")

        else:
            logging.warning(f"Falha na requisição para {url}. Código de status: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao fazer a requisição para {url}: {e}")

# Função para agendar a requisição
def agendar_requisicao(url, hora):
    schedule.every().day.at(hora).do(fazer_get, url=url)
    logging.info(f"Requisição para {url} agendada para {hora}.")

# Carregar configurações do arquivo JSON
try:
    with open('config.json', 'r') as file:
        config = json.load(file)
    urls_agendadas = config['tasks']
    print("Configurações carregadas com sucesso!")
    logging.info("Configurações carregadas com sucesso.")
except Exception as e:
    logging.error(f"Erro ao carregar o arquivo config.json: {e}")
    exit(1)

# Agendar todas as URLs
for url_info in urls_agendadas:
    agendar_requisicao(url_info['url'], url_info['hora'])

# Loop para rodar o agendador
logging.info("Agendador iniciado. Pressione Ctrl+C para parar.")
while True:
    schedule.run_pending()
    time.sleep(1)