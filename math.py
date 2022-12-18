#make a program that calculates every combination of operations between 4 numbers until get 10 and if needs to divide by 0 will skip that operation

import itertools

def main():
    #input numbers and put them in a list
    numbers = []
    for i in range(4):
        try:
            numbers.append(int(input("Numero"+str(i+1)+": ")))
        except ValueError:
            print("Error: Solo se aceptan numeros")
            exit()
    operations = ['+','-','*','/']
    for i in itertools.product(operations, repeat=3):
        for j in itertools.permutations(numbers):
            a = j[0]
            b = j[1]
            c = j[2]
            d = j[3]
            op1 = i[0]
            op2 = i[1]
            op3 = i[2]
            if op1 == '+':
                if op2 == '+':
                    if op3 == '+':
                        try:
                            if a + b + c + d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '-':
                        try:
                            if a + b + c - d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '*':
                        try:
                            if a + b + c * d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass

                    if op3 == '/':
                        try:
                            if a + b + c / d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                if op2 == '-':
                    if op3 == '+':
                        try:
                            if a + b - c + d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '-':
                        try:
                            if a + b - c - d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '*':
                        try:
                            if a + b - c * d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '/':
                        try:
                            if a + b - c / d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                if op2 == '*':
                    if op3 == '+':
                        try:
                            if a + b * c + d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '-':
                        try:
                            if a + b * c - d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '*':
                        try:
                            if a + b * c * d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '/':
                        try:
                            if a + b * c / d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                if op2 == '/':
                    if op3 == '+':
                        try:
                            if a + b / c + d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '-':
                        try:
                            if a + b / c - d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '*':
                        try:
                            if a + b / c * d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '/':
                        try:
                            if a + b / c / d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
            if op1 == '-':
                if op2 == '+':
                    if op3 == '+':
                        try:
                            if a - b + c + d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '-':
                        try:
                            if a - b + c - d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '*':
                        try:
                            if a - b + c * d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                    if op3 == '/':
                        try:
                            if a - b + c / d == 10:
                                print(a,op1,b,op2,c,op3,d)
                        except ZeroDivisionError:
                            pass
                

if __name__ == "__main__":
    while True:
        main()