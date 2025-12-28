import re

def normalize_message(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def find_reply(user_message, rules, company_info):
    if not user_message or not user_message.strip():
        return "Please type something."

    if len(user_message) > company_info["max_message_length"]:
        return "That message is a long. Please keep it short."

    clean_message = normalize_message(user_message)

    for rule in rules:
        for phrase in rule["triggers"]:
            if re.search(rf"\b{re.escape(phrase)}\b", clean_message):
                return rule["reply"]

    return company_info["default_reply"]
