email=input("Enter your Email :- ")
email=email.strip()
slicer_index=email.index("@")
user_name=email[:slicer_index]
domain_name=email[slicer_index+1:]
print(f"Your user name {user_name} and domain is {domain_name}")