age = int(input('Enter your age: ')) # if 18+
have_id = bool(input("ignore if you don't have id")) # and True

if age < 18:
    print('you are not eligible to vote')
    print('wait for another', 18-age, 'years')

elif age >= 18 and have_id:
    print('You are eligible to vote')

elif age >= 18 and not have_id:
    print("You need and ID to vote")

else:
    print('Invalid data')
