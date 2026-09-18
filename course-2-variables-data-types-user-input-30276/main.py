print('=' * 40)
print('     WELCOME TO THE PROFILE BUILDER')
print('=' * 40)
print('Let\'s get to know you better! Please enter your information.')
name = input('What is your full name? ')
age = input('How old are you? ')
height = input('What is your heights (in meters)? ')
weight = input('What is your weight (in kilograms)? ')
is_student = input('Are you a student(yes/no): ')
color = input('What is your favorite color? ')
city = input('What city do you live in? ')
print('=' * 40)
print('     YOUR PROFILE')
print('=' * 40)
print('Personal Information:')

#NAME
name = name.strip().title()
if not name:
    print('Nothing Entered')
print(f'- Name: {name} ({type(name).__name__}, {len(name)} characters)')

#AGE
try:
    age = int(age)
    months = age * 12
    days = age * 365
    print(f'- Age ({type(name).__name__})')
    print(f' * {months} months')
    print(f' * {days} days (approximately)')
except ValueError:
    age = 0
    print('No age entered, Enter digits')


#CITY
city = city.strip().title()
if not city:
    print('Nothing Entered')
print(f'- City: {city} ({type(city).__name__})')

#COLOUR
color = color.strip().title()
if not color:
    print('Nothing Entered')
print(f'- Favorite color: {color} ({type(color).__name__})')

#STUDENT
is_student = is_student.strip().lower()
try:
    if is_student in ['yes', 'y']:
        is_student = True
    elif is_student in ['no','n']:
        is_student = False
    print(f'- Student: {is_student} ({type(is_student).__name__})')
except ValueError:
    is_student = False
    print('Invalid, enter (yes/no)')

#ADULT
is_adult = False
if age >= 18:
    is_adult = True
print(f'- Adult: {is_adult} ({type(is_adult).__name__})')

print('Health Information:')

#HEIGHT
try:
    height = float(height)
    print(f'- Height: {height} m ({type(height).__name__})')
except ValueError:
    height = 0
    print('No height entered, Enter digits')

#WEIGHT
try:
    weight = float(weight)
    print(f'- Weight: {weight:.2f} kg ({type(weight).__name__})')
except ValueError:
    weight = 0
    print('No weight entered, Enter digits')

#BMI
try:
    bmi = weight / (height * height)
    if bmi:
        if bmi < 18.5:
            bmi_category = 'Under weight'
        elif bmi < 25:
            bmi_category = 'Normal weight'
        elif bmi < 30:
            bmi_category = 'Overweight'
        else:
            bmi_category = 'Obese'
    print(f'- BMI: {bmi:.2f} ({type(bmi).__name__})')
    print(f'- BMI Category: {bmi_category}')
except ZeroDivisionError:
    bmi = 0
    print('Weight / height not entered')

print('=' * 40)
print(f'Profile Complete! Thank you, {name}!')
print('=' * 40)

print('Data Types Summmary:')
print(f'- Name: {type(name).__name__}')
print(f'- Age: {type(age).__name__}')
print(f'- Height: {type(height).__name__}')
print(f'- Weight: {type(weight).__name__}')
print(f'- Student: {type(is_student).__name__}')
print(f'- Favorite color: {type(color).__name__}')
print(f'- City: {type(city).__name__}')
print(f'- BMI: {type(bmi).__name__}')
print('=' * 40)