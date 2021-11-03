"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
 So sánh hai phương pháp thang độ xám khác nhau.
Giải pháp:
    ....
"""
from images import Image


def grayscale1(image):
    """Chuyển đổi hình ảnh sang thang độ xám bằng cách sử dụng
     những biến đổi chính xác về mặt tâm lý."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


def grayscale2(image):
    """Chuyển đổi hình ảnh sang thang độ xám bằng cách sử dụng mức trung bình thô
     trong số r, g và b"""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            ave = (r + g + b) // 3
            image.setPixel(x, y, (ave, ave, ave))


if __name__ == '__main__':
    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    grayscale2(image)
    image.draw()

