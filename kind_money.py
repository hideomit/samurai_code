kind_money = {
    "一万円札" : 10000,
    "五千円札" : 5000,
    "千円札":1000,
    "五百円玉":500,
    "百円玉":100,
    "五十円玉":50,
    "十円玉":10,
    "五円玉":5,
    "一円玉":1
}

class Payment:
    
    def culc(self):
        
        try:
            
            amount = int(input("金額を入力してください"))
            print("金額：{} 円".format(amount))
        
            while amount != 0:
            
                if amount >= 10000:
                    money = amount // kind_money["一万円札"]
                    amount = amount - (kind_money["一万円札"] * money)
                    print("一万円札= {} 枚".format(money))
        
                elif amount >= 5000 and amount < 10000:
                    money = amount // kind_money["五千円札"]
                    amount = amount - (kind_money["五千円札"] * money)
                    print("五千円札={} 枚".format(money))
                
                elif amount >= 1000 and amount < 5000:
                    money = amount // kind_money["千円札"]
                    amount = amount - (kind_money["千円札"] * money)
                    print("千円札= {} 枚".format(money))
            
                elif amount >= 500 and amount < 1000:
                    money = amount // kind_money["五百円玉"]
                    amount = amount - (kind_money["五百円玉"] * money)
                    print("五百円玉= {} 個".format(money))
            
                elif amount >= 100 and amount < 500:
                    money = amount // kind_money["百円玉"]
                    amount = amount - (kind_money["百円玉"] * money)
                    print("百円玉= {} 枚".format(money))
            
                elif amount >= 50 and amount < 100:
                    money = amount // kind_money["五十円玉"]
                    amount = amount - (kind_money["五十円玉"] * money)
                    print("五十円玉= {} 個".format(money))
                
                elif amount >= 10 and amount < 50:
                    money = amount // kind_money["十円玉"]
                    amount = amount - (kind_money["十円玉"] * money)
                    print("十円玉= {} 個".format(money))
            
                elif amount >= 5 and amount < 10:
                    money = amount // kind_money["五円玉"]
                    amount = amount - (kind_money["五円玉"] * money)
                    print("五円玉= {} 個".format(money))
            
                else:
                    money = amount // kind_money["一円玉"]
                    amount = amount - (kind_money["一円玉"] * money)
                    print("一円玉= {} 個".format(money))
            
        except ValueError:
            print("整数値を入力してください")
            

payment = Payment()

payment.culc()