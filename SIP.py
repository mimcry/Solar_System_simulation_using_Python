# lets make SIP calculator


def sip_calculator(monthly_investmeny, Expected_annual_return, Time_period):
    monthly_rate = (Expected_annual_return/100)/12
    total_month = Time_period*12
    future_value = monthly_investmeny
    for month in range(total_month):
        future_value += monthly_investmeny
        future_value *= (1+monthly_rate)

    return future_value


monthly_investmeny = float(input("What is your monthly investment: \n"))
Expected_annual_return = float(input("What is your Expected annual return :\n"))
Time_period = int(input("How many years do you want to invest for? : \n"))
maturity = sip_calculator(monthly_investmeny, Expected_annual_return, Time_period)
print(maturity)

# Yearly = 12*monthly_investmeny

# Total_investment = Yearly*Time_period
# print(Total_investment)


# Yearly_Return = ((Expected_annual_return)/100)*monthly_investmeny
# monthly_return = Yearly_Return/12
# Balance1 = monthly_investmeny + monthly_return
# Yearly_Return1 = ((Expected_annual_return)/100)*monthly_investmeny
# monthly_return1= Yearly_Return1/12
# For_next_month= Balance1+monthly_return1
# Balance2= Balance1+For_next_month
# Total_balance = Balance2*30


# print(Total_balance)
