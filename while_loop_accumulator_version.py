def get_starting_number():
    while True:
        num = input("How many bottles of beer on the wall? ")
        if num.isdigit() and int(num) >= 1:
            return int(num)
        print("Please enter a valid number (1 or greater).")

def sing(starting_number):
    bottles = starting_number
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            if bottles - 1 == 1:
                print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
        bottles -= 1

if __name__ == "__main__":
    start = get_starting_number()
    sing(start)
