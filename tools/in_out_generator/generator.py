# -*- coding: utf-8 -*-

# 此文件实现自动化生成测试用例
# 需要满足的条件：1. 同目录下存在文件夹exam，测试用例将生成在其中
#              2. 同目录下存在文件example.py，且其中已经实现了正确的代码
# 在编写完此文件后，直接运行，并将exam文件夹下生成的.in和.out文件上传到OJ即可

import subprocess
execute = lambda x: subprocess.Popen(x, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

# 此函数在每次调用时，都应该按照某种规则返回一个测试输入列表
# 返回的列表的元素依次为输入的第一行...最后一行
# 函数接受的参数一般情况下是数据规模等等
def generate(n):
    return ['test in of cycle %d' % n]

for cycle in range(10):
    res = generate(cycle)
    inpath = 'exam/%d.in' % cycle
    with open(inpath, 'w') as f:
        f.write('\n'.join(res))
    out = execute("python3 %s < %s" % ('example.py', inpath))
    outpath = 'exam/%d.out' % cycle
    with open(outpath, 'w') as f:
        f.write(out.decode('utf-8'))
