"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
  Xác định và kiểm tra một chức năng để hậu kỳ hình ảnh.
Giải pháp:
    ....
"""

from images import Image


def posterize(image, color=(0, 0, 0)):
    """Chuyển đổi hình ảnh màu thành hai màu,
     một trong số đó màu trắng và một trong số đó là
     mặc định là màu đen hoặc do người dùng chỉ định
     Giá trị RGB."""
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, color)
            else:
                image.setPixel(x, y, whitePixel)


def main():
    filename = input("Nhập tên tệp hình ảnh: ")
    red = int(input("Nhập một số nguyên [0..255] cho màu đỏ: "))
    green = int(input("Nhập một số nguyên [0..255] cho màu xanh lục: "))
    blue = int(input("Nhập một số nguyên [0..255] cho màu xanh lam: "))
    image = Image(filename)
    posterize(image, (red, green, blue))
    image.draw()


main()