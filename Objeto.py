import csv

class Objeto:
    discount_porcentage = .9
    instaces = []
    def __init__(self, name: str, price: float, quantity=0):
        #Arguments validations
        assert price >= 0,"Price must be equal or greater than 0"
        assert quantity >= 0, "Quantity must be equal or greater than 0"

        #Arguments asiggnment
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Extra actions 
        Objeto.instaces.append(self)

    @property
    def price(self):
        return self.__price
    
    def discount(self):
        self.__price = self.__price * self.discount_porcentage

    def increment_price(self,increment):
        self.__price = round(self.__price + self.__price * increment)

    @price.setter
    def price(self,value):
        self.__price = value
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if len(value) >= 5: 
            self.__name = value
        else:
            raise Exception("Given name attribute is too short")

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('objetos.csv','r') as f:
            reader = csv.DictReader(f)
            objetos = list(reader)
        for objeto in objetos:
            Objeto(
                name= objeto.get('name'),
                price= round(float(objeto.get('price'))),
                quantity= round(float(objeto.get('quantity')))
            )
    
    @staticmethod#Basically normal subroutines
    def is_integer(num):
        #Eliminates the floats that end in .0
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}(name= '{self.name}', price= '{self.__price}', quantity= '{self.quantity}')"
    
    def _connect(self, smpt_server):
        pass

    def _prepare_body(self,text):
        return f"""
        hello bitches
        We are luserinos
        {self.name} {self.quantity}
        """

    def send_email(self):
        self.__connect()
        self.__prepare_body()

