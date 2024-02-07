def hello():
    print("Hello, Welcome to my Python file!")

def pack(fruit1, fruit2, fruit3):
    return [fruit1, fruit2, fruit3]

result = pack("orange", "strawberries", "blueberries")
print(result)

def eat_lunch(food_list):
    if not food_list:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

eat_lunch(["chips", "sandwich", "cookies"])
eat_lunch([])

