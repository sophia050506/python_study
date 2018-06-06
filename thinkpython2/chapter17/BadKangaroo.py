class Kangaroo:

    def __init__(self, name, contents=None):
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        print("item:",item)
        self.pouch_contents.append(item)
        print("pouch_contents:",self.pouch_contents)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
