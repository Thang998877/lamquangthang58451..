"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Xác định và kiểm tra chức năng đảo ngược hình ảnh.
Giải pháp:
    ....
"""
from images import Image


def invert(image):
    """Đảo một hình ảnh thành âm bản của nó."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            image.setPixel(x, y, (255 - r, 255 - g, 255 - b))


def blackAndWhite(image):
    """Chuyển đổi hình ảnh sang màu đen và trắng."""
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)


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
    filename = input("Nhập tên tệp hình ảnh:  ")
    image = Image(filename)
    grayscale(image)
    invert(image)
    image.draw()
