import openai
import os

os.environ["OPENAI_API_KEY"] = "your_api_key"

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(question):
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3 engine
        prompt=question,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

# Main loop for chatting
def chat():
    print("Welcome to the GPT-3 Chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("Ask a question: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = ask_gpt(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
