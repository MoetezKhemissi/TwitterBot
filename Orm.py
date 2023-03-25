
import orm_sqlite  

class Email(orm_sqlite.Model):  

    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    Email = orm_sqlite.StringField()
    Password = orm_sqlite.StringField()
    Gender = orm_sqlite.StringField()
    Birthdate = orm_sqlite.StringField()


db = orm_sqlite.Database('UserInfo.db')
Email.objects.backend = db


