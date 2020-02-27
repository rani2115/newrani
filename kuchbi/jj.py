
postlit=[]
class Post:
    def __init__(self):
        self.uname=''
        self.pwd=''
    def save(self):
        postlit.append(self)

print(postlit)
for i in range(5):
    p=Post()
    p.uname="Ram"
    p.pwd="12345"
    p.save()

print(postlit)
for v in postlit:
    print(v.uname)
    print(v.pwd)