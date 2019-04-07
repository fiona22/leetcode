def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    return _singleton

@Singleton
class Myclass(object):
    a = 1

c1 = Myclass()
c2 = Myclass()
print c1==c2
