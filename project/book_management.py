
from datetime import datetime
books=[]

class Book():
    def __init__(self,book_name=""):
        self.id =0
        self.book_name=book_name
        self.created_at =datetime.today().today()
    def __str__(self):
        return self.book_name

    def save(self):
        if books:
            id =books[-1].id+1
        else:
            id =1
        self.id=id
        books.append(self)

    def all(self):
        return books

    def values(self):
        records=[]
        for i in books:
               records.append({'id':i.id,'book_name':i.book_name,'created_at':i.created_at})
        return records

    def getBook(self,id):
        for i in books:
            if i.id==id:
                return {'id':i.id,'book_name':i.book_name,'created_at':i.created_at}
        else:
            return {}

    def updateBook(self,id,book_name):
        for b in books:
            if b.id==id:
                b.book_name=book_name








b =Book("Jungle Book")
b.save()

b =Book("Rich dada poor dad")
b.save()

data =b.getBook(0)
# print(data)
# print(b.all())
# print(b.values())
b.updateBook(1,"Neetu Book")

print(b.values())




# data=[{'id':1,'name':"Ajay"}]
# for r in data:
#     if r['id']==1:
#         r['name']="neetu"
#     else:
#         print("No Id Found")


# print(data)