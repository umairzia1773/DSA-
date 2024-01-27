class Node:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None

class PolynomialLinkedList:
    def __init__(self):
        self.head = None

    def add_term(self, coef, exp):
        new_node = Node(coef, exp)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        terms = []
        while current:
            terms.append(f"{current.coef}x^{current.exp}")
            current = current.next
        print(" + ".join(terms))

def add_polynomials(poly1, poly2):
    result = PolynomialLinkedList()
    current1, current2 = poly1.head, poly2.head

    while current1 or current2:
        coef1, exp1 = current1.coef if current1 else 0, current1.exp if current1 else 0
        coef2, exp2 = current2.coef if current2 else 0, current2.exp if current2 else 0

        if exp1 == exp2:
            result.add_term(coef1 + coef2, exp1)
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None
        elif exp1 > exp2:
            result.add_term(coef1, exp1)
            current1 = current1.next
        else:
            result.add_term(coef2, exp2)
            current2 = current2.next

    return result

def main():
    poly_list1 = PolynomialLinkedList()
    poly_list1.add_term(2, 50)
    poly_list1.add_term(3, 75)
    poly_list1.add_term(5, 10)
    poly_list1.add_term(-1, 0)

    poly_list2 = PolynomialLinkedList()
    poly_list2.add_term(3, 10)
    poly_list2.add_term(2, 5)
    poly_list2.add_term(3, 0)

    poly_list3 = PolynomialLinkedList()
    poly_list3.add_term(4, 80)
    poly_list3.add_term(5, 70)
    poly_list3.add_term(6, 10)
    poly_list3.add_term(9, 0)

    poly_list4 = PolynomialLinkedList()
    poly_list4.add_term(10, 100)
    poly_list4.add_term(9, 50)
    poly_list4.add_term(2, 0)

    poly_list5 = PolynomialLinkedList()
    poly_list5.add_term(17, 200)
    poly_list5.add_term(16, 100)
    poly_list5.add_term(41, 78)
    poly_list5.add_term(9, 37)
    poly_list5.add_term(8, 10)
    poly_list5.add_term(2, 0)

    print("Polynomial 1:")
    poly_list1.display()
    print("\nPolynomial 2:")
    poly_list2.display()
    print("\nPolynomial 3:")
    poly_list3.display()
    print("\nPolynomial 4:")
    poly_list4.display()
    print("\nPolynomial 5:")
    poly_list5.display()

    result_poly_all = add_polynomials(add_polynomials(add_polynomials(add_polynomials(poly_list1, poly_list2), poly_list3), poly_list4), poly_list5)
    print("\nResult of adding all five polynomials:")
    result_poly_all.display()

if __name__ == "__main__":
    main()
