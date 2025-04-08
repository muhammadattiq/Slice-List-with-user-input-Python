## This Prgram will allow user to slice element of list and start the list from user given starting index and ends the list on user given ending index ## ##

my_list = ['apple',33, 'orange', 45, 'pineapple']

print(my_list)

choice1 = int(input("please enter the index from which you want to start the List :"))

choice2 = int(input("please enter your the index before which you want to end the list :"))

def slice_list(num1,num2):
    print(f"your desired sliced list {my_list[num1:num2]}")

slice_list(choice1,choice2)