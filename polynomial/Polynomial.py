class Polynomial:

    def __init__(self, params):
        if not isinstance(params, (list, tuple, Polynomial)):
            raise TypeError()
        if isinstance(params, Polynomial):
            self.coeffs = params.coeffs.copy()
        else:
            if len(params) == 0:
                raise AttributeError()
            if not all(isinstance(coef, int) for coef in params):
                raise TypeError()
            params = self._remove_zeros(params)
            if isinstance(params, tuple):
                self.coeffs = list(params)
            else:
                self.coeffs = params

    def __add__(self, other):
        return self._add(other)

    def __radd__(self, other):
        return self._add(other)

    def __sub__(self, other):
        return self._add(-other)

    def __rsub__(self, other):
        return (-self)._add(other)

    def __mul__(self, other):
        return self._mul(other)

    def __rmul__(self, other):
        return self._mul(other)

    def __eq__(self, other):
        if not isinstance(other, Polynomial):
            raise TypeError()
        else:
            return self.coeffs == other.coeffs

    def __str__(self):
        return self._str()

    def __repr__(self):
        return "Polynomial(" + str(self.coeffs) + ")"

    def __neg__(self):
        self.coeffs = [-i for i in self.coeffs]
        return self

    def _add(self, other):
        if isinstance(other, int):
            self.coeffs[-1] = self.coeffs[-1] + other
        elif isinstance(other, Polynomial):
            if len(self.coeffs) > len(other.coeffs):
                big_pol = self.coeffs
                short_pol = other.coeffs
            else:
                big_pol = other.coeffs
                short_pol = self.coeffs
            range_size = min(len(self.coeffs), len(other.coeffs))
            for i in range(range_size):
                big_pol[-1-i] = big_pol[-1-i] + short_pol[-1-i]
            self.coeffs = self._remove_zeros(big_pol)
        else:
            raise TypeError()
        return self

    def _mul(self, other):
        if isinstance(other, int):
            result = [i * other for i in self.coeffs]
        elif isinstance(other, Polynomial):
            self_len = len(self.coeffs)
            other_len = len(other.coeffs)
            result_len = self_len + other_len - 1
            result = [0]*result_len

            for i in range(self_len):
                for j in range(other_len):
                    index = - (self_len - i - 1) - (other_len - j - 1) - 1
                    result[index] = result[index] + self.coeffs[i] * other.coeffs[j]
        else:
            raise TypeError

        self.coeffs = self._remove_zeros(result)
        return self

    def _str(self):

        def _sym_to_str(coeffs, degree):
            index = -degree-1
            sym = str(abs(coeffs[index])) if (abs(coeffs[index]) != 1 or degree == 0) else ''
            if degree == 0:
                return sym
            elif degree == 1:
                return sym + "x"
            else:
                return sym + "x^" + str(degree)

        result = ""
        _len = len(self.coeffs)
        for i in range(_len):
            degree = _len - i - 1
            if i == 0:
                sign = '-' if self.coeffs[i] < 0 else ''
                result = sign + _sym_to_str(self.coeffs, degree)
            else:
                sign = '+' if self.coeffs[i] > 0 else '-'
                if self.coeffs[i] == 0:
                    continue
                result = result + ' ' + sign + ' ' + _sym_to_str(self.coeffs, degree)
        return result

    @staticmethod
    def _remove_zeros(coeffs):
        if not isinstance(coeffs, (list, tuple)):
            raise TypeError()
        i = 0
        while coeffs[i] == 0:
            if i == len(coeffs) - 1:
                break
            i += 1
        return coeffs[i:]