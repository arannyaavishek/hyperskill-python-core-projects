import random
random.seed()

run = 1
correct = 5
runs = 5

def greeting():
    print("Which level do you want? Enter a number:"
          "\n1 - simple operations with numbers 2-9"
          "\n2 - integral squares of 11-29")


def simple():
    global runs
    global correct

    while runs:
        a = str(random.randint(2, 9))
        b = str(random.randint(2, 9))
        signs = ['+', '-', '*']
        sign = ''.join(random.choices(signs))
        global expression
        expression = a + ' ' + sign + ' ' + b
        print(expression)
        correct_input = True
        while correct_input:
            try:
                answer = int(input())
            except:
                print("Incorrect format.")
                continue
            else:
                correct_input = False

        if eval(expression) == answer:
            print('Right!')
            runs -= 1
        else:
            print('Wrong!')
            correct -= 1
            runs -= 1


def integral():
    global runs
    global correct
    
    while runs:
        a = str(random.randint(11, 29))
        global expression
        expression = a
        print(expression)

        correct_input = True
        while correct_input:
            try:
                answer = int(input())
            except:
                print("Incorrect format.")
                continue
            else:
                correct_input = False

        expression = expression + "*" + expression

        if eval(expression) == answer:
            print('Right!')
            runs -= 1
        else:
            print('Wrong!')
            correct -= 1
            runs -= 1


def process_choice():
    global run
    global option
    while run:
        try:
            greeting()
            global choice
            choice = int(input())
            run -= 1
        except:
            print("Incorrect format.")
            continue
        else:
            if choice in [1, 2]:
                if choice == 1:
                    simple()
                    option = "(simple operations with numbers 2-9)"
                else:
                    integral()
                    option = "(integral squares of 11-29)"
            else:
                print("Incorrect format.")


process_choice()
print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
saving = input()
if saving in ["yes", "YES", "y", "Yes"]:
    print("What is your name?")
    name = input()
    my_file = open('results.txt', 'a')
    my_file.write(f'{name}: {correct}/5 in level {choice} {option}.')
    my_file.close()
    print('The results are saved in "results.txt".')
