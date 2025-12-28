# Simple Company Chatbot

This is a simple rule based chatbot built with Python. It's designed to be a lightweight and easy to understand solution for answering common questions about a company. Since it doesn't rely on any AI models or external services, it's fast, private and simple to maintain.

## Features

- **No AI, No APIs:** Works completely offline without any external dependencies.
- **RuleBased:** Responds based on a simple set of predefined rules.
- **Easy to Customize:** Company information and chat rules can be easily modified in dedicated Python files.
- **Lightweight:** Requires no external libraries to run.

## How to Run

1.  **Prerequisites:** Make sure you have Python installed on your system.
2.  **Start the Chatbot:** Open your terminal or command prompt, navigate to the project directory, and run the following command:

    ```bash
    python main.py
    ```

## Customization

You can change the chatbot's knowledge and responses by editing the following files:

-   **`chatbot/company_data.py`**: Modify this file to change the company's name, welcome message, and other specific details.
-   **`chatbot/response_rules.py`**: Add, edit, or remove rules in this file to change how the chatbot responds to different keywords and phrases.

## File Structure

The project is organized as follows:

```
.
├── main.py                 # The main script to run the chatbot
├── requirements.txt        # Shows that no external libraries are needed
├── chatbot/
│   ├── chat_logic.py       # Core logic for finding replies
│   ├── company_data.py     # Stores company specific information
│   └── response_rules.py   # Defines the chatbot's conversational rules
└── README.md               
```

## Exit Commands

To end the chat session, you can use any of the following commands:

-   `exit`
-   `quit`
-   `bye`
