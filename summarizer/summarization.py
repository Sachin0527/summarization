import google.generativeai as genai
from config.config import API_KEY, MODEL_NAME, GENERATION_CONFIG

# Configure the API key
genai.configure(api_key=API_KEY)

# Create the model instance
model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    generation_config=GENERATION_CONFIG,
)

def summarize_large_text(text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Summarize this: {text}")
    return response.text
