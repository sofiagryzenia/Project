# import the random module
import random

# create the class Dice
class Dice:
    # create the constructor (__init__) method
    # it takes as input the number sides and if none is specified use 6
    # it sets the dice object's number of sides (instance variable)
    # it sets the list that tracks the rolls to the empty list (instance variable)
    def __init__(self, sides):
        user_input = int(input("Enter number of sides"))
        if user_input == "":
            self.sides = 6
        self.sides = sides
        self.roll_lst = []
        self.roll_lst.append(user_input)

    # create the __str__ method
    # it returns "Last roll: value" where value is the last value in the list that tracks the rolls
    def __str__(self):
        return "Last roll: " + self.roll_lst[-1]

    # create the roll method
    # it randomly picks a value from 1 to the number of sides this dice object has
    # it adds that value to the end of the list that tracks all the rolls
    # it returns the value
    import random 

    def roll(self, random):
        self.random = random.randrange(1,self.sides + 1)
        self.roll_lst.append(self.random)
        return self.random

    
    def num_rolls(self):
        input2 = int(input("How many times do you want to roll?"))
        for roll in self.roll_lst:
            print(roll)

    # BONUS
    # create the print_count_for_num method
    # it will count how many times the passed number has been rolled and print 
    # number was rolled x times - where number is the number and x is the count

    def print_count_for_num(self, num):
        count = 0
        self.num = num
        if num in self.rol_lst:
            count += 1
            print(self.num, " was rolled ", count, "times")

# main function
def main():
    
    # Create an instance
    three_sided = Dice(3)
    print("Three sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(three_sided.roll())

    # Print last roll
    print(three_sided)

    # Create an instance
    six_sided = Dice()
    print("\nSix sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(six_sided.roll())

    # Print last roll
    print(six_sided)

    # BONUS quiz
    # Print accumulation
    six_sided.print_count_for_num(3)

if __name__ == "__main__":
    main()