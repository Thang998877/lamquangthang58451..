"""
Tác giả: Lâm Quang Thắng
Ngày: 17/10/2021
Vấn đề:
 Xác định một hàm biến đổi đại diện cho một tổng thể
mẫu để duyệt qua một hình ảnh và sửa đổi các pixel của nó.

 Kiểm tra chức năng này bằng cách sử dụng nó để xác định thang độ xám và
chức năng đen trắng.
Giải pháp:
    ....
"""
from images import Image


def transform(image, function):
    """Duyệt qua hình ảnh và đặt lại từng pixel với kết quả
     của việc áp dụng chức năng cho nó."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            image.setPixel(x, y, function(image.getPixel(x, y)))


def grayscale(image):
    """Chuyển đổi hình ảnh sang thang độ xám bằng cách sử dụng
     những biến đổi chính xác về mặt tâm lý."""

    def change(triple):
        """Chuyển đổi một pixel thành thang độ xám."""
        (r, g, b) = triple
        r = int(r * 0.299)
        g = int(g * 0.587)
        b = int(b * 0.114)
        lum = r + g + b
        return (lum, lum, lum)

    transform(image, change)


def blackAndWhite(image):
    """Chuyển đổi hình ảnh sang màu đen và trắng."""

    def change(triple):
        """Chuyển đổi một pixel thành màu đen và trắng."""
        (r, g, b) = triple
        average = (r + g + b) // 3
        if average < 128:
            return (0, 0, 0)
        else:
            return (255, 255, 255)

    transform(image, change)


if __name__ == '__main__':
    filename = input("Nhập tên tệp hình ảnh: ")
    image = Image(filename)
    grayscale(image)
    # blackAndWhite(image)
    image.draw()