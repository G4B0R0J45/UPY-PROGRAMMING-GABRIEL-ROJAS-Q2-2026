
SEQUENCE = [2, 3, 4, 5, 6, 7]
 
# INPUT 
rol = input("Enter UTFSM rol (digits only, no hyphen): ")
 
# PROCESS 
reversed_rol = rol[::-1]
 
total = 0
for i, digit in enumerate(reversed_rol):
    total += int(digit) * SEQUENCE[i % 6]
 
remainder = total % 11
result    = 11 - remainder
 
if result == 11:
    check_digit = "0"
elif result == 10:
    check_digit = "K"
else:
    check_digit = str(result)
 
# OUTPUT
print(f"Check digit : {rol}-{check_digit}")