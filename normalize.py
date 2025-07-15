# Manipulação dos dados recebidos (lowercase, upper, capitalize)
def normallize_data(userData):
    for key, value in userData.items():
        if isinstance(value, str):
            if key == 'fullName':
                userData[key] = value.title().replace('De','de').replace('Da','da').replace('Das','das').replace('Do','do').replace('Dos','dos').replace('Em','em')  
            elif key == 'jobTitle': 
                userData[key] = value.title().replace('De','de').replace('Da','da').replace('Das','das').replace('Do','do').replace('Dos','dos').replace('Em','em')              
            elif key == 'department':
                userData[key] = value.upper()
            elif key == 'phoneNumber':
                if len(value) == 10:
                    userData[key] = value[0:2] + ' ' + value[2:6] + '-' + value[6:10]
            else:
                userData[key] = value.lower()
        