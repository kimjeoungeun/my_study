age = 16
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken :
    print("치킨을 먹는다.")
    money=money=chicken
if money >= beer and age >= 20:
    print("맥주를 마신다.")
    money=money-beer
if money >= drink :
    print("음료수를 마신다.")
    money=money-drink

print("1-마실거리를 1개만 먹어야 할 경우")
if money >= chicken + beer and age >= 20 :
    print("치킨과 맥주를 먹는다.")
elif money >= chicken + drink :
    print("치킨과 음료수를 먹는다.")
elif money >= chicken : 
    print("치킨만 먹는다")
elif money >= drink :
    print("음료수만 먹는다.")
else :
    print("아무것도 못먹는다.")

print("2-음료 두가지 이상 먹을 수 있을 경우")
if money >= chicken + beer + drink and age >= 20 :
    print("치킨과 맥주, 음료수를 먹는다.")
elif money >= chicken + beer and age >= 20 :
    print("치킨과 맥주를 먹는다.")
elif money >= chicken + drink :
    print("치킨과 음료수를 먹는다.")
elif money >= chicken : 
    print("치킨만 먹는다")
elif money >= beer + drink and age >= 20 :
    print("맥주와 음료수를 먹는다.")
elif money >= beer and age >= 20 :
    print("맥주만 먹는다.")
elif money >= drink :
    print("음료수만 먹는다.")
else :
    print("아무것도 못먹는다.")
