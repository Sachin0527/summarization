from .summarization import summarize_large_text

def read_from_txt(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_to_txt(output_file_path, summarized_text):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(summarized_text)

def summarize_txt(input_file_path, output_file_path):
    input_text = read_from_txt(input_file_path)
    summary = summarize_large_text(input_text)
    write_to_txt(output_file_path, summary)
    print(f"Summary has been written to {output_file_path}")
