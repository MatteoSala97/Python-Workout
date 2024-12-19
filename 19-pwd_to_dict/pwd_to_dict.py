def pwd_to_dict(file_path):
    users = {}
    with open (file_path) as pwd: 
        for line in pwd:
            if not line.startswith(('#','\n')):
                user_info = line.split(':')
            users[user_info[0]] = int(user_info[2])
    return users

file_path = r'C:\Users\matteo.sala\Documents\Python Workout\19-pwd_to_dict\pwd.txt'

print(pwd_to_dict(file_path))