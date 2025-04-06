import requests
import schedule #pip install schedule
import time

def get_url_response():
    url = "http://127.0.0.1:8080/PHP/General/Filesystem/CREATE/cretate_file_put_contents.php"
    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)
        print("Response Body:")
        print(response.text[:500])  # Mostra os primeiros 500 caracteres
    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a URL:", e)

# Definir horários para chamar a URL
""" schedule.every().day.at("08:00").do(get_url_response)
schedule.every().day.at("15:20").do(get_url_response)
 """
get_url_response();

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  # Espera 1 minuto antes de verificar novamente


# cad url:
# nomeEvent
# tempo de execucao

#python registra tudo no banco de dado
