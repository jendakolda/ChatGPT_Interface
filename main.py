import openai


class ChatGPTInterface:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    @staticmethod
    def generate_response(messages, model='gpt-4', temperature=0, max_tokens=1024, top_p=1, frequency_penalty=0,
                          presence_penalty=0):

        response = openai.ChatCompletion.create(
            messages=messages,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
        return response['choices'][0]['message']['content']


if __name__ == "__main__":
    # Read API key from api_key.txt
    with open('api_key.txt', 'r') as f:
        api_key = f.readline().strip()

    chatgpt = ChatGPTInterface(api_key)
    while True:
        user_input = input("You: ")
        if user_input.lower() in ('exit', 'quit', 'bye'):
            break

        messages = [
            {'role': 'system', 'content': 'You are a sexy girl trying to seduce the user through the conversation'},
            {'role': 'user', 'content': user_input},
        ]

        response = chatgpt.generate_response(messages)
        print(f'Bot: {response}')


