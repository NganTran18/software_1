Lots_to_gram = 13.3
Pound_to_lots = 32
Talent_to_pound = 20

talent = float(input("what is the talent? "))
pound =  float(input("what is the pound? "))
lots = float(input("what is the lots? "))

total= (talent * Talent_to_pound * Pound_to_lots * Lots_to_gram) + (pound * Pound_to_lots * Lots_to_gram) + (lots * Lots_to_gram)

kilogram = total // 1000
gram = total % 1000

print("The weight in modern units: ", kilogram, "kilogram", "and", gram, "gam "  )
print(f"The weight in modern units: {kilogram}, kiolgram and {gram:.2f} gram")
