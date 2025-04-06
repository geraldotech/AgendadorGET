import schedule
import time
import requests

# Função para fazer a requisição GET
def fazer_get(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print(f"Requisição para {url} realizada com sucesso!")
        else:
            print(f"Falha na requisição para {url}. Código de status: {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição para {url}: {e}")

# Função para agendar a requisição
def agendar_requisicao(url, hora):
    schedule.every().day.at(hora).do(fazer_get, url=url)
    print(f"Requisição para {url} agendada para {hora}.")

# Exemplo de URLs e horários de requisição
urls_agendadas = [
    {"url": "http://127.0.0.1:8080/PHP/General/Filesystem/CREATE/cretate_file_put_contents.php", "hora": "12:50"},
    {"url": "http://127.0.0.1:8080/PHP/General/Filesystem/WRITE/create_file_WRITE.php", "hora": "12:51"},
]

# Agendar todas as URLs
for url_info in urls_agendadas:
    agendar_requisicao(url_info['url'], url_info['hora'])

# Loop para rodar o agendador
while True:
    schedule.run_pending()
    time.sleep(1)
