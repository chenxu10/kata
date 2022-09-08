# Binary Search出错细节与变招
## 套路
如果题目长成given(arr=[],k)，让你以某种方式(find the smallest)分割那个list以达到k的样子,
你需要利用二分搜索的优美性质：让你每次能只问一个问题快速缩小搜索空间。

## 容易出错的细节
不要写成(l + h) // 2，防止加法的结果大于整型能够代表的范围。
```python
m = l + (h -l) // 2
```
自己有一个模型一直写 ``while l < h return l``，至于循环内部的``l = mid - 1还是mid + 1``
取一个三元素array根据题目判断。

脑海中有右边指针收紧还是左边指针收紧的心理图像。

## 变招
1. mid是取大取小了不是直接判断，而是需要通过一定计算与第二个参数比较。
    - leetcode875(Koto eating bananas)
https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems
2. 学会使用bisect现成库，三维数组存储信息，不记录所有只记录变化。
3. 与DFS或者BFS结合(DIJKSTRA算法)
    - leetcode1631