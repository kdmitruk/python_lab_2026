
while True :
    angle = float(input("Kąt: "))
    if angle <= 0 or angle >= 90:
        print("Wartość nie jest odpowiednia!")
    else:
        break

velocity = float(input("Prędkość początkowa: "))

print(velocity)
print(angle)
