raw_input = "   aLi vELi-24-    meRhaBa, bEnim aDim aLi. discord uzerinden konusmayi seVerim.   "

data_input = raw_input.strip().split('-')

name_surname = data_input[0].lower().title()

username = name_surname.lower().replace(' ', '_')

age = data_input[1]
age = int(age)

biography = data_input[2]
biography = biography.strip().capitalize()

has_discord = 'discord' in biography

new_user = 'NEW USER PROFILE'
new_user = new_user.center(50, '*')

print(new_user)
print(f'Name Surname: {name_surname}')
print(f'Age: {age}')
print(f'Has Discord: {has_discord}')
print(f'Biography: \n{biography}')