# Set the value of a new variable to 3
my_var = 3
# Print the value assigned to my_var
print(my_var)
# Change the value of the variable to 100
my_var = 100
# Print the new value assigned to my_var
print(my_var)
# Increase the value by 3
my_var = my_var + 3
# Print the value assigned to my_var
print(my_var)


# Create variables
num_years = 4
days_per_year = 365
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)
print(hours_per_day)


num_hours=50
hourly_wage=200
tax_bracket=2
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax
higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print(higher_pay_aftertax)


# Define the function with no arguments and with no return
def print_hello():
    print("Hello, you!")
    print("Good morning!")
# Call the function
print_hello()

my_number = "1.12321"
print(my_number)
print(type(my_number))

var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only
    # if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message
print(evaluate_temp(37))
print(evaluate_temp(39))


def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message
print(evaluate_temp_with_elif(36))
print(evaluate_temp_with_elif(34))

def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(type(flowers))
print(flowers)

flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
print(type(flowers_list))
print(flowers_list)
# The list has ten entries
print(len(flowers_list))

print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])