from ORM.DBConnection import DB


class ModelMetaclass(type):
    def __new__(cls, name,bases,attrs):
        if name != 'Model':
            mappings = []
            for k ,v in attrs.items():
                if isinstance(v,Filed):
                    mappings.append(k)
            for k in mappings:
                attrs.pop(k)
            attrs["__mappings__"] = mappings
            attrs["__tableName__"] = name
        return type.__new__(cls,name,bases,attrs)

class Filed(object):
    def __init__(self,name):
        self.name = name

    @property
    def field_name(self):
        return self.name

class StringField(Filed):
    def __init__(self,name = None):
        super().__init__(name)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def returnDB(self):
        db = DB()
        return db.getCon()


    def save(self):
        mapping = self.__mappings__
        tableName = self.__tableName__
        column = ""
        values = ""
        for k in mapping:
            column += k+","
            values += "'"+getattr(self,k,None)+"',"
        column = column[:-1]
        values = values[:-1]
        sql = "insert into "+tableName+"(%s) values (%s)"%(column,values)
        print(sql)
        db = self.returnDB()
        cursor = db.cursor()
        cursor.fe
        try:
            cursor.execute(sql)
            db.commit()
            print("insert successfully")
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            db.close()



class Student(Model):
    sno = StringField()
    name = StringField()
    age = StringField()
    major = StringField()

    # def __init__(self,sno,name,age,major):
    #     self.sno = sno
    #     self.name = name
    #     self.age = age
    #     self.major = major


def main():
    s = Student(sno="3",name="wangyi",age="10",major="software")
    s.save()

if __name__ == '__main__':
    main()