"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
Xác định và kiểm tra một chức năng để chuyển đổi hình ảnh sang màu nâu đỏ.
Giải pháp:
    ....
"""
from images import Image


def sepia(image):
    """Chuyển đổi hình ảnh sang màu nâu đỏ."""
    grayscale(image)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            if r < 63:
                r = int(r * 1.1)
                b = int(b * 0.9)
            elif r < 192:
                r = int(r * 1.15)
                b = int(b * 0.85)
            else:
                r = min(int(r * 1.08), 255)
                b = int(b * 0.93)
            image.setPixel(x, y, (r, g, b))


def grayscale(image):
    """Chuyển đổi hình ảnh sang thang độ xám."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))


if __name__ == '__main__':

    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    sepia(image)
    image.draw()
