class Score:
    
    def culc(self):
        eng = input("英語の成績を入力してください")
        math = input("算数の成績を入力してください")
        
        Sum = (int(eng) + int(math) )
        avg = Sum/2
        
        print("合計は{}です".format(Sum))
        print("平均点は{}です".format(avg))
        

score = Score()

score.culc()
