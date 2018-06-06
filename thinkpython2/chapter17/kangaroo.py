class Kangaroo:
    def __init__(self):
        self.pounch_contents = []

    def put_in_pounch(self,list):
        self.pounch_contents = list
        return self

    def __str__(self):
        for i in self.pounch_contents:
            print(i)
k = Kangaroo()
list = [1,2,3,4]
print(k.put_in_pounch(list))