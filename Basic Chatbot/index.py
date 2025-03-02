questions = [
    "What is your name?",
    "What is your age?",
    "What is your favorite color?",
    "What is your profession?"
]

responses = {}

print("ChatBot: Hello! Let's chat. Type 'exit' anytime to stop.")

for question in questions:
    user_input = input(f"ChatBot: {question} ")

    if user_input.lower() == "exit":
        print("ChatBot: Goodbye! Have a great day!")
        break

    responses[question] = user_input

print("\nChatBot: Here’s what I learned about you:")
for question, answer in responses.items():
    print(f"- {question} {answer}")

print("ChatBot: It was nice talking to you!")
