class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = list()
        self.loc = 0

    def append(self, item):
        # if list is at capacity replace the oldest file
        # add values in a stack
        
        # check if list is at capacity
        if len(self.list) >= self.capacity:

            # at capacity repace the oldest file

            self.list.pop(self.loc)

            self.list.insert(self.loc,item)

            if self.loc >= (self.capacity - 1):
                self.loc = 0
            else:
                self.loc += 1

            # else keep adding
        else:
            self.list.append(item)



    def get(self):
        return self.list


# capacity store the size of how big the ringring will be

ring = RingBuffer(5)

ring.append("a")
ring.append('a')
ring.append('b')
ring.append('c')
ring.append('d')
ring.append('e')
ring.append('f')
ring.append('g')
ring.append('h')
ring.append('i')

print(ring.get())