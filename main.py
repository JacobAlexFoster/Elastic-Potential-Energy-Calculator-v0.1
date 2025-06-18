import math

print("Which two parts of the equation do you know?")
print("Elastic Potential Energy = Ee")
print("Spring Constant = k")
print("Extension/Compression = x")

x = input("First known variable (Ee/k/x): ").strip().upper()
y = input("Second known variable (Ee/k/x): ").strip().upper()

if x == "k" and y == "x":
    k = float(input("Spring Constant (N/m): "))
    x = float(input("Extension/Compression (m): "))
    Ee = 0.5 * k * x**2
    print(f"Elastic Potential Energy (Ee): {Ee} Joules")

elif x == "Ee" and y == "k":
    Ee = float(input("Elastic Potential Energy (J): "))
    k = float(input("Spring Constant (N/m): "))
    x = math.sqrt((2 * Ee) / k)
    print(f"Extension/Compression (x): {x} meters")

elif x == "Ee" and y == "x":
    Ee = float(input("Elastic Potential Energy (J): "))
    x = float(input("Extension/Compression (m): "))
    k = (2 * Ee) / x**2
    print(f"Spring Constant (k): {k} N/m")

else:
    print("Invalid input. Please enter Ee, k, or x.")