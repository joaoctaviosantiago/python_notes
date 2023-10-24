
bill = float(input("Bill: "))
tip = float(input("Tip: "))
calculated_tip = bill * (tip / 100)
total = bill + calculated_tip

print(f"Bill: {bill}")
print(f"Tip: {tip}%")
print(f"Total: ${'%.2f' % total}")
