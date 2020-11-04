import math 

print("Возняк Софія ІС-01")
print("Варіант 28")

e = 0
print("Введіть a > 0: ") #Введення а
a = float(input())
x0 = 0
if a <= 0: # якщо а < 0, програма вибиватиме помилку
    print("ERROR input unsigned value more 0")
    e=-1
elif a <= 1:  # перевірка зкачення а і присвоєння значення х0 в залежності від а
    x0 = min(2*a, 0.95)
elif (a > 1) & (a < 25):
    x0 = a/5
else: 
    x0 = a/25

if e==0: # якщо а > 0, програма запускається  далі
    print("x0 = ",x0)
    x_nm1 = x0 # присвоєння попередньому члену ряду початкове значення х0
    x_n = 0
    result = 0
    
    while True:
        x_n = 4/5*x_nm1 + a/(5*math.pow(x_nm1,4)) #формула для знаходження н-го члена ряда
        x_np1 = 4/5*x_n + a/(5*math.pow(x_n,4)) #формула для знаходження наступного члена ряда
        c = 5/4*a*abs(float(x_np1)-x_n) 
        print("x_n = ","%13.10f" % (x_n), " c = ","%14.13f" % (c)) 

        if c < math.pow(10,-6): #перевірка, чи виконується нерівність для поточного члена ряда
            print("x_np1 =","%.10f" % (x_np1))
            result = a - math.pow(x_n,5) # розрахунок різниці для першого члена ряда, у якого виконалась нерівність
            print("Result:","%.15f" % (result))  # Вивід остаточної різниці
            break # припинення циклу

        x_nm1 = x_n # присвоєння для попереднього члена наступного значення для подальшого продовження циклу
    
      
    
