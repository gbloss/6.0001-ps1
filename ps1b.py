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
current_savings = 0
r = 0.04

#Gather User Input

annual_salary = sanitized_input ("Enter your annual salary: ", float, 0)
portion_saved = sanitized_input ("Enter the percent of your salary to save: ", 
                                float, 0, 1)
total_cost = sanitized_input ("Enter the cost of your dream home: ", float, 0)
semi_annual_raise = sanitized_input ("Enter the semi­annual raise, as a decimal: ", 
                                float, 0, 1)

# Calculate Montly Values

monthly_salary = annual_salary/12
mr = r/12

# Set required test values

down_payment = portion_down_payment * total_cost
monthly_savings = monthly_salary * portion_saved
number_of_months = 0

while current_savings < down_payment:
    if number_of_months != 0 and number_of_months%6 == 0:
        monthly_savings = monthly_savings*(1+semi_annual_raise)
    current_savings = monthly_savings + current_savings*(1+mr)
    number_of_months = number_of_months + 1
    
#print ("Down payment is :", down_payment)
#print ("Current savings is ", current_savings)
print ("Number of months is ", number_of_months)
    