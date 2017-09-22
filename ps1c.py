def sanitized_input(prompt, input_type=None, input_min=None, input_max=None):
    if input_min is not None and input_max is not None and input_max < input_min:
        raise ValueError("Minimum must be less than or equal to the maximum.")
    while True:
        user_input = input(prompt)
        if input_type is not None:
            try:
                user_input = input_type(user_input) 
            except ValueError:
                print("Input type must be {0}.".format(input_type.__name__))
                continue
        if input_max is not None and user_input >= input_max:
            print("Input must be less than {0}.".format(input_max))
        elif input_min is not None and user_input <= input_min:
            print("Input must be greater than {0}.".format(input_min))
        else:
            return user_input

# Set Constant Values

portion_down_payment = 0.25
total_savings = 0
semi_annual_raise = 0.07
total_cost = 1000000
r = 0.04
number_of_months = 36

#Gather User Input

annual_salary = sanitized_input ("Enter your annual salary: ", float, 0)
#savings_rate = sanitized_input ("Enter your savings rate: ", int, 0, 10000)


# Calculate Monthly Values

monthly_salary = annual_salary/12
mr = r/12

# Set required test values


total_savings = 0
low = 0
high = 10000
required_savings = portion_down_payment * total_cost
epsilon = 100
num_guesses = 0
monthly_savings = 0
old_guess = 0
 


while abs (total_savings - required_savings) > epsilon and monthly_savings < monthly_salary and old_guess != guess:
    old_guess = guess
    if num_guesses == 0:
        guess = int((low + high)/2)   
    elif total_savings < required_savings:
        low = guess
        guess = int((low + high)/2) 
    else:
        high = guess
        guess = int((low + high)/2)    
    monthly_savings = monthly_salary*guess/10000
    current_month = 0
    current_savings = 0
#    print (old_guess, guess)
    for i in range (number_of_months):
        if current_month != 0 and current_month%6 == 0:
            monthly_savings = monthly_savings*(1+semi_annual_raise)
        current_savings = monthly_savings + current_savings*(1+mr)
        current_month += 1
    total_savings = current_savings 
    num_guesses += 1
#    print("Guess is: ", guess)
#    print("Total savings is:", total_savings)
#    print("Required savings is:", required_savings)

if old_guess == guess:
    print("Can't get as close as",epsilon)
    print ("Here's what would get you close ", guess/10000)    
elif abs(total_savings - required_savings) > epsilon:
    print("Sorry pal.  You need to make more money")
else:
    print ("Required savings rate ", guess/10000)

print ("Steps in bisection search ", num_guesses)
    