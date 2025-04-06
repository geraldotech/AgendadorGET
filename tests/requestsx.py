
import requests

def get_url_response(url):
    try:
        response = requests.get(url)
        print("Status Code:", response.status_code)
        print("Response Body:")
        print(response.text[:500])  # Mostra os primeiros 500 caracteres
    except requests.exceptions.RequestException as e:
        print("Erro ao acessar a URL:", e)

if __name__ == "__main__":
    url = input("Digite a URL: ")
    get_url_response(url)
