# from ultrafastai.client import UltraFastAI

# api = UltraFastAI(api_key="your-api-key")
# response = api.generate_text(model="groq-llama3", prompt="Tell me a joke.")
# print(response)

from ultrafastai.api_key import APIKeyManager
from ultrafastai.inference import InferenceClient

# Step 1: Generate an API Key (only needed once)
user_email = "user@example.com"
api_key_data = APIKeyManager.generate_api_key(user_email)
api_key = api_key_data["api_key"]
print(f"Generated API Key: {api_key}")

# Step 2: Initialize Inference Client
client = InferenceClient(api_key)

# Step 3: Perform Text Generation
response = client.generate_text(model="llama3", prompt="Write a startup idea about AI")
print(response)
