from chatbot.company_data import COMPANY_INFO
from chatbot.response_rules import CHAT_RULES
from chatbot.chat_logic import find_reply

def start_chat():
    print(COMPANY_INFO["welcome_message"])

    while True:
        user_text = input("You: ").strip()

        if user_text.lower() in ["exit", "quit", "bye"]:
            print("Bot: Thanks for chatting. Have a great day!")
            break

        bot_reply = find_reply(user_text, CHAT_RULES, COMPANY_INFO)
        print("Bot:", bot_reply)

if __name__ == "__main__":
    start_chat()
