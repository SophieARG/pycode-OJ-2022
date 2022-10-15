# -*- coding: utf-8 -*-
import subprocess
execute = lambda x: subprocess.Popen(x, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()[0]

class BeatMatcher:
    @classmethod
    def check(cls, pypath, inpath):
        print('Checking ...\n\nInput From %s:' % inpath)
        with open(inpath, 'r') as f:
            print(''.join(f.readlines()))
        out = execute("python3 %s < %s" % (pypath, inpath))
        print('\nOutput From %s: \n%s\n' % (pypath, out.decode('utf-8').strip()))

    @classmethod
    def match(cls, testpy, refpy, inputs):
        print('Beat Matching ... ', end='') 
        for input_ in inputs:
            with open('sophie.in', 'w') as f:
                f.write(input_)
            refout = execute("python3 %s < sophie.in" % refpy)
            testout = execute("python3 %s < sophie.in" % testpy)
            if refout != testout:
                print('Error Found')
                with open('sophie.in', 'r') as f:
                    print('\nInput:')
                    print(''.join(f.readlines()))
                print('\nStd Output:')
                print(refout.decode('utf-8').strip())
                print('\nYour Output:')
                print(testout.decode('utf-8').strip())
                break
        else:
            print('Error Not Found\n')
        rmout = execute("rm sophie.in")
            
import random
def inputs():
    for n in range(1, 101):
        res = [str(n)]
        res.append(' '.join((str(random.randint(1, 100)) for i in range(n))))
        yield '\n'.join(res)

#BeatMatcher.check('test.py', 'in.txt')
#BeatMatcher.match('test.py', 'ref.py', inputs())

    
