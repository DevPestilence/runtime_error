#This is a faulty program for age verification!
minimum_age = 18;
maximum_Age = 90;

#Here is the main code for running the program and gathering the input of the user.
age = int(input("Enter age before proceeding:"));
if age == minimum_age:
    print('Thank you for confirming your age. You are', age, 'years old.')
elif age == maximum_age:
    print('You are far too old. My apologies')
elif age == 17:
    print('Sorry. Try again, next year!')
else:
    print('You are too young to proceed.');
