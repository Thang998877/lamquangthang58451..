"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Xác định và kiểm tra một chức năng để lọc màu. Sử dụng cái này
chức năng xác định các chức năng làm sáng và tối ảnh.
Giải pháp:
    ....
"""
from images import Image


def colorFilter(image, rgbTriple):
    """Thêm các giá trị rgb đã cho vào mỗi pixel sau khi chuẩn hóa."""

    def baseValue(value, offset):
        """Chuẩn hóa giá trị để 0 <= value <= 255."""
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)

    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = baseValue(r, rgbTriple[0])
            g = baseValue(g, rgbTriple[1])
            b = baseValue(b, rgbTriple[2])
            image.setPixel(x, y, (r, g, b))


def lighten(image, amount):
    """Làm sáng hình ảnh theo số lượng."""
    colorFilter(image, (amount, amount, amount))


def darken(image, amount):
    """Làm đậm hình ảnh theo số lượng."""
    colorFilter(image, (-amount, -amount, -amount))


def main():
    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    print("Đóng cửa sổ để xem các thay đổi đối với hình ảnh")
    image.draw()
    lighten(image, 20)
    # làm tối(image, 20)
    image.draw()


main()
