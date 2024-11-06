
class TitleDiscriptor:
    def __get__(self,instance,owner):
        if instance is None:
            return self
        print("==",instance)
        print("==",instance.__dict__)
        print("sdeer",owner)
        return instance.__dict__.get('name',None)

    # def __set__(self, instance, value):
    #     for i in range(len()):
    #         if i < 3:


# когда даеться значение 1 буква будет большой буквой и пусть в нем не будет ни одной цифры перед удалением пусть предуапреждает что класс удаляеться

# # Descriptor class
class NameDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        # print("================", instance)
        # print("================", instance.__dict__)
        # print("================", owner)
        return instance.__dict__.get('name', None)

    def __set__(self, instance, value):

        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        if len(value) < 3:
            print("salom")
            raise ValueError("Name must be at least 3 characters long!")

        instance.__dict__['name'] = value

    def __delete__(self, instance):
        raise AttributeError("Name attribute cannot be deleted!")

class EmailDescriptor:
    pass
#
# # Main class using the descriptor
class Person:
    name = NameDescriptor()  # Attach the descriptor to the `name` attribute

    def __init__(self, name):
        self.name = name  # Triggers the descriptor's __set__ method


person = Person("123")
person.name ="23"
print(person.name)

# # Example usage
# # try:
# #     person = Person("Al")  # Valid name
# #     print(person.name)  # Triggers the descriptor's __get__ method
# #
# #     person.name = "Bo"  # Invalid, raises ValueError
# # except ValueError as e:
# #     print(e)
#
# # try:
# #     del person.name  # Invalid, raises AttributeError
# # except AttributeError as e:
# #     print(e)
#
#
# # # Meta Programming Nimaga Kerak?
# # # Dynamic Code Generation
# # # Sinf va ob'ektlarni bajarilish vaqtida o‘zgartirish imkonini beradi.
# # # Masalan, ORM (Object-Relational Mapping) kabi vositalarda ma’lumotlar
# # # bazasi ustunlarini Python sinflariga moslashtirish uchun ishlatiladi.
# # #
# # # Avtomatlashtirish
# # # Ko‘p marta takrorlanadigan ishlarni kod ichida avtomatik bajarish imkonini beradi.
# # #
# # # Validatsiya va Nazorat
# # # Sinflarga kiritilayotgan o‘zgarishlarni cheklash yoki maxsus qoidalarni
# # # amalga oshirish uchun ishlatiladi.
# # #
# # # DSL (Domain-Specific Languages)
# # # Ma’lum sohalarga moslashtirilgan dasturlash interfeyslarini yaratish.
# #
# #
# # # Qachon Metaprogrammalashdan Foydalanish Mumkin?
# # #
# # # Murakkab tizimlar: Katta dasturiy ta’minotlar, masalan, web-frameworklar
# # # (Django’da metaclass va dekoratorlardan foydalaniladi).
# # # Avtomatik kod yozish: Kodning qayta-qayta yozilishini oldini olish.
# # # Cheklovlar yoki qoidalarni amalga oshirish: Sinf yoki atributlar ustidan nazorat.
# #
# #
# class Field:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name, None)
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# class ModelMeta(type):
#     def __new__(cls, name, bases, dct):
#         fields = {k: v for k, v in dct.items() if isinstance(v, Field)}
#         dct['_fields'] = fields
#         return super().__new__(cls, name, bases, dct)
#
#
# class Model(metaclass=ModelMeta):
#     def save(self):
#         print(f"Saving: {', '.join(f'{k}={v}' for k, v in self._fields.items())}")
#
#
# class User(Model):
#     username = Field("username")
#     email = Field("email")
# user ={
#     "username":"dsjhfsidufh",
#     "eamil":"sdjfosidh"
# }
#
# # Foydalanish
# user = User()
# user.username = "johndoe"
# user.email = "johndoe@example.com"
# user.save()
# #
# # # Xulosa: Python’da metaprogrammalash dasturlarni dinamik boshqarish,
# # # kengaytirish va avtomatlashtirish imkoniyatlarini taqdim etadi.
# # # Lekin murakkabligi sababli uni ehtiyotkorlik bilan qo‘llash kerak
# #
# #
# # # Python Exceptions: Nima va Qanday Ishlaydi?
# #
# # # Exceptions - bu dastur ishlayotgan paytda yuzaga keladigan xatolarni
# # # boshqarish uchun Python’da ishlatiladigan mexanizm. Exceptions koddagi
# # # odatiy oqimni buzadi va xatolikni qayd etib, uni hal qilish imkonini beradi.
# # # Masalan, nolga bo‘lish yoki faylni ochishda xato bo‘lsa, exception ishlatiladi.
# #
# # # Exception’ning Asosiy Tuzilishi
