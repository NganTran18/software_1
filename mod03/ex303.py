female_gender = input("what is the biological gender? ")
male_gender = input("what is the biological gender? ")
female_value = float(input("what is the  hemoglobin value of female? "))
male_value = float(input("what is the  hemoglobin value of male? "))

if female_value < 117:
    print("low, pay attention!")
elif 117 <= female_value <= 155:
    print("normal, good")
elif female_value > 155:
    print("high, pay attention")

if male_value < 134:
    print("low, pay attention!")
elif 134 <= male_value <= 167:
    print("normal, good")
elif male_value > 167:
    print("high, pay attention")