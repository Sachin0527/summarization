from src import Summarizer

config_file = 'config.yaml'


def main():
    try:
        input_file = input("Enter the path to the file you want to summarize: ")
        summarizer = Summarizer(config_file)
        result = summarizer.summarize(input_file)
        print(result)
        return result
    except Exception as e:
        msg = f"An error occurred during the summarization process. Check logs for details. \n {str(e)}"
        print(msg)
        return msg


if __name__ == '__main__':
    main()
