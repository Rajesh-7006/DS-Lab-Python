class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, power):
        new_node = Node(coeff, power)
       
        if not self.head or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next and temp.next.power > power:
                temp = temp.next
           
            if temp.next and temp.next.power == power:
                temp.next.coeff += coeff
            else:
                new_node.next = temp.next
                temp.next = new_node

    def display(self):
        terms = []
        temp = self.head
        while temp:
            if temp.coeff != 0:
                if temp.power == 0:
                    terms.append(f"{temp.coeff}")
                elif temp.power == 1:
                    terms.append(f"{temp.coeff}x")
                else:
                    terms.append(f"{temp.coeff}x^{temp.power}")
            temp = temp.next
        print(" + ".join(terms) if terms else "0")

    @staticmethod
    def add(poly1, poly2):
        p = poly1.head
        q = poly2.head
        result = Polynomial()

        while p and q:
            if p.power == q.power:
                coeff_sum = p.coeff + q.coeff
                if coeff_sum != 0:
                    result.insert_term(coeff_sum, p.power)
                p = p.next
                q = q.next
            elif p.power > q.power:
                result.insert_term(p.coeff, p.power)
                p = p.next
            else:
                result.insert_term(q.coeff, q.power)
                q = q.next

       
        while p:
            result.insert_term(p.coeff, p.power)
            p = p.next
        while q:
            result.insert_term(q.coeff, q.power)
            q = q.next

        return result



print("Enter first polynomial:")
poly1 = Polynomial()
n1 = int(input("Enter number of terms in polynomial 1: "))
for i in range(n1):
    coeff = int(input(f"Enter coefficient of term {i + 1}: "))
    power = int(input(f"Enter power of term {i + 1}: "))
    poly1.insert_term(coeff, power)

print("\nEnter second polynomial:")
poly2 = Polynomial()
n2 = int(input("Enter number of terms in polynomial 2: "))
for i in range(n2):
    coeff = int(input(f"Enter coefficient of term {i + 1}: "))
    power = int(input(f"Enter power of term {i + 1}: "))
    poly2.insert_term(coeff, power)

print("\nFirst Polynomial: ", end="")
poly1.display()
print("Second Polynomial: ", end="")
poly2.display()

result = Polynomial.add(poly1, poly2)
print("\nResultant Polynomial after addition: ", end="")
result.display()
