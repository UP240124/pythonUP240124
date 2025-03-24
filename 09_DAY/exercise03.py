person={
    'first_name': 'Benjamin',
    'last_name': 'Gonzalez',
    'age': 18,
    'country': 'Mexico',
    'is_marred': False,
    'skills': ['soccer', 'sleep', 'math',"Videpgames"],
    'address': {
        'street': 'Flor de nochebuena 84',
        'zipcode': '20296'
    }
    }
#1
if 'skills' in person:
    skills = person['skills']
    middle_skill_index = len(skills) // 2
    print("Middle skill:", skills[middle_skill_index])
#2
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.")
    else:
        print("The person does not have Python skill.")
#3
if 'skills' in person:
    skills = set(person['skills'])
    
    if {'JavaScript', 'React'} == skills:
        print("He is a front end developer.")
    elif {'Node', 'Python', 'MongoDB'} == skills:
        print("He is a backend developer.")
    elif {'React', 'Node', 'MongoDB'} == skills:
        print("He is a fullstack developer.")
    else:
        print("Unknown title")
#4
if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} is married and lives in Finland.")