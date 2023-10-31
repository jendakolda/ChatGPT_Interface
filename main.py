import openai


class ChatGPTInterface:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    @staticmethod
    def generate_response(messages):
        response = openai.ChatCompletion.create(
            model="gpt-4",  # "gpt-4.0-turbo",
            messages=messages)
        return response['choices'][0]['message']['content']


if __name__ == "__main__":
    # Read API key from api_key.txt
    with open('api_key.txt', 'r') as f:
        api_key = f.readline().strip()

    chatgpt = ChatGPTInterface(api_key)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        messages = [
            {'role': 'system', 'content': 'You are a chatbot.'},
            {'role': 'user', 'content': user_input},
        ]

        response = chatgpt.generate_response(messages)
        print(f'Bot: {response}')


