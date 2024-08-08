class Shopping_Cart:
    items = {
        "Rice":1000,
        "Tissues":30,
        "Perfume":4000,
        "Icecream":80,
        "Watermelon":150,  
             }
    user_items = {}
    print(items)
    def adding_items(self,items):
        self.user_items[items] = self.items[items]

    def remove_items(self,items):
        del self.user_items[items]

    def total_items(self):
        print(f"Total Items : {self.user_items}")

    def total_price(self):
        total = sum(self.user_items.values())
        print("Total price : ",total)


def main():
    test1 =Shopping_Cart()
    select = int(input('Enter the Option : \n1.Adding Items\n2.Remove Items\n3.Total Items\n4.Total Price'))
    if(select == 1):
        print(Shopping_Cart.items)
        add = input('Enter the items you want : ')
        test1.adding_items(add)
        main()
    elif(select == 2):
        print(Shopping_Cart.items)
        rem = input('Enter the items that you want to remove : ')
        test1.remove_items(rem)
    elif(select == 3):
        test1.total_items()
        main()
    elif(select == 4):
        test1.total_price()
    else:
        print('choose the correct option')
        main()

if __name__ == '__main__':
     main()
