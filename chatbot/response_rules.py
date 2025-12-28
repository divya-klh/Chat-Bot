from chatbot.company_data import COMPANY_INFO

CHAT_RULES = [
    {
        "triggers": ["hi", "hello", "hey"],
        "reply": COMPANY_INFO["welcome_message"]
    },
    {
        "triggers": ["services", "what do you do"],
        "reply": COMPANY_INFO["info"]["services"]
    },
    {
        "triggers": ["contact", "email", "phone"],
        "reply": COMPANY_INFO["info"]["contact"]
    },
    {
        "triggers": ["location", "address"],
        "reply": COMPANY_INFO["info"]["location"]
    },
    {
        "triggers": ["hours", "timing", "working hours"],
        "reply": COMPANY_INFO["info"]["hours"]
    }
]
