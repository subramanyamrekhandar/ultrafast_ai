import requests

class InferenceClient:
    def __init__(self, api_key: str, base_url: str = "http://127.0.0.1:8000/api"):
        """
        Initialize the inference client.
        
        :param api_key: API key for authentication.
        :param base_url: Base URL of the backend API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

    def generate_text(self, model: str, prompt: str, max_tokens: int = 256):
        """
        Generate text using a specified AI model.
        
        :param model: Model name (e.g., "llama3", "mistral", "gemini").
        :param prompt: Input prompt for text generation.
        :param max_tokens: Maximum number of tokens in the response.
        :return: Generated text or error message.
        """
        url = f"{self.base_url}/generate-text"
        payload = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise error if status code is not 200
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def batch_inference(self, model: str, prompts: list, max_tokens: int = 256):
        """
        Perform batch inference for multiple prompts.
        
        :param model: Model name.
        :param prompts: List of prompts.
        :param max_tokens: Maximum tokens per response.
        :return: List of generated texts or errors.
        """
        url = f"{self.base_url}/batch-inference"
        payload = {
            "model": model,
            "prompts": prompts,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_models(self):
        """
        Fetch the list of available AI models.
        
        :return: List of models or error message.
        """
        url = f"{self.base_url}/models"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def check_api_usage(self):
        """
        Check the current API usage stats.
        
        :return: API usage details or error message.
        """
        url = f"{self.base_url}/usage"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}














# import requests
# import logging

# class UltraFastAI:
#     BASE_URL = "https://api.yourservice.com"

#     def __init__(self, api_key: str):
#         self.api_key = api_key
#         self.headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
#         self.token_usage = 0

#     def generate_text(self, model: str, prompt: str, max_tokens: int = 100):
#         """Generate text using AI model."""
#         url = f"{self.BASE_URL}/v1/generate"
#         payload = {"model": model, "prompt": prompt, "max_tokens": max_tokens}
#         response = self._post_request(url, payload)
#         self._track_tokens(response)
#         return response

#     def batch_inference(self, model: str, inputs: list):
#         """Perform batch inference."""
#         url = f"{self.BASE_URL}/v1/batch"
#         payload = {"model": model, "inputs": inputs}
#         response = self._post_request(url, payload)
#         self._track_tokens(response)
#         return response

#     def _post_request(self, url, payload):
#         """Handle API request with rate-limit handling."""
#         try:
#             response = requests.post(url, json=payload, headers=self.headers)
#             if response.status_code == 429:
#                 logging.warning("Rate limit exceeded. Try again later.")
#                 return {"error": "Rate limit exceeded. Try again later."}
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             logging.error(f"Request failed: {e}")
#             return {"error": str(e)}

#     def _track_tokens(self, response):
#         """Track token usage from API response."""
#         if isinstance(response, dict) and "token_usage" in response:
#             self.token_usage += response["token_usage"]
#             logging.info(f"Total tokens used: {self.token_usage}")
