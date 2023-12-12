class obj(object):
    def __init__(self,d):
        for x,y in d.items():
            setattr(self,x,obj(y) if isinstance(y,dict) else y)
            

data={'a':5,'b':'2'}
obj = obj(data)
