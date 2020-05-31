class Sort:
    
    def sortnum(self):

        try:
            num = []
        
            num.append(int(input("3つの数を入力してください。1番目")))
            num.append(int(input("3つの数を入力してください。2番目")))
            num.append(int(input("3つの数を入力してください。3番目")))
        
            num.sort()
            print(num)

        except ValueError:
            print("入力できるのは整数のみです。整数を入力してください")

sort = Sort()

sort.sortnum()