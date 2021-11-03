"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
 Xác định và kiểm tra một chức năng để phóng to hình ảnh.
Giải pháp:
    ....
"""
from images import Image


def enlarge(image, factor):
    """Tạo và trả về bản sao của hình ảnh lớn hơn
     bởi các yếu tố."""
    oldWidth = image.getWidth()
    oldHeight = image.getHeight()
    new = Image(oldWidth * factor, oldHeight * factor)
    oldY = 0
    newY = 0
    while oldY < oldHeight:
        for countY in range(factor):
            oldLeft = 0
            oldRight = oldWidth - 1
            newLeft = 0
            newRight = new.getWidth() - 1
            while oldLeft < oldRight:
                leftPixel = image.getPixel(oldLeft, oldY)
                rightPixel = image.getPixel(oldRight, oldY)
                for count in range(factor):
                    new.setPixel(newLeft, newY, leftPixel)
                    new.setPixel(newRight, newY, rightPixel)
                    newLeft += 1
                    newRight -= 1
                oldLeft += 1
                oldRight -= 1
            newY += 1
        oldY += 1
    return new


if __name__ == '__main__':

    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    print("Đóng cửa sổ để xem các thay đổi đối với hình ảnh.")
    image.draw()
    newimage = enlarge(image, 2)
    newimage.draw()

