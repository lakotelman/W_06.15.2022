

class Product: 
    def __init__(self, name: str, quantity: int): 
        self.name = name
        self.quantity = quantity
    def __str__(self): 
        return f"{self.quantity}: {self.name}"


class ShoppingCart: 
    def __init__(self):
        self.cart: list[Product] = []

    def shopping_add(self): 
        while True:
            name = input("What item would you like to add? (Use [b] to go back) ").strip()
            if name == "b":
                break
            else:
                quantity = input("How many would you like? ").strip()
                entry = Product(name, quantity)
                self.cart.append(entry)


    def shopping_remove(self): 
        while True: 
            question = input("Are you [r]emoving or [c]hanging quantity? (Use [b] to go back) ").strip()
            if question == "b": 
                break
            elif question == "r": 
                rmitem = input("Which item would you like to [r]emove? ")
                try:
                    target = None
                    for obj in self.cart: 
                        if obj.name == rmitem: 
                            target = obj
                            break
                    self.cart.remove(target)
                    print(f"Got it! Removed {target} from your list")
                    print("-" * 20)
                except ValueError: 
                    print("That's not on your list, silly. ")
                    print("-" * 20) 
            elif question == "c": 
                reviseitem = input ("Which item did you want to change the quantity for? ")
                print("-" * 20)
                try:
                    for obj in self.cart:
                        if obj.name == reviseitem:
                            newquant = int(input("How many do you actually want? "))
                            obj.quantity = newquant
                            print(f"Gotcha. Changed your list to have {newquant} {obj.name}")
                            print("-" * 20)
                except ValueError: 
                    print("That's not on your list, silly. ")

                
                    

    def shopping_view_list(self): 
        for obj in self.cart:
            print(obj)
        print("=" * 20)
        
class ShopTime: 
    def __init__(self):
        self.new_cart = ShoppingCart() 
        
    def greeting(self): 
        print("----------------------------------------")
        print("--------------Shopping List-------------")
        print("----------------------------------------")

    def instructions(self):
        print("Instructions:")
        print(" - Use [q] at anytime to quit and print your list")
        print(" - Use [a] to add items")
        print(" - Use [r] to revise items")
        print(" - Use [v] to view your list progress")
        print(" - Use [i] to see these instructions again")

    def shop(self):
        self.greeting()
        self.instructions()
        while True:
            cue = input("What would you like to do? ").lower().strip() 
            if cue == "q" and not self.new_cart.cart:

                print("See ya!") 
                break
            elif cue == "q" and self.new_cart.cart:

                print("\nHere's your list!\n")
                for items in self.new_cart.cart:

                    print(f"- {items}")
                print("\nSee ya!")
                break    
            elif cue == "a": 
                self.new_cart.shopping_add()
            elif cue == "r": 
                self.new_cart.shopping_remove()
            elif cue == "v": 
                self.new_cart.shopping_view_list()
            elif cue =="i": 
                self.instructions()
            else: 
                print("I didn't get that command. Press [i] to repeat instructions. ")
    

todaylist = ShopTime()
todaylist.shop()


