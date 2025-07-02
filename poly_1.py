class Books:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __sub__(self, other):
        return self.price - other.price

    def __mul__(self, other):
        return self.price * other.price

    def __truediv__(self, other):
        return self.price / other.price

    def __floordiv__(self, other):
        return self.price // other.price

    def __mod__(self, other):
        return self.price % other.price        #arithmatic operators finish here

    def __eq__(self, other):                   # comparison operators starts here        
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

   
    def __str__(self):
        return f"Books({self.name!r}, {self.price})"


b1 = Books("python", 100)
b2 = Books("java", 50)

print(b1)               
print(b2)               

print(b1 + b2)          
print(b1 - b2)          
print(b1 * b2)          
print(b1 / b2)          
print(b1 // b2)       
print(b1 % b2)          
print(b1 == b2)         
print(b1 != b2)        
print(b1 > b2)         
print(b1 < b2)         
print(b1 >= b2)        
print(b1 <= b2)   
  
 #---------------------------------------------------------------------------------------------------------------------------------
                                                #   METHOD OVERLOADING WITH FOUR OBJECTS METHOD
class books:
    def __init__(self,name,p):
            self.bookname = name
            self.price = p

    def __add__(self,other):
      return self.price + other.price 
    
    def __sub__(self,other):
      return self.price - other.price              

b1=books("core python",200)
b2=books("adv python",400)
b3=books("data science",600)
b4=books("data sci",600)

print( b1.price + b2.price + b3.price  + b4.price )
print( b1.price - b2.price - b3.price  - b4.price )

    