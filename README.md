# Skrypt do Automatyzacji Testów API

To repozytorium zawiera prosty skrypt do automatyzacji testów endpointów API przy użyciu curl.

Skrypt wysyła żądania HTTP GET do określonych endpointów publicznego API (JSONPlaceholder) za pomocą curl, sprawdza kody statusu HTTP, parsuje odpowiedzi JSON oraz weryfikuje obecność wymaganych kluczy w odpowiedzi.

1. Upewnij się, że masz zainstalowanego Pythona na swoim komputerze.
2. Zainstaluj curl na swoim komputerze.
3. Zapisz skrypt do pliku, na przykład `api_test.py`.
4. Uruchom skrypt z linii komend:

   ```sh
   python api_test.py