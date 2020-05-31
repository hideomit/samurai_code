import math

class Loan:
    
    def returnLoan(self):
        
        try:
            amount = int(input("借金の金額を入力してください"))
            rate = float(input("利息の年利率（％）を入力してください"))/100
            amount_r = int(input("月々の返済額を入力してください"))
        
            i = 1
            all_r = 0
        
            while amount > 0:
            
                interest_m = math.ceil((amount * rate)/12) #月額利息(切り上げ)
                amount = amount + interest_m
                amount = amount - amount_r
                
                if amount < 0:
                    all_r = all_r + (amount + amount_r)
                    print("{0}月: 返済額{1}円 これで完済。返済総額{2}円".format(i,amount + amount_r,all_r))
                
                else:
                    all_r = all_r + amount_r
                    print("{0}月: 返済額{1}円 残り{2}円".format(i,amount_r,amount))
            
                i += 1
        
        except ValueError:
            print("入力は数字のみとしてください")

loan = Loan()
loan.returnLoan()
