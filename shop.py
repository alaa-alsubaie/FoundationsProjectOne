####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Delicious"
signature_flavors = ["sunshine", "moonlight", "magnificencee", "unique"]
order_list = []


def print_menu():
    """
        Print the items in the menu dictionary.
        """
    print()
    print("Our menu:")
    for y in menu:
      print (y +": "+ str(menu[y]))
    print()


def print_originals():
    """
        Print the original flavor cupcakes.
        """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for o in original_flavors:
      print (o)

    print()


def print_signatures():
    """
        Print the signature flavor cupcakes.
        """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for s in signature_flavors:
     print (s)

    print()



def is_valid_order(order):
    """
        Check if an order exists in the shop.
        """
    t = 0
    for m in menu:
        if order == m:
            t = t+1
        else:
            t = t+0

    for o in original_flavors:
        if order == o:
            t = t+1
        else:
            t = t+0

    for s in signature_flavors:
        if order == s:
            t = t+1
        else:
            t = t+0

    if t>0:
      return True
    else:
      return False


def get_order():
    """
        Repeatedly ask customer for order until they end their order by typing "Exit".
        """
    order_list = []
    order = input("What is your order?\n")
    while order.lower() != "exit":
        if is_valid_order(order.lower()) == False:
            print ("Sorry .. It' not available! Please retype the order again in the same exact spelling and capitalization of the item")
            order = input()
        else:
            order_list.append(order)
            order = input()
                
    return order_list



def accept_credit_card(total):
    """
        Return whether an order is eligible for credit card payment.
        """
    if total >= 5:
        text = "This order is eligible for credit card payment "
    else:
        text = "This order is not eligible for credit card payment"
            
    return text




def get_total_price(order_list):
    """
        Calculate and return total price of the order.
        """
    total = 0
    for items in order_list:
        for m in menu:
            if items == m:
                total = total + menu[m]
            else:
               continue
    for items in order_list:
        for o in original_flavors:
            if items == o:
                total = total + original_price
            else:
               continue
    for items in order_list:
        for s in signature_flavors:
            if items == s:
                total = total + signature_price
            else:
               continue
                        
    return total



def print_order(order_list):
    """
        Print the order of the customer.
        """
    print()
    print("Your order is: ")
    for list in order_list:
     print (list)
    print ("\n")
    t = get_total_price(order_list)
    print("The total is"+" "+str(t)+" KD")
    print (accept_credit_card(t))
    print("Thank you for shopping at Delicious ")








