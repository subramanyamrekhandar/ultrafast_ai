import requests
from ultrafastai.config import BASE_URL

class APIKeyManager:
    @staticmethod
    def generate_api_key(user_email: str):
        """Request an API key for a given email."""
        url = f"{BASE_URL}/generate_api_key"
        response = requests.post(url, json={"email": user_email})
        return response.json()

    @staticmethod
    def validate_api_key(api_key: str):
        """Check if an API key is valid."""
        url = f"{BASE_URL}/validate_api_key/{api_key}"
        response = requests.get(url)
        return response.json()
    
    @staticmethod
    def revoke_api_key(api_key: str):
        """Revoke an API key (for admin use)."""
        url = f"{BASE_URL}/revoke_api_key/{api_key}"
        response = requests.post(url)
        return response.json()

