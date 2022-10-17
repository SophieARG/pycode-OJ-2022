# -*- coding: utf-8 -*-
from functools import singledispatchmethod
from collections.abc import Iterable, Generator

class LayerDict:
    def __init__(self, n: int) -> None:
        self.root = dict()
        self.n = n
        self.dicts = [dict() for i in range(n)]

    @singledispatchmethod
    def __setitem__(self, key: tuple, value: object) -> None:
        if key not in self.root:
            keylst = list(key)
            for _key, _dict in zip(key, self.dicts):
                _dict[_key] = keylst
        self.root[key] = value

    @__setitem__.register(slice)
    def _(self, keyslc: slice, value: object) -> None:
        keylst = self.dicts[keyslc.start][keyslc.stop]
        key = tuple(keylst)
        if keyslc.step is None:
            self.root[key] = value
        else:
            if isinstance(keyslc.step, int):
                zips = [(keyslc.step, value)]
            else:
                zips = zip(keyslc.step, value)
            for s, v in zips:
                del self.dicts[s][keylst[s]]
                keylst[s] = v
            for s, v in zips:
                self.dicts[s][v] = keylst
            value = self.root[key]
            del self.root[key]
            self.root[tuple(keylst)] = value

    @singledispatchmethod
    def __getitem__(self, key: tuple) -> object:
        return self.root[key]

    @__getitem__.register(slice)
    def _(self, keyslc: slice) -> object:
        keylst = self.dicts[keyslc.start][keyslc.stop]
        if keyslc.step is None:
            return self.root[tuple(keylst)]
        if isinstance(keyslc.step, int):
            return ketlst[keyslc.step]
        return tuple(keylst[s] for s in keyslc.step)
        
    @singledispatchmethod
    def __delitem__(self, key: tuple) -> None:
        for _key, _dict in zip(key, self.dicts):
            del _dict[_key]
        del self.root[key]

    @__delitem__.register(slice)
    def _(self, keyslc: slice) -> None:
        del self[tuple(self.dicts[keyslc.start][keyslc.stop])]      

    def __contains__(self, key: tuple) -> bool:
        return key in self.root
    
    def __len__(self) -> int:
        return len(self.root)
    
    def __clear__(self) -> None:
        self.__init__(self.n)
    
    def dict(self, index: int) -> dict:
        return {_key: self.root[tuple(keylst)] for _key, keylst in self.dicts[index].items()}

    def __repr__(self) -> str:
        return repr(self.root)

    def keys(self, index=None) -> Generator:
        if index is None:
            return (key for key in self.root)
        return (_key for _key in self.dicts[index])

    def values(self) -> Generator:
        return (value for value in self.root.values())

    def items(self, index=None) -> Generator:
        if index is None:
            return (item for item in self.root.items())
        return ((_key, self.root[tuple(keylst)]) for _key, keylst in self.dicts[index].items())

class LayerSet:
    def __init__(self, n: int) -> None:
        self.root = set()
        self.n = n
        self.dicts = [dict() for i in range(n)]

    def add(self, key: tuple) -> None:
        if key not in self.root:
            self.root.add(key)
            keylst = list(key)
            for _key, _dict in zip(key, self.dicts):
                _dict[_key] = keylst

    def remove(self, key: tuple) -> None:
        for _key, _dict in zip(key, self.dicts):
            del _dict[_key]
        self.root.remove(key)

    def setkey(self, i, key, js, values) -> None:
        keylst = self.dicts[i][key]
        key = tuple(keylst)
        if isinstance(js, int):
            zips = [(js, values)]
        else:
            zips = zip(js, values)
        for j, value in zips:
            del self.dicts[j][keylst[j]]
            keylst[j] = value
        for j, value in zips:
            self.dicts[j][value] = keylst
        self.root.remove(key)
        self.root.add(tuple(keylst))
        
    def getkey(self, i, key, js=None) -> object:
        keylst = self.dicts[i][key]
        if js is None:
            return tuple(keylst)
        if isinstance(js, int):
            return keylst[js]
        return tuple(keylst[j] for j in js)

    def __contains__(self, key: tuple) -> bool:
        return key in self.root
    
    def __len__(self) -> int:
        return len(self.root)
    
    def __clear__(self) -> None:
        self.__init__(self.n)
    
    def set(self, index: int) -> set:
        return {_key for _key in self.dicts[index]}

    def __repr__(self) -> str:
        return repr(self.root)
