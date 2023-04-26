print("Welcome to the Secret Auction Program.")


should_continue=True
result={}

while should_continue:
    name = input("What is your name?")
    bid = float(input("What's your bid?"))
    result[name] = bid
    res = input("Are there any other bidders? Type 'yes or 'no")
    if res=="no":
        should_continue=False

#print(result)

max=0.0
winner_name=""

for x in result:
    if result[x]>max:
        max=result[x]
        winner_name=x

print(f"The winner is {winner_name} with a bid of ${max}." )





