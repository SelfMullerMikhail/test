from functools import reduce
import random



class Clients_counter():
    def __init__(self):
        """Прошу прощения, я не совсем понял условие задач. 
        По этому я решил реализовать все возможные варианты при помощи различных методов класса
        Если ни одно решение не подходит, то я бы с радостью уточнил у вас условие и реализовал
        бы решение снова"""

# Создаем переменные
        self.groups = []
        self.lines = {}
        self.total_customers = 0

# Метод преобразует число в сумму цифр
    def transformation(self, customer): # O(n)
        self.numbers = [int(x) for x in str(customer)] # O(n)
        self.summ = reduce(lambda x,y: y + x, self.numbers) # O(n)
        self.if_else(self.summ) # O(1)

# Метод проверяет условие строки на наличие "0" в наале строки и
# Ведет счетчик клиентов
    def _clietns_counter(self, count): # O(n)
        if type(count) == str: # O(1)
            self.total_customers += int(count.replace("0", "")) # O(n)
        else:
            self.total_customers += count-1 # O(1)

# Метод распределяет счетчик клиентов по группам
    def if_else(self, summ):
        self.summ = summ # O(1)
        if self.summ not in list(self.lines): # O(n)
            self.lines[self.summ] = 1 # O(1)
            self.total_customers += 1 # O(1)
        else:
            self.counter = self.lines[self.summ] # O(1)
            self.lines[self.summ] = self.counter + 1 # O(1)
            self.total_customers += 1 # O(1)


# Метод переберает числа списка и передает их в калькулятор чисел
    def list_counter(self, customer): # O(n^2)
        for i in customer: # O(n)
            self.transformation(i) # O(n)
    

# Метод проверяет обьект на соответсвие критерий и в зависимости от результата
# Передает выполнение на нужную фунцкию, дейсвтие
    def customer_add(self, customer):

        # Елсти просто число, то +1 клиент и сортировка по категории
        if str(customer)[0] != "0" and len(str(customer)) >= 4: # O(1)
            self.transformation(customer) # O(n) - Но так как у точно известно, что 
                                         # все числа могут быть максимум до 7 цифр, так что скорее
                                         # всего ближе к O(1)

        # Если число меньше 5 (т.к. номера от 5 до 7 цифр), тогда + n клиентов
        elif len(str(customer)) <= 4: # O(1)
            self.total_customers += int(customer)-1 # O(1)

        # Если строка начинается с 0 (т.к. целое число "int "не может начинаться с 0),
        # передаем на обработку строки и +n клиентов
        else:
            self._clietns_counter(str(customer)) # O(n)

    # Для удобства просмотра состояния
    def __str__(self):
        return f"{self.lines}, total clients: {self.total_customers}".replace(", ", "\n")  # O(1)
    

# Мы конечно нигде не импортируем, что бы так делать. 
# Но мне кажется это правильным
if __name__ == "__main__":

    clients = []
    for i in range(100):
        clients.append(random.randint(10000, 10100))

# При худшем варианте, временная сложность O(n^2).
    test = Clients_counter()
    test.list_counter(clients)
    test.customer_add("00999")
    test.customer_add(999)
    test.customer_add(43214)
    print(test)
    """Да уж... Как то не очень читабельно вышло... Извините)"""

