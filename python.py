name = input("what's your name? \n")
password = input("write your password \n")
password_length =len(password)
hidden_password = "*" * password_length
print(f"Hey! {name} your password is {hidden_password} and it is of {len(password)} length")
