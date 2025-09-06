#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速排序算法实现
Quick Sort Algorithm Implementation (非冒泡排序)

快速排序通过分治的思想选择一个枢轴（pivot），
将数组分成比枢轴小与比枢轴大的两部分，然后递归地排序这两部分。

时间复杂度：
- 最坏情况：O(n²)
- 平均/期望：O(n log n)

空间复杂度：
- 平均：O(log n)（递归栈）
"""

import random
from typing import List, TypeVar, Callable, Optional

T = TypeVar("T")


def quick_sort(values: List[T], 
               key: Callable[[T], T] = lambda x: x, 
               reverse: bool = False,
               randomize: bool = True) -> List[T]:
    """
    使用快速排序返回排序后的新列表（不修改原列表）。

    Args:
        values: 待排序的列表
        key: 提供比较键的函数，默认直接比较元素本身
        reverse: 是否降序排序，默认False（升序）
        randomize: 是否随机选择pivot以避免最坏情况，默认True

    Returns:
        新的排序列表
    """
    if len(values) <= 1:
        return values.copy()

    # 随机选择pivot或使用中位数，避免最坏情况
    if randomize:
        pivot_idx = random.randint(0, len(values) - 1)
    else:
        pivot_idx = len(values) // 2
    
    pivot = values[pivot_idx]
    pivot_key = key(pivot)

    # 预计算所有元素的key，避免重复计算
    keyed_values = [(key(v), v) for v in values]
    
    less = [v for k, v in keyed_values if k < pivot_key]
    equal = [v for k, v in keyed_values if k == pivot_key]
    greater = [v for k, v in keyed_values if k > pivot_key]

    if reverse:
        return quick_sort(greater, key, reverse, randomize) + equal + quick_sort(less, key, reverse, randomize)
    else:
        return quick_sort(less, key, reverse, randomize) + equal + quick_sort(greater, key, reverse, randomize)


def quick_sort_inplace(values: List[T], 
                      start: int = 0, 
                      end: Optional[int] = None,
                      key: Callable[[T], T] = lambda x: x,
                      reverse: bool = False) -> None:
    """
    原地快速排序（修改原列表，节省内存）。
    
    Args:
        values: 待排序的列表
        start: 开始索引
        end: 结束索引（不包含），None表示到列表末尾
        key: 比较键函数
        reverse: 是否降序
    """
    if end is None:
        end = len(values)
    
    if start < end - 1:
        pivot_idx = _partition(values, start, end, key, reverse)
        quick_sort_inplace(values, start, pivot_idx, key, reverse)
        quick_sort_inplace(values, pivot_idx + 1, end, key, reverse)


def _partition(values: List[T], start: int, end: int, 
               key: Callable[[T], T], reverse: bool) -> int:
    """分区函数，返回pivot的最终位置"""
    # 随机选择pivot并移到末尾
    pivot_idx = random.randint(start, end - 1)
    values[pivot_idx], values[end - 1] = values[end - 1], values[pivot_idx]
    
    pivot_key = key(values[end - 1])
    i = start
    
    for j in range(start, end - 1):
        if (key(values[j]) <= pivot_key) != reverse:
            values[i], values[j] = values[j], values[i]
            i += 1
    
    values[i], values[end - 1] = values[end - 1], values[i]
    return i


# 保持向后兼容的简化函数
def quick_sort_descending(values: List[T], key: Callable[[T], T] = lambda x: x) -> List[T]:
    """降序快速排序（向后兼容）"""
    return quick_sort(values, key, reverse=True)


def print_array(arr, title="数组"):
    print(f"{title}: {arr}")


def test_quick_sort():
    print("=" * 60)
    print("优化后的快速排序算法测试（非冒泡）")
    print("=" * 60)

    test_data = [64, 34, 25, 12, 22, 11, 90]
    
    print_array(test_data, "原始数组")
    
    # 测试新的统一函数
    print("\n--- 使用统一函数 quick_sort ---")
    asc = quick_sort(test_data, reverse=False)
    desc = quick_sort(test_data, reverse=True)
    print_array(asc, "升序（reverse=False）")
    print_array(desc, "降序（reverse=True）")
    
    # 测试原地排序
    print("\n--- 测试原地排序 quick_sort_inplace ---")
    test_copy1 = test_data.copy()
    test_copy2 = test_data.copy()
    
    print_array(test_copy1, "原地排序前")
    quick_sort_inplace(test_copy1)
    print_array(test_copy1, "原地升序后")

    quick_sort_inplace(test_copy2, reverse=True)
    print_array(test_copy2, "原地降序后")
    
    # 测试key函数
    print("\n--- 测试key函数（按绝对值排序）---")
    mixed_data = [-3, 5, -1, 4, -2]
    print_array(mixed_data, "原始数组")
    abs_sorted = quick_sort(mixed_data, key=abs)
    print_array(abs_sorted, "按绝对值升序")
    
    # 性能对比测试
    print("\n--- 边界情况测试 ---")
    edge_cases = [
        ("空数组", []),
        ("单元素", [42]),
        ("重复元素", [5, 5, 5, 5]),
        ("已排序", [1, 2, 3, 4, 5])
    ]
    
    for name, data in edge_cases:
        result = quick_sort(data)
        print(f"{name}: {data} → {result}")
    
    print("\n✅ 所有测试完成！")


if __name__ == "__main__":
    test_quick_sort()


