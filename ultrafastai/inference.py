import requests
from ultrafastai.config import BASE_URL

class InferenceClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_text(self, model: str, prompt: str, max_tokens: int = 100):
        """Generate text using an AI model."""
        url = f"{BASE_URL}/inference/text"
        payload = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
        }
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    
    def batch_inference(self, model: str, prompts: list):
        """Perform batch inference."""
        url = f"{BASE_URL}/inference/batch"
        payload = {"model": model, "prompts": prompts}
        headers = {"Authorization": f"Bearer {self.api_key}"}

        response = requests.post(url, json=payload, headers=headers)
        return response.json()
