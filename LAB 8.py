# Lewis Muthomi
# 1250 01
# Lab 8
# 10 october 2022

# This program will determine how many breaths and heartbeats a person
# has had in their life

# User greeting
print('Welcome to calculate your total breaths and heartbeat. Enter your age in years')
print()

run = 'y'

while run == 'y':
    
   # User input their age
    age = float(input('Please enter your age: '))
    print()

    
   # Variable minYear
    minYear = 525600

   # Checks the age entered
    if age >= 15:
        breathsTaken = (1 * minYear * 45) + (4 * minYear * 25) + (10 * minYear * 20) + ((age - 15) * minYear * 16)
    elif age >= 5:
        breathsTaken = (1 * minYear * 45) + (4 * minYear * 25) +((age - 5) * minYear * 20)
    elif age >= 1:
        breathsTaken = (1 * minYear * 45) + ((age -1) * minYear * 25)
    else:
        breathsTaken = (age * minYear * 45)

        
    # Calculate heartbeats 
    heartbeats = age * minYear * 67.5

    # Display results
    print('You have taken about', format(breathsTaken, ',.0f'), 'breaths in your life')
    print('Your heart has beat approximately', format(heartbeats, ',.0f'), 'times')
    print()

    # Program loop
    run = input('would you like to run program again? ').lower()

    # Error check loop
    while run != 'y' and run != 'n':
        run = input ('INPUT ERROR: Please enter a (y/n): ').lower()
    print()

# Exit message
print('Have a nice day!!!!')
   
