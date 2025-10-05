import app_config
from breeze_connect import BreezeConnect

print("Attempting to initialize BreezeConnect...")
try:
    breeze = BreezeConnect(api_key=app_config.API_KEY)
    print("BreezeConnect initialized successfully.")
except Exception as e:
    print(f"An error occurred during initialization: {e}")