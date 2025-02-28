import logging

def track_tokens(response, token_usage):
    """Update token usage from response."""
    if isinstance(response, dict) and "token_usage" in response:
        token_usage += response["token_usage"]
        logging.info(f"Total tokens used: {token_usage}")
    return token_usage

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_api_call(endpoint: str, status_code: int):
    """Log API request details."""
    logging.info(f"API Call - Endpoint: {endpoint}, Status: {status_code}")
