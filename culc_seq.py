class Culc_seq:
    
    def culc(self):
        
        num = []
        count = 0

        while True: 
        
            try:    
        
                i = int(input("データ入力（負の数で終了）"))
            
                if i < 0:
                    break
                
                num.append(i)
                count += 1
            
            except ValueError:
                print("入力は整数のみです")
                continue
        
        culcSum = sum(num)
        culcAvg = format(culcSum/count,'.1f')
        
        print("データ数: {0} 合計: {1} 平均: {2}".format(count,culcSum,culcAvg))
        


culc_seq = Culc_seq()
culc_seq.culc()
