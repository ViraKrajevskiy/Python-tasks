class Title():
    def __get__(self,instance,name):
        if instance is None:
            return self
        print("user ",isinstance)
        print("name",isinstance.__dict__)
        print("user",name)
        return instance.__dict__.get('Name',None)

    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise ValueError("Email is string")
        if len(value)> 100:
            raise ValueError("Not longest email 100 words")

    def __delete__(self, instance):
        raise ValueError("Email is not deleted")

