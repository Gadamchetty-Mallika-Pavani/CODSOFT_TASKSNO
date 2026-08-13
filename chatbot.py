def chatbot():
    print("Nora: Hello! I'm Nora, your chatbot.")
    print("Nora: Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("Nora: Hi! Nice to meet you.")

        elif "how are you" in user_input:
            print("Nora: I'm doing great! Thanks for asking.")

        elif "your name" in user_input or "who are you" in user_input:
            print("Nora: I'm Nora, a simple rule-based chatbot.")

        elif "what can you do" in user_input:
            print("Nora: I can answer some basic questions and chat with you.")

        elif "how old are you" in user_input:
            print("Nora: I'm just a chatbot, so I don't really have an age!")

        elif "where are you from" in user_input:
            print("Nora: I live in your computer! Pretty convenient, right?")

        elif "who created you" in user_input:
            print("Nora: I was created as an AI internship project using Python.")

        elif "what is python" in user_input:
            print("Nora: Python is a popular programming language known for its simplicity.")

        elif "do you like music" in user_input:
            print("Nora: I can't listen to music, but I think humans have great taste!")

        elif "thank you" in user_input or "thanks" in user_input:
            print("Nora: You're welcome! 😊")

        elif "good morning" in user_input:
            print("Nora: Good morning! I hope you have a wonderful day.")

        elif "good night" in user_input:
            print("Nora: Good night! Sleep well.")

        elif "help" in user_input:
            print("Nora: You can ask me about my name, Python, my abilities, or just chat with me.")

        elif user_input in ["bye", "exit", "quit"]:
            print("Nora: Goodbye! Have a great day!")
            break

        else:
            print("Nora: Hmm... I don't understand that yet. Try asking me something else.")


chatbot()