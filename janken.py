import random

janken_data = ["グー","チョキ","パー"]

class Janken:
  
     def janken(self):

        try:

            kekka = 0

            print(kekka)

            while kekka == 0:
                myJanken = int(input("あなたは？（0:グー、1:チョキ、2:パー）"))

                comp = random.randint(0,2)

                
                if myJanken == 0:
                    if comp == 0:
                        print("わたしはグー、あなたもグー。あいこです。もう一度！")
                        kekka = 0
                    elif comp == 1:
                        print("わたしはチョキ、あなたはグー。あなたの勝ちです。")
                        kekka = 1
                    elif comp == 2:
                        print("わたしはパー、あなたはグー。あなたの負けです。")
                        kekka = 1
                    
                elif myJanken == 1:
                    if comp == 0:
                       print("私はグー、あなたはチョキ。あなたの負けです。")
                       kekka = 1
                    elif comp == 1:
                        print("わたしはチョキ、あなたもチョキ。あいこです。もう一度！")
                        kekka = 0
                    elif comp == 2:
                        print("わたしはパー、あなたはチョキ。あなたの勝ちです。")
                        kekka = 1

                elif myJanken == 2:
                    if comp == 0:
                        print("私はグー、あなたはパー。あなたの勝ちです。")
                        kekka = 1
                    elif comp == 1:
                        print("わたしはチョキ、あなたはパー。あなたの負けです。")
                        kekka = 1
                    elif comp == 2:
                        print("わたしはパー、あなたもパー。あいこです。もう一度！")
                        kekka = 0
                else:
                    print("0から2の範囲で入力してください")
    
        except ValueError:
            print("数字で入力してください")


janken = Janken()

janken.janken()
