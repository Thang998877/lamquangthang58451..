"""
Author: Lâm Quang Thắng
Date: 09/10/2021
Program:
 Viết chương trình nhập tệp văn bản. Chương trình sẽ in ra
các từ trong tệp theo thứ tự bảng chữ cái.

Solution:
    ....
"""
def unique_file(input_filename, output_filename):
    input_file = open(input_filename, 'r')
    file_contents = input_file.read()
    input_file.close()
    duplicates = []
    word_list = file_contents.split()
    file = open(output_filename, 'w')
    for word in word_list:
        if word not in duplicates:
            duplicates.append(word)
            file.write(str(word) + "\n")
    file.close()


unique_file('07.txt','02.txt')
for line in sorted(open('02.txt')):
    print(line, end='')
