import shelve
"""学习shelve序列化文件"""

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

def create_shelve_file():
    stu = Student('tom',10)
    db = shelve.open('shelve_create_file')
    db['s'] = stu
    db.close()

def read_shelve_file():
    db = shelve.open('shelve_create_file')
    st = db['s']
    print (st)
    print (st.name)
    print (st.age)
    db.close()

if __name__ == '__main__':
    read_shelve_file()