import unittest
from ultrafastai.client import UltraFastAI

class TestUltraFastAI(unittest.TestCase):
    def setUp(self):
        self.api = UltraFastAI(api_key="test-key")

    def test_generate_text(self):
        response = self.api.generate_text(model="groq-llama3", prompt="Hello")
        self.assertIn("error", response)  # Expect error because of invalid API key

if __name__ == '__main__':
    unittest.main()
