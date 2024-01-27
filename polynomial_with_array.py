class PolynomialTerm:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __str__(self):
        terms = []
        degree = len(self.coefficients) - 1
        for i in range(len(self.coefficients)):
            coef = self.coefficients[i]
            if coef != 0:
                term = f"{coef}x^{degree}"
                terms.append(term)
            degree -= 1
        return " + ".join(terms)

    def __add__(self, other):
        len_self = len(self.coefficients)
        len_other = len(other.coefficients)

        if len_self < len_other:
            self.coefficients = [0] * (len_other - len_self) + self.coefficients
        else:
            other.coefficients = [0] * (len_self - len_other) + other.coefficients

        result_coefficients = [self.coefficients[i] + other.coefficients[i] for i in range(len(self.coefficients))]

        result_polynomial = PolynomialTerm(result_coefficients)
        return result_polynomial


class PolynomialArray:
    def __init__(self):
        self.polynomials = []

    def add_polynomial(self, coefficients):
        polynomial = PolynomialTerm(coefficients)
        self.polynomials.append(polynomial)

    def print_polynomials(self):
        for i in range(len(self.polynomials)):
            print(f"Polynomial Eq {i + 1}: {self.polynomials[i]}")

    def add_all_polynomials(self):
        result = PolynomialTerm([0])  # Initialize with zero polynomial
        for polynomial in self.polynomials:
            result += polynomial
        return result


def main():
    poly_array = PolynomialArray()
    poly_array.add_polynomial([1, 2, 3, 0, 0, 5])
    poly_array.add_polynomial([2, -1, 0, 4, 0, 0, 1])
    poly_array.add_polynomial([0, 0, 0, 1, 0, 0, 0, 1])
    poly_array.add_polynomial([1, 1, 0, 0, 0, 0, 0, 0, 1])
    poly_array.add_polynomial([4, 0, 2, -1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1])
    poly_array.print_polynomials()
    result = poly_array.add_all_polynomials()
    print(f"\nADDITION OF ALL POLYNOMIAL Eqs : {result}")
main()
