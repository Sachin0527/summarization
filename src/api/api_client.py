import google.generativeai as genai


class APIClient:
    def __init__(self, config):
        genai.configure(api_key=config.get('api_key'))
        self.model = genai.GenerativeModel(
            model_name=config.get('model_name'),
            generation_config=config.get('generation_config')
        )

    def api_call(self, text):
        try:
            chat_session = self.model.start_chat()
            response = chat_session.send_message(f"Summarize this: {text}")
            return response.text
        except Exception as e:
            raise Exception(str(e))
