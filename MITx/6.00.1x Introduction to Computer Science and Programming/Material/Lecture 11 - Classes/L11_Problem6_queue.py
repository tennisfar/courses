class Queue(object):

    def __init__(self):
        self.q = []

    def insert(self, e):
        self.q.append(e)

    def remove(self):
        try:
            return self.q.pop(0)
        except:
            raise ValueError()


q1 = Queue()
q2 = Queue()
q1.insert(17)
q1.insert(18)
q1.insert(19)
q2.insert(20)
q1.remove()
q2.remove()
