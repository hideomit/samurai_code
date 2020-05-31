class Bmi:
    
    def culbmi(self):
        
        height = input("身長をm単位で入力してください")
        weight = input("体重をkg単位で入力してください")
    
        bmi = float(weight)/(float(height))**2
        
#        print(bmi)
        
        if bmi >= 30:
            print("あなたは高度肥満です")
        elif bmi >= 25 and bmi < 30:
            print("肥満です")
        elif bmi >= 18.5 and bmi < 25:
            print("標準です")
        else:
            print("やせてます")

bmi = Bmi()

bmi.culbmi()