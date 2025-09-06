#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
冒泡排序算法实现
Bubble Sort Algorithm Implementation

冒泡排序是一种简单的排序算法，它重复地遍历要排序的列表，
比较相邻的元素并交换它们的位置，直到列表排序完成。

时间复杂度：
- 最坏情况：O(n²)
- 最好情况：O(n) - 当数组已经排序时
- 平均情况：O(n²)

空间复杂度：O(1) - 原地排序
"""


def bubble_sort(arr):
    """
    冒泡排序算法实现
    
    Args:
        arr (list): 待排序的列表
        
    Returns:
        list: 排序后的列表
    """
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记本轮是否发生交换
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮后最大的元素会"冒泡"到正确位置
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序
        if not swapped:
            break
    
    return arr


def bubble_sort_descending(arr):
    """
    冒泡排序算法实现（降序）
    
    Args:
        arr (list): 待排序的列表
        
    Returns:
        list: 降序排序后的列表
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # 改变比较条件实现降序
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def print_array(arr, title="数组"):
    """打印数组"""
    print(f"{title}: {arr}")


def test_bubble_sort():
    """测试冒泡排序算法"""
    print("=" * 50)
    print("冒泡排序算法测试")
    print("=" * 50)
    
    # 测试用例1：普通数组
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    print_array(test_arr1, "原始数组")
    sorted_arr1 = bubble_sort(test_arr1.copy())
    print_array(sorted_arr1, "升序排序后")
    print()
    
    # 测试用例2：已排序数组
    test_arr2 = [1, 2, 3, 4, 5]
    print_array(test_arr2, "已排序数组")
    sorted_arr2 = bubble_sort(test_arr2.copy())
    print_array(sorted_arr2, "升序排序后")
    print()
    
    # 测试用例3：逆序数组
    test_arr3 = [5, 4, 3, 2, 1]
    print_array(test_arr3, "逆序数组")
    sorted_arr3 = bubble_sort(test_arr3.copy())
    print_array(sorted_arr3, "升序排序后")
    print()
    
    # 测试用例4：包含重复元素
    test_arr4 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print_array(test_arr4, "包含重复元素")
    sorted_arr4 = bubble_sort(test_arr4.copy())
    print_array(sorted_arr4, "升序排序后")
    print()
    
    # 测试降序排序
    test_arr5 = [64, 34, 25, 12, 22, 11, 90]
    print_array(test_arr5, "原始数组")
    desc_sorted = bubble_sort_descending(test_arr5.copy())
    print_array(desc_sorted, "降序排序后")
    print()
    
    # 测试空数组和单元素数组
    empty_arr = []
    single_arr = [42]
    
    print_array(empty_arr, "空数组")
    print_array(bubble_sort(empty_arr.copy()), "排序后")
    print()
    
    print_array(single_arr, "单元素数组")
    print_array(bubble_sort(single_arr.copy()), "排序后")


def interactive_mode():
    """交互模式：让用户输入数组进行排序"""
    print("\n" + "=" * 50)
    print("交互模式 - 冒泡排序")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\n请输入要排序的数字（用空格分隔，输入 'quit' 退出）: ")
            
            if user_input.lower() == 'quit':
                print("退出程序。")
                break
            
            # 解析用户输入
            numbers = [int(x) for x in user_input.split()]
            
            if not numbers:
                print("请输入至少一个数字！")
                continue
            
            print_array(numbers, "原始数组")
            
            # 升序排序
            ascending = bubble_sort(numbers.copy())
            print_array(ascending, "升序排序")
            
            # 降序排序
            descending = bubble_sort_descending(numbers.copy())
            print_array(descending, "降序排序")
            
        except ValueError:
            print("输入格式错误！请输入用空格分隔的数字。")
        except KeyboardInterrupt:
            print("\n程序被用户中断。")
            break


if __name__ == "__main__":
    # 运行测试
    test_bubble_sort()
    
    # 询问是否进入交互模式
    try:
        choice = input("\n是否进入交互模式？(y/n): ").lower()
        if choice in ['y', 'yes', '是']:
            interactive_mode()
    except KeyboardInterrupt:
        print("\n程序结束。")



