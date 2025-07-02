"""
using a fuction to come up with a simple men

"""
def menu():
    print("1. breakfast")
    print("2. lunch")

def handle_selection(selected_value):
    if selected_value == 1:
        print("you have selected Breakfast")
    elif selected_value == 2:     
        print("you have selected lunch")
    else:
        print("please enter the correct selection")
def main():
    menu()
    selected_value = int(input("please make achoice:"))
    handle_selection(selected_value)
main()