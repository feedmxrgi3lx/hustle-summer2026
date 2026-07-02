# Alexander Mendoza | lab 4 | intro to python
#ticket 1
# it will likely give access to those 13 and above
#
ages = [17,11,25,13,]

for age in ages:
    if age >= 13:
        print("access grandted)")
    else:
        print("access denied")

#tiket 2
#if no is typed it wlll probably end the loop not allowing it to run
#it is less complicated
keep_going = "yes"

while keep_going == "yes":
    age = int(input("check another?"))
    if age >=13:
        print(f"{age} - access granted")
    else:
        print(f"{age} - too young")
    keep_going = input("check another age? (yes/no)"):
    
#ticket 3
#if I forgotto place the break function the code would probably keep continuing.
# this one puts anend to the prompt by adding stop
while True: keep_going == "stop"
age = int(input("enter an age","stop"))
    if age : "stop"
 break
else:
print(f"{age}-continue")

#ticket 4
#it actually allows for something to occur when age is put
#it probably is much more simpler and states that someting is true
def can_access(parameter):
    if age >= 13:
        return True
    else:
        return False
    can_access("access granted")

#ticket 5
#4
#funtioms
def signup_report(parameter):
    for num, item in enumerate(my_list, start=1):
        signups = [22, 10, 15, 8, 19, 13]
        print(f"{num}. {item}")