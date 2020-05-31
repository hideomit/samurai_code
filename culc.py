class Keisan:
    def culc(self,a,b):
        print(str(a) + "+" + str(b)  + "=" + str(a+b) )
        print(str(a) + "-" + str(b)  + "=" + str(a-b) )
        print(str(a) + "*" + str(b)  + "=" + str(a*b) )
        print(str(a) + "÷" + str(b)  + "=" + str(a//b) + "余り" + str(a%b))
        print(str(a) + "÷" + str(b)  + "=" + str(a/b) )

keisan = Keisan()
keisan.culc(5,2)