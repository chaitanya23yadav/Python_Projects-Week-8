from random import random
otp = str(random())[-6:]
print('Your OTP :', otp)
user = input('Enter OTP : ')
print('Success' if user == otp else 'Incorrect')
