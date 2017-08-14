# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(100) #例如这里设置为一百
class Screen(object):
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self,value):
        self._weight=value

    @weight.getter
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height=value

    @height.getter
    def height(self):
        return self._height

    @property
    def resolution(self):
        return self._weight*self._height

s = Screen()
s.weight = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
