guest_list = ['cousin', 'mom', 'dad', 'brother', 'aunty', 'sister', 'nephew']
message = "Sorry, but I can only invite two people for the dinner now our new dinner table won't arrive in time for it"
print(message)
first_uninvited = guest_list.pop(0)
print(f"I am sorry I had to, but I can't invite you again {first_uninvited.title()}.")
second_uninvited = guest_list.pop()
print(f"I am sorry I had to, but I can't invite you again {second_uninvited.title()}.")
third_uninvited = guest_list.pop(4)
print(f"I am sorry I had to, but I can't invite you again {third_uninvited.title()}.")
fourth_uninvited = guest_list.pop(3)
print(f"I am sorry I had to, but I can't invite you again {fourth_uninvited.title()}.")
fifth_uninvited = guest_list.pop(-2)
print(f"I am sorry I had to, but I can't invite you again {fifth_uninvited.title()}.")

print(f"You have been selected to come with me for the dinner {guest_list[1]}.")
print(f"You have been selected to come with me for the dinner {guest_list[2]}.")