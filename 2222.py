def sip_calculator(principal, monthly_contribution, rate_of_return, years):
    # Convert annual rate of return to monthly rate
    monthly_rate = (rate_of_return / 100) / 12
    
    # Calculate total number of months
    total_months = years * 12
    
    # Initialize the future value
    future_value = principal
    
    # Calculate the future value using the compound interest formula
    for month in range(total_months):
        future_value += monthly_contribution
        future_value *= (1 + monthly_rate)
    
    return future_value

# Get input from the user
principal = float(input("Enter the initial investment amount: "))
monthly_contribution = float(input("Enter the monthly contribution amount: "))
rate_of_return = float(input("Enter the expected annual rate of return (%): "))
years = int(input("Enter the number of years: "))

# Calculate and display the SIP maturity value
maturity_value = sip_calculator(principal, monthly_contribution, rate_of_return, years)
print(f"The maturity value after {years} years is: {maturity_value}")
