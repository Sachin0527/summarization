import google.generativeai as genai
from config.config import API_KEY, GENERATION_CONFIG

# Configure the API key
genai.configure(api_key=API_KEY)

# Create the GenerativeModel instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=GENERATION_CONFIG
)

# Function to summarize text
def summarize_text(input_text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Summarize this: {input_text}")
    return response.text

# Function to handle large texts by splitting into chunks
def chunk_text(text, max_tokens=1000):
    paragraphs = text.split("\n\n")  # Split based on paragraph breaks
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) < max_tokens:
            current_chunk += paragraph + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# Function to summarize large text by processing in chunks
def summarize_large_text(input_text):
    chunks = chunk_text(input_text)
    full_summary = []

    for idx, chunk in enumerate(chunks):
        print(f"Summarizing chunk {idx + 1} of {len(chunks)}...")
        summary = summarize_text(chunk)
        full_summary.append(summary)

    return "\n\n".join(full_summary)
