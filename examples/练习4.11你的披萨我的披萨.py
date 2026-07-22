favourite_pizza=["Margherita Pizza", "Pepperoni Pizza", "BBQ Chicken Pizza", "Hawaiian Pizza", "Veggie Pizza"]
friend_pizza=favourite_pizza[:]
favourite_pizza.append("Meat Lovers Pizza")
friend_pizza.append("Buffalo Chicken Pizza")
print("My favourite pizzas are:")
for pizza in favourite_pizza:
    print(pizza)
print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizza:
    print(pizza)
