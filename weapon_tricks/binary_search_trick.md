## 套路
如果题目长成given(arr=[],k)，让你以某种方式(find the smallest)分割那个list以达到k的样子,
你需要利用二分搜索的优美性质：让你每次能只问一个问题快速缩小搜索空间。

## 模板
不要写成(l + h) // 2，防止加法的结果大于整型能够代表的范围。
```python
m = l + (h -l) // 2
```
自己有一个模型一直写 ``while l < h return l``，至于循环内部的``l = mid - 1还是mid + 1``
取一个三元素array根据题目判断。

## 典型例题
1. leetcode875(Koto eating bananas)

## 相关文献
https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems