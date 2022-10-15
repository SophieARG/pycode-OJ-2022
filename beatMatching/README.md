# 对拍机
`beatMatching.py`提供了一个对拍机，实现了两个类方法：
1. `BeatMatcher.check` 样例检查方法。
* `pypath: str` 代码路径 
* `inpath: str` 样例输入路径
* 输出样例运行结果
2. `BeatMatcher.match` 对拍方法。
* `testpy: str` 测试代码路径 
* `refpy: str` 参考代码路径 
* `inputs: str iterable` 待测试的全部输入
* 输出对拍结果

## 一个例子
这里选用的例子是2ndHW的[毕业生年薪统计](http://phyic.openjudge.cn/2022b02/1/)。

相关测试文件`in.txt`输入样例、`ref.py`参考代码、`test.py`测试代码已经上传。

样例检查方法示例：
~~~
>>> BeatMatcher.check('test.py', 'in.txt')
Checking ...

Input From in.txt:
7
62 57 84 92 76 15 30

Output From test.py: 
6

>>> 
~~~

对拍方法示例：
~~~
>>> BeatMatcher.match('test.py', 'ref.py', inputs())
Beat Matching ... Error Not Found

>>> 
~~~
