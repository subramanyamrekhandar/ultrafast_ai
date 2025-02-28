from ultrafastai.client import UltraFastAI

api = UltraFastAI(api_key="your-api-key")
inputs = ["Translate 'hello' to French", "What is 2+2?"]
response = api.batch_inference(model="groq-llama3", inputs=inputs)
print(response)
