import orm_sqlite 


def database_write_follower(follower):
    follower['checked_dmable']=0
    follower['dmable']=0
    pomodoro = Follower(follower)
    pomodoro.save()

def database_read_followers():
    return Follower.objects.all()

class Follower(orm_sqlite.Model):  

    id = orm_sqlite.IntegerField(primary_key=True) # auto-increment
    link = orm_sqlite.StringField()
    checked_dmable = orm_sqlite.IntegerField()
    dmable = orm_sqlite.IntegerField()


def delete_by_id(id):
    Follower.objects.get(pk=id).delete()
'''def update_email_by_id(id, dmable):
    obj = Follower.objects.get(pk=id)
    obj['Email'] = email
    obj.update()'''
follower_template = {"link": "https://twitter.com/elonmusk/status/1642026231766953985"}
db2 = orm_sqlite.Database('Follwer.db')
Follower.objects.backend = db2
'''
database_write_follower(follower_template)
print(database_read_followers())'''