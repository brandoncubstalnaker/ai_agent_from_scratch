from google import genai
from config import get_api_key

class LLMClient:

    def __init__(self,model_name="gemini-3.5-flash"):
        api_key = get_api_key()
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    def generate(self, prompt):
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )
        return response.text


if __name__ == "__main__":
    client = LLMClient()
    print(client.generate("Say 'Agent Available!!!'")) 
