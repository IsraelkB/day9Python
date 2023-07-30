from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("welcome to the secret auction program.")

auction = {}
keep_running = True
while keep_running:
  name = input("what is your name?\n")
  bid = int(input("what is your bid?: $"))
  auction[name] = bid
  other_bidder = input("are there any other bidders? type 'yes' or 'no'.\n")
  if other_bidder == 'no':
    keep_running = False
  else:
    clear()

max_bid = 0
name_of_max = ""
for names in auction:
  if auction[names] > max_bid:
    max_bid = auction[names]
    name_of_max = names

print(f"the winner is {name_of_max} with a bid of ${max_bid}")
