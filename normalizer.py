import re

def normalizeNameOrJobTitle(text: str) -> str:
    articles_prepositions = ['De', 'Da', 'Das', 'Do', 'Dos', 'E', 'Em',]
    text = text.lower().title()
    for word in articles_prepositions:
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, word.lower(), text, flags=re.IGNORECASE)

    return text

def formatPhoneNumber(phone: str) -> str:
    cleaned_phone = re.sub(r'\D', '', phone)
    if len(cleaned_phone) == 10:
        return re.sub(r'(\d{2})(\d{4})(\d{4})', r'(\1) \2-\3', cleaned_phone)
    elif len(cleaned_phone) == 8:
        return re.sub(r'(\d{4})(\d{4})', r'\1-\2', cleaned_phone)
    else:
        return phone
    
def normalizeData(userData: dict) -> dict:
    normalizedData = userData.copy()

    for key, value in normalizedData.items():
        if isinstance(value, str):
            match key:
                case 'fullName' | 'jobTitle':
                    normalizedData[key] = normalizeNameOrJobTitle(value)
                case 'department':
                    normalizedData[key] = value.upper()
                case 'phoneNumber':
                    normalizedData[key] = formatPhoneNumber(value)
                case _:
                    normalizedData[key] = value.lower()

    return normalizedData
        