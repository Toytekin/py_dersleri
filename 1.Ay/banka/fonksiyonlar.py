kisiler={'İbrahim':1453, 'Ahmet':1253}

def isimKontrol(a):
        for i in kisiler.keys():
                if i==a:
                        return True
                else:
                        return False
       
       
def sifreKontrol(b):
        for i in kisiler.values():
                if i==int(b):
                        return True
                else:
                        return False                


