class Bar:
    def barLength(self):
        
        try:
        
            maxint = int(input("バーの長さを入力してください"))
        
            i = 0
            bar = "" #この定義の仕方しかない？
            
            if maxint != 0:
                while i < maxint:
                    bar = bar + "■"
                    i += 1
        
            print(bar)

        except ValueError:
            print("入力は整数のみです")

bar = Bar()
bar.barLength()

    