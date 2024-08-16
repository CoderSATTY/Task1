#Task 1 : Modern Calculator
print("Hello User, This is a Modern Calculator!\n")
flag = True
while flag==True:
        choice = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Solve Linear Equation\n6.Solve Quadratic Equation\n7.Trigonometry Function\n8.Logarithmic Function\nSelect your operation by typing it's operation number:\n"))
        if choice==1:
                print("Enter two numbers you want to add:")
                num1 = int(input("First Number:"))
                num2 = int(input("Second Number:"))
                result = num1+num2
                print(f"Result of {num1}+{num2} is: ",result )
        elif choice==2:
                print("Enter two numbers you want to subtract:")
                num1 = int(input("First Number:"))
                num2 = int(input("Second Number:"))
                result = num1-num2
                print(f"Result of{num1}-{num2}: ", result)
        elif choice==3:
                print("Enter two numbers you want to multiply:")
                num1 = int(input("First Number:"))
                num2 = int(input("Second Number:"))
                result =  num1*num2
                print(f"Result of{num1}*{num2}: ", result)
        elif choice==4:
                print("Enter two numbers you want to divide:")
                num1 = int(input("First Number:"))
                num2 = int(input("Second Number:"))
                if num2==0:
                    print("Does not exist!")
                else:
                     print(f"Result of{num1}/{num2}: ",num1/num2)
        elif choice==5:
             print("Enter a1,a2,b1,b2,c1,c2 for solving 2 linear equations of form:\na1x + b1y = c1\na2x + b2y = c2\n")
             a1=float(input("a1 = "))
             a2=float(input("a2 = "))
             b1=float(input("b1 = "))
             b2=float(input("b2 = "))
             c1=float(input("c1 = "))
             c2=float(input("c2 = "))
             D = float(a1*b2 - a2*b1)
             D1 = float(b1*c2 - b2*c1)
             D2 = float(a1*c2 - a2*c1)
             print(f"So your linear equations are {a1}x + {b1}y = {c1} and {a2}x + {b2}y = {c2}")
             x = D1/D   
             y = D2/D
             if D==0:
                 print("There are infinite solutions!")
             else:
                print("The value of x is ",x)
                print("The value of y is ",y)
        elif choice==6:
              print("For a quadratic equation of type ax\u00b2 + bx + c, Enter a, b and c:")
              a = float(input("a = "))
              b = float(input("b = "))
              c = float(input("c = "))
              print(f"So your Quadratic Equation is {a}x\u00b2 + {b}x + {c}")
              D = b**2 - 4*a*c
              x1 = (-b + D**0.5)/2*a
              x2 = (-b - D**0.5)/2*a
              if D>0:
                    print(f"It has real and unequal roots and they are {x1} and {x2}")
              elif D==0:
                    print(f"It's roots are real and equal and the root is {x1}")
              else:
                    print("It's roots are imaginary")
        elif choice==7:   
            print("Which function to use?\n1.Sinx\n2.Cosx\n3.tanx\n4.secx\n5.cosecx\n6.cotx\n")
            opt=int(input("Type Trigo function number: "))
            def factorial(p):
                    if p == 0:
                     return 1
                    else:
                     return p * factorial(p - 1) 
            if opt==1:
                def sin(x):
                    sine = 0
                    for i in range(0,51):
                        sign = (-1)**i
                        pi=22/7
                        y=x*(pi/180)
                        sine = sine + ((y**(2.0*i+1))/factorial(2*i+1))*sign
                    print(f"Sin{x}= ")
                    return sine
                print(sin(x=float(input("Enter the value of x in degrees: ")))) 
            elif opt==2:
               def cosine(x):
                    cosx = 1
                    sign = -1
                    for i in range(2, 50, 2):
                        pi=22/7
                        y=x*(pi/180)
                        cosx = cosx + (sign*(y**i))/factorial(i)
                        sign = -sign
                    print(f"Cos{x}= ")
                    return cosx
               print(cosine(x=float(input("Enter the value of x in degrees: "))))
            elif opt==3:
                x = int(input("Enter the value of x in degrees:"))
                tanx = (sin(x)) / (cosine(x))
                print(f"Tan{x}= \n",tanx)
            elif opt==4:
              x = int(input("Enter the value of x in degrees:"))
              secx = 1/(cosine(x))  
              print(f"Sec{x}= ",secx) 
            elif opt==5:
              x = int(input("Enter the value of x in degrees:"))
              cosecx = 1/(sin(x))  
              print(f"Cosec{x}= ",cosecx)
            elif opt==6:
              x = int(input("Enter the value of x in degrees:"))
              cotx = 1/(tanx)  
              print(f"Cot{x}= ",cotx)
        elif choice==8:
            num = float(input("Enter the number whose logarithm is to be found: "))
            numb = num
            i = 0
            while True:
                if num >= 1:
                    i = i+1
                    num = float(num/10)
                else:
                    break
            gif = float(i) - 1
            frac = round(num,1)
            log1 = 0
            log2 = 0.3010
            log3 = 0.4771
            log4 = 2 * log2
            log5 = 0.6989
            log6 = log2 + log3
            log7 = 0.8450
            log8 = 3 * log2
            log9 = 2 * log3
            if frac==0.1:
                frac = log1
                print(f"Approx value for Log of {numb} is: \n", gif + log1)
            elif frac==0.2:
                print(f"Approx value for Log of {numb} is: \n", gif + log2)
            elif frac==0.3:
                print(f"Approx value for Log of {numb} is: \n", gif + log3)
            elif frac==0.4:
                print(f"Approx value for Log of {numb} is: \n", gif + log4)
            elif frac==0.5:
                print(f"Approx value for Log of {numb} is: \n", gif + log5)
            elif frac==0.6:
                print(f"Approx value for Log of {numb} is: \n", gif + log6)
            elif frac==0.7:
                print(f"Approx value for Log of {numb} is: \n", gif + log7)
            elif frac==0.8:
                print(f"Approx value for Log of {numb} is: \n", gif + log8)
            elif frac==0.9:
                print(f"Approx value for Log of {numb} is: \n", gif + log9)
            else:
                print(f"Log of {numb} is: \n", gif + frac)                                  
        ask = int(input("Do you want to continue?\nType 1 for \"Yes\" \nType 2 for \"No\"\n"))
        while True:
            if ask == 1:
               print("Lets go again:")
               break
         
            else:
                print("Thanks for using Modern Calculator!")
                flag=False
                break
        

    
    

     
    


