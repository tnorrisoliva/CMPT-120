def main():

    '''ask the user for their age. If the user is 25 or older, tell them they can buy alcohol, nicotine products, and they can rent a car
        If they're 21 or older but younger than 25, tell them they can buy alcohol and nicotine products, but cannot rent a car
        If they're 18 and older but younger than 21, tell them they can only buy nicotine products in some states
        If they're less than 18, they can only purchase candy cigarettes and sody pops
    '''
    age= input("Enter your age")

    if int(age) >= 25 :
        print("you can buy alc,nic and rent a car")
    elif int(age) < 25 and int(age) >= 21:
        print("you can buy alc and nic but you cannot rent a car")
    elif int(age) <21 and int(age) >= 18:
        print("you can only buy nic in some states")
    else:
        print("you can only buy candy cigarettes and soda")
        print(".")
        print(".")
        print(".")
        print("nerd")
  

  
  
  
main()
