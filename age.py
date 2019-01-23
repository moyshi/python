__author__ = 'moyshi'

age = input('נא הכנס את הגיל שלך')
age = int(age)
if age == 18:
    print('מזל טוב')
elif age < 18:
    print('אתה עדיין קטן')
else:
    print('אתה כבר גדול')
