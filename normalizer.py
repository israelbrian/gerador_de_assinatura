import re

def capitalizeData(text: str) -> str:
    articles_prepositions = ['De', 'Da', 'Das', 'Do', 'Dos', 'E', 'Em',]
    text = text.lower().title()
    for word in articles_prepositions:
        pattern = r'\b' + re.escape(word) + r'\b'
        text = re.sub(pattern, word.lower(), text, flags=re.IGNORECASE)

    return text

def formatPhoneNumber(phone: str) -> str:
    cleaned_phone = re.sub(r'\D', '', phone)
    length = len(cleaned_phone)

    if length == 11: # Celular: (XX) XXXXX-XXXX
        return re.sub(r'(\d{2})(\d{5})(\d{4})', r'(\1) \2-\3', cleaned_phone)
    elif length == 10: # Fixo: (XX) XXXX-XXXX
        return re.sub(r'(\d{2})(\d{4})(\d{4})', r'(\1) \2-\3', cleaned_phone)
    elif length == 8: # Fixo sem DDD: XXXX-XXXX
        return re.sub(r'(\d{4})(\d{4})', r'\1-\2', cleaned_phone)
    else:
        return phone

def normalizeAdress(text: str) -> str:
    normalized_text = capitalizeData(text)
    acronyms = ['Bh', 'Mg', 'Srs', 'Grs'] 

    for acronym in acronyms:
        pattern = r'\b' + re.escape(acronym) + r'\b'
        normalized_text = re.sub(pattern, acronym.upper(), normalized_text)

    return normalized_text

def normalizeData(userData: dict) -> dict:
    normalizedData = userData.copy()

    for key, value in normalizedData.items():
        if isinstance(value, str):
            match key:
                case 'fullName' | 'jobTitle':
                    normalizedData[key] = capitalizeData(value)
                case 'department':
                    normalizedData[key] = value.upper()
                case 'phoneNumber' | 'telephoneNumber':
                    normalizedData[key] = formatPhoneNumber(value)
                case 'adress':
                    normalizedData[key] = normalizeAdress(value)
                case _:
                    normalizedData[key] = value.lower()

    return normalizedData
        