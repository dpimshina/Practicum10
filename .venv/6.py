def check_message(text):
    if len(text) <= 160:
        return text
    else:
        return text[:160]