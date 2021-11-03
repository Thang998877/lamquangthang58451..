"""
Tác giả: Lâm Quang Thắng
Ngày: 23/10/2021
Vấn đề:
  Danh sách được sắp xếp theo thứ tự tăng dần nếu nó trống hoặc từng mục ngoại trừ mục cuối cùng là
nhỏ hơn hoặc bằng người kế nhiệm của nó. Xác định một vị từ được Sắp xếp mong đợi một danh sách
dưới dạng một đối số và trả về True nếu danh sách được sắp xếp hoặc trả về False nếu không (Gợi ý: Đối với danh sách có độ dài 2 hoặc lớn hơn, hãy lặp lại danh sách và so sánh các cặp
các mục, từ trái sang phải và trả về Sai nếu mục đầu tiên trong một cặp lớn hơn.)

Giải pháp:
    ....
"""
def issorted(lyst):
    if len(lyst) == 0 or len(lyst) == 1:
        return True
    else:
        for index in range(len(lyst)-1):
            if lyst[index] > lyst[index + 1]:
                return False
    return True
def main():
    lyst=[]
    print(issorted(lyst))
    lyst=[1]
    print(issorted(lyst))
    lyst= list(range(10))
    print(issorted(lyst))
    lyst[9]=3
    print(issorted(lyst))

main()
