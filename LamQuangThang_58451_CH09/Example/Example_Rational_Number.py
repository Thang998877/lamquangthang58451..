"""
Tác giả: Lâm Quang Thắng
lop: CA20B1
Vấn đề
  Tài nguyên để thao tác với số hữu tỉ.
Giải pháp:

    ....
"""


class Rational(object):
     """Biểu diễn một số hữu tỉ."""

     def __init__(self, numer, denom) :
         """Hàm tạo tạo một số với giá trị đã cho tử số và mẫu số và giảm nó xuống các số hạng thấp nhất."""
         self._numer = numer
         self._denom = denom
         self._reduce()

     def numerator(self):
         """Trả về tử số."""
         return self._numer

     def denominator(self):
         """Trả về mẫu số."""
         return self._denom

     def __str__(self):
          """Trả về biểu diễn chuỗi của số."""
          return str(self._numer) + "/" + str(self._denom)

     def _reduce(self):
          """Người trợ giúp để giảm số lượng xuống các điều khoản thấp nhất."""
          divisor = self._gcd(self._numer, self._denom)
          self._numer = self._numer // divisor
          self._denom = self._denom // divisor

     def _gcd(self, a, b):
          """ thuật toán uclid cho ước số chung lớn nhất (phiên bản của hacker)."""
          (a, b) = (max(a, b), min(a, b))
          while b > 0:
           (a, b) = (b, a % b)
          return a

     def __add__(self, other):
      """Trả về tổng các số. self là toán hạng bên trái và khác là toán hạng bên phải."""
      print("DEBUG: call __add__")
      newNumer = self._numer * other._denom + \
                 other._numer * self._denom
      newDenom = self._denom * other._denom
      return Rational(newNumer, newDenom)

     def __lt__(self, other):
      """So sánh hai số hữu tỉ, tự và khác, sử dụng dấu <."""
      print("DUBUG: call __lt__")
      extremes = self._numer * other._denom
      means = other._numer * self._denom
      return extremes < means

     def __eq__(self, other):
      """Kiểm tra bản thân và kiểm tra sự bình đẳng khác."""
      print("DUBUG: call __eq__")
      if self is other:
         return True
      elif type(self) != type(other):
         return False
      else:
         return self._numer == other._numer and \
                self._denom == other._denom

if __name__ == '__name__':
    oneHalf = Rational(1, 2)
    twoSixth = Rational(2, 6)
    print(f"oneHalf: {oneHalf}")
    print(f"twoSixth: {twoSixth}")

    print(oneHalf + twoSixth)

    print(f"oneHalf == twoSixth: {oneHalf == twoSixth}")
    print(f"oneHalf < twoSixth: {oneHalf < twoSixth}")
