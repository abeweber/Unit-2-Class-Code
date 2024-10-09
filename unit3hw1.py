cat_age = int(input("How old is the cat in months?"))

kitten = cat_age <=6
teen = 7<= cat_age <= 11
adult = 12<= cat_age <=95
senior = 96<=cat_age<= 456

if kitten:
    print(f"The cat is a Kitten, Age:{cat_age} months old, Price: $250")
if teen:
    print(f"The cat is a Teen, Age:{cat_age} months old, Price: $225 ")
if adult:
    print(f"The cat is an Adult, Age:{cat_age} months old, Price: $150")
if senior:
    print(f"The cat is a Senior, Age:{cat_age} months old, Price: $85")