import google.generativeai as genai
from config import API_KEY, GENERATION_CONFIG

# Configure the API key
genai.configure(api_key=API_KEY)

# Create the GenerativeModel instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=GENERATION_CONFIG
)

# Function to summarize text
def summarize_text(input_text):
    # Start a chat session and send the prompt
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"Summarize this: {input_text}")
    return response.text

# Function to handle large texts by splitting into chunks
def chunk_text(text, max_tokens=1000):
    # Split text into manageable chunks
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

# Function to summarize text from multiple paragraphs or large documents
def summarize_large_text(input_text):
    # Chunk the text if necessary
    chunks = chunk_text(input_text)
    full_summary = []

    # Summarize each chunk
    for idx, chunk in enumerate(chunks):
        print(f"Summarizing chunk {idx + 1} of {len(chunks)}...")
        summary = summarize_text(chunk)
        full_summary.append(summary)

    # Combine all summaries into a single text
    return "\n\n".join(full_summary)

# Function to read input from a text file and write the summary to an output file
def summarize_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        input_text = file.read().strip()

    # Summarize the large text
    summary = summarize_large_text(input_text)

    # Write the summary to the output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(summary)

# Specify the paths to the input and output files
input_file_path = 'input.txt'
output_file_path = 'summary.txt'

# Perform the summarization
summarize_from_file(input_file_path, output_file_path)

print(f"Summary has been written to {output_file_path}")
