import os
import pytest
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

BASE_URL = "https://api.green-api.com"
ID_INSTANCE = os.getenv("GREEN_API_ID")  # Используйте имя переменной, а не значение
API_TOKEN = os.getenv("GREEN_API_TOKEN")  # Используйте имя переменной, а не значение

def test_send_message():
    url = f"{BASE_URL}/waInstance{ID_INSTANCE}/SendMessage/{API_TOKEN}"
    payload = {
        "chatId": "79991234567@c.us",  # Замените на реальный chatId
        "message": "Hello from pytest!"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert "idMessage" in response.json()

def test_get_chat_history():
    url = f"{BASE_URL}/waInstance{ID_INSTANCE}/GetChatHistory/{API_TOKEN}"
    payload = {
        "chatId": "79991234567@c.us",  # Замените на реальный chatId
        "count": 10
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert isinstance(response.json(), list)