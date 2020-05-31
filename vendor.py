import os

vendor_dic = {
        "Cola":110,
        "Water":90,
        "tea":160
        }


class Vendor:
    
    def __init__(self):
        for i in vendor_dic:
            print(i)
    
    def buy(self):
        item = input("購入する商品を選んでください")
    
        if item in vendor_dic:
            amount = input("金額を入力してください")
                
            if int(amount) >= vendor_dic[item]:
                print("{}を購入しました".format(item))
                print("おつりは{}円です".format(int(amount) - vendor_dic[item]))
            else:
                print("投入金額が不足しています")
                print("{}円足りません".format(vendor_dic[item] - int(amount)))
            
        else:
            
            Continue = "none"
            
            while(Continue != "yes" and Continue != "no"):
                
                Continue = input("該当商品がありません。購入を続けますか？(yes/no)")
            
                if Continue == "yes":
                    os.system('clear')
                    return 0
                
                elif Continue == "no":
                    print("ありがとうございました")

            
vendor = Vendor()

while(vendor.buy() == 0):
    del vendor
    vendor = Vendor()