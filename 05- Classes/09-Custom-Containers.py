# // container types like : Dit, List, Array and so on ..
# Let's implement our own


class TagCloud:
    def __init__(self):
        self.tags = {}
        self.total = 0
    def add(self, tag, number=1):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + number
        self.total = self.total + number
    def __len__(self):
        return len(self.tags)

    def __getitem__(self, tag) :
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self,tag,count): 
        self.tags[tag.lower()] = count

    def __iter__ (self) :
        return iter(self.tags)
    
    def getTotal(self):
        return self.total

cloud = TagCloud()
# len(cloud)
print('=========== ::::::::::::::::::::: ============')
print('=========== ::::TAG CLOUD ::::: ============')
print( 'len' , len(cloud) )

# cloud["python"] = 10
cloud.add('js', 1)
cloud.add('python', 10)
cloud.add('Python', 1)
print('NEW len' , len(cloud) , ' (number of tags):')
print('number on all tags: ',cloud.getTotal())
print('===== the tags: ============')
print(cloud.tags )

# // USING GET AND SET ITEM MAGIC METHODS 
print('===== get and set item: ============')
cloud['js'] = 5
print(cloud['js'])

print('===== iteration : ============')
for tag in cloud :
    print (tag)
