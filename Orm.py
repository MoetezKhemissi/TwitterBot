
import orm_sqlite  

class Account(orm_sqlite.Model):  

    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    Email = orm_sqlite.StringField()
    Password = orm_sqlite.StringField()
    username = orm_sqlite.StringField()


db = orm_sqlite.Database('UserInfo.db')
Account.objects.backend = db


