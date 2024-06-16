import os
import json
import subprocess

def send_request(url):
    """
    Wysyła żądanie HTTP GET do podanego URL za pomocą curl i zwraca kod statusu HTTP oraz ciało odpowiedzi JSON.
    """
    try:
        # Wykonuje curl i zwraca odpowiedzi.
        response = subprocess.check_output(['curl', '-s', '-w', '%{http_code}', url])
        http_code = response[-3:].decode('utf-8')  # Ostatnie 3 znaki to kod statusu
        json_body = response[:-3].decode('utf-8')  # Reszta to ciało JSON
        return http_code, json_body
    except subprocess.CalledProcessError as e:
        print(f"Błąd podczas wysyłania żądania do {url}: {e}")
        return None, None

def check_response(http_code, json_body, required_keys):
    """
    Sprawdza, czy odpowiedź HTTP ma status 200 i czy ciało odpowiedzi zawiera wymagane klucze.
    """
    if http_code != '200':
        return False, f"Nieoczekiwany kod statusu HTTP: {http_code}"

    try:
        data = json.loads(json_body)  # Parsowanie ciała JSON
    except json.JSONDecodeError:
        return False, "Nie udało się sparsować JSON"

    # Sprawdzanie obecności wymaganych kluczy
    for key in required_keys:
        if key not in data:
            return False, f"Brak klucza w odpowiedzi JSON: {key}"

    return True, "Odpowiedź jest poprawna"

def run_tests():
    """
    Uruchamia serię testów na wybranych endpointach API.
    """
    api_base = "https://jsonplaceholder.typicode.com"
    tests = [
        {"endpoint": "/posts/1", "keys": ["userId", "id", "title", "body"]},
        {"endpoint": "/users/1", "keys": ["id", "name", "username", "email"]},
        {"endpoint": "/todos/1", "keys": ["userId", "id", "title", "completed"]},
    ]

    # Iteracja przez testy
    for i, test in enumerate(tests, start=1):
        url = api_base + test["endpoint"]
        http_code, json_body = send_request(url)  # Wysyłanie żądania
        if http_code is None:
            print(f"Test {i}: NIEUDANY (błąd żądania)")
            continue
        
        passed, message = check_response(http_code, json_body, test["keys"])  # Sprawdzanie odpowiedzi
        result = "UDANY" if passed else "NIEUDANY"
        print(f"Test {i}: {result} ({message})")

if __name__ == "__main__":
    run_tests()
