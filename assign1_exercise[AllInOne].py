#Initialize Variables
menu_list= ["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzaziki", "paidakia"]

#Menu Options
print('\n')
print("WELCOME TO 1st ASSIGNMENT")

def menu():
    print('\n')
    print('______________MENU_______________')
    print("FOR 1st EXERSICE PRESS: '1'")
    print("FOR 2nd EXERCISE PRESS: '2'")
    print("FOR 3rd EXERCISE PRESS: '3'")
    print("FOR 4th EXERCISE PRESS: '4'")
    print('\n')
    print("FOR EXIT PRESS: 0")
    print('\n')

menu()
option=(int(input("Enter your option: ")))


#Main Structure
while (option!=0):
    if option == 1:
      print('\n')
      print('_______________________________________________')
      print('Exercise 1')
      print('_______________________________________________')
      print('\n')
      
      count=0
      for x in menu_list:
            count=count +1
            print(x)

      print('\n')
      print('Total number of items')
      print(count)
      
      menu()
      option=(int(input("Enter your option: ")))

    elif option == 2:
       
       print('_______________________________________________')
       print('Exercise 2')
       print('_______________________________________________')
       print('\n')
       


       i=0
       allInOneList=[]
       while i<len(menu_list):
           allInOneList+=menu_list[i]
           i += 1

       counter_a=0
       counter_e=0
       counter_i=0
       counter_o=0
       counter_u=0
       for i in range(0,len(allInOneList),1):
          if 'a' == allInOneList[i]:
                 counter_a+=1
          elif 'e' == allInOneList[i]:
                 counter_e+=1
          elif 'i' == allInOneList[i]:
                 counter_i+=1
          elif 'o' == allInOneList[i]:
                 counter_o+=1
          elif 'u' == allInOneList[i]:
                 counter_u+=1
          else: counter=0

       print('The letter "a" appears %d times' % counter_a)
       print('The letter "e" appears %d times' % counter_e)    
       print('The letter "i" appears %d times' % counter_i)
       print('The letter "o" appears %d times' % counter_o)
       print('The letter "u" appears %d times' % counter_u)
       menu()
       option=(int(input("Enter your option: ")))

    elif option==3:
       
       
       print('_______________________________________________')
       print('Exercise 3')
       print('_______________________________________________')
       print('\n')

       for x in range(len(menu_list)):
          word=menu_list[x]
          print(word[::-1])

       menu()
       option=(int(input("Enter your option: ")))

    elif option==4:
       
       print('_______________________________________________')
       print('Exercise 4')
       print('_______________________________________________')
       print('\n')
       

       thisdict = { }
       for i in range(0,len(allInOneList),1):
          thisdict[allInOneList[i]] = counter_a


       letters={}
       letters.update({"a": counter_a,
               "e": counter_e,
               "i": counter_i,
               "o": counter_o,
               "u": counter_u}
        )

       print(letters)
       menu()
       option=(int(input("Enter your option: ")))
    
    else: 
        print('\n')
        print("Invalid Opion...Please Choose:")
        print('\n')
        menu()
        option=(int(input("Enter your option: ")))