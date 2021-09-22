"""
使用场景：将两个已排序的数组，合并成一个排序数组
"""
def mergeSort(array1, array2):
    """
    归并排序
    :param array1: 已从小到大排序的数组1
    :param array2: 已从小到大排序的数组2
    :return: 合并后的数组，从小到大排序
    """
    # 数组1的长度
    length_array1 = len(array1)
    # 数组2的长度
    length_array2 = len(array2)
    # 合并后的数组长度
    length_array3 = length_array1 + length_array2
    # 合并后的数组长度=数组1的长度的话，就代表数组2为空，直接返回数组1
    if length_array3 == length_array1:
        return array1
    # 合并后的数组长度=数组2的长度的话，就代表数组1为空，直接返回数组2
    elif length_array3 == length_array2:
        return array2
    else:
        # 数组1和数组2合并的数组
        array3 = []
        # i指向数组1
        i = 0
        # j指向数组2
        j = 0
        while i < length_array1 and j < length_array2:
            # i指向数组1的值和j指向的数组2的值进行比较
            # i指向的值<=j指向的值，那么就把i指向的值尾添到数组3中，且i后移一位
            if array1[i] <= array2[j]:
                array3.append(array1[i])
                i += 1
            else:
                # i指向的值>j指向的值，那么就把j指向的值尾添到数组3中，且j后移一位
                array3.append(array2[j])
                j += 1
        # 当有数组比较完了，那么剩余没比完的就可以直接合并到数组3中
        # 这里根据i的值判断是那个先比完，i<数组1的长度，表示数组1没有比完，数组2先比完
        if i < length_array1:
            # 数组1未比完，那么就把数组1中剩余未比的元素合并到数组3中
            # 数组1中未比完的元素 = 此时i指向的值~数组1长度-1
            array3 += array1[i:length_array1]
        else:
            # 数组2未比完，那么就把数组2中剩余未比的元素合并到数组3中
            # 数组2中未比完的元素 = 此时j指向的值~数组2长度-1
            array3 += array2[j:length_array2]
        return array3


def test01():
    array1 = [1, 3, 4, 5, 9]
    array2 = [2, 3, 5, 6, 7, 8, 11, 13, 15]
    print("和并前:")
    print("\t数组1:{}".format(array1))
    print("\t数组2:{}".format(array2))
    print("合并后:")
    print("\t{}".format(mergeSort(array1, array2)))


if __name__ == "__main__":
    test01()
